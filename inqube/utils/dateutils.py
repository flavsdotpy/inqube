from datetime import datetime, timedelta

from inqube.exceptions import ConfigInvalidValueException


def get_date_pair_for_delta(delta_type: str):
    if delta_type == "hour":
        end = datetime.now().replace(minute=0, second=0, microsecond=0)
        return end - timedelta(hours=1), end
    elif delta_type == "day":
        end = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
        return end - timedelta(days=1), end
    elif delta_type == "week":
        end = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
        return end - timedelta(days=1), end
    else:
        raise ConfigInvalidValueException(f"Invalid delta type `{delta_type}`. Valid delta types: hour, day, week")
