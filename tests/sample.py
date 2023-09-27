from inqube import InQubeRunner

if __name__ == "__main__":
    cfg = """
    reader:
        class: inqube.readers.gsheets.GSheetsReader
        entity: spreadsheet
        spreadsheet_id: 18JCaEY_4Vu0YO9Qiiva5VP4G16pSiSf4o6mJeM-CqbU
        worksheet_id: 202308241616_parses
        header: true
    processors:
        - class: inqube.processors.drop_columns.DropColumnsProcessor
          columns_to_drop:
            - report_id
            - report_fight_id
    writer:
        class: inqube.writers.fs.FileSystemWriter
        filepath: /Users/ext.flteixeira/.sample
        format: json
    """
    InQubeRunner().run(cfg)
