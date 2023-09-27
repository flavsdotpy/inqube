import gspread

from inqube.credentials import load_from_env
from inqube.exceptions import ConfigInvalidValueException, ConfigMissingRequiredException
from inqube.readers import BaseReader, BaseReaderConfig


class GSheetsReaderConfig(BaseReaderConfig):
    _NAME = "GSheetsReaderConfig"

    _ENTITY_REQUIRED = {
        "spreadsheet": {
            "spreadsheet_id",
            "worksheet_id",
            "header"
        }
    }
    _OPTIONAL = {
        "range": "A1:ZZ",
        "columns": []
    }


class GSheetsReader(BaseReader):
    _NAME = "GSheetsReader"
    _CFG_CLASS = GSheetsReaderConfig

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.creds = self.__load_creds()
        self.client = gspread.service_account_from_dict(self.creds)

    def __load_creds(self):
        return {
            "type": "service_account",
            "project_id": load_from_env("GSHEETS_PROJECT_ID"),
            "private_key_id": load_from_env("GSHEETS_PRIVATE_KEY_ID"),
            "private_key": load_from_env("GSHEETS_PRIVATE_KEY"),
            "client_email": load_from_env("GSHEETS_CLIENT_EMAIL"),
            "client_id": load_from_env("GSHEETS_CLIENT_ID"),
            "auth_uri": "https://accounts.google.com/o/oauth2/auth",
            "token_uri": "https://oauth2.googleapis.com/token",
            "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
            "client_x509_cert_url": load_from_env("GSHEETS_CLIENT_X509_CERT_URL"),
            "universe_domain": "googleapis.com"
        }

    def read_spreadsheet(self):
        spreadsheet = self.client.open_by_key(self.cfg.spreadsheet_id)
        values = spreadsheet.values_get(f"{self.cfg.worksheet_id}!{self.cfg.range}")["values"]
        if self.cfg.header:
            cols = values[0]
            return [
                {cols[i]: row[i] for i in range(len(row))}
                for row in values[1:]
            ]
        else:
            if not self.cfg.columns:
                raise ConfigMissingRequiredException("Missing columns config for headerless spreadsheet")
            cols = self.cfg.columns
            return [
                {cols[i]: row[i] for i in range(len(row))}
                for row in values
            ]

    def read(self) -> list[dict]:
        if self.cfg.entity == "spreadsheet":
            return self.read_spreadsheet()
        else:
            raise ConfigInvalidValueException(f"Invalid entity `{self.cfg.entity}`. Valid entities: spreadsheet")
