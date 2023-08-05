import re

import ujson as json
import urequests as requests

DEBUG = False
_api_url = "http://worldtimeapi.org/api/ip"


def _query_local_timestring(api_url: str) -> tuple[str | None, str | None]:
    try:
        _response = requests.get(api_url)
        _data = json.loads(_response.text)

        if _response.status_code == 200:
            _datetime = _data.get("datetime", "N/A")
            _day_of_week = _data.get("day_of_week", "N/A")
            return _datetime, _day_of_week
        else:
            DEBUG and print("Error:", _data.get("error", "Unknown error"))
            return None, None
    except Exception as e:
        DEBUG and print("An error occurred:", e)
        return None, None


def get_local_datetime(api_url: str = _api_url) -> tuple[int, int, int, int, int, int, int, int]:
    # Returns datetime tuple (year, month, day, weekday {Mon=0}, hours, minutes, seconds, subseconds)
    _local_timestring, _day_of_week = _query_local_timestring(api_url)

    if _local_timestring:
        # Split ISO time by those characters.
        _regex = re.compile("[-T:.+]")
        _split = _regex.split(_local_timestring)

        _year = int(_split[0])
        _month = int(_split[1])
        _day = int(_split[2])

        _day_of_week = int(_day_of_week)

        _hour = int(_split[3])
        _minute = int(_split[4])
        _second = int(_split[5])
        _subsecond = int(_split[6])
    else:
        # Start of epoch
        _year = 2000
        _month = 1
        _day = 1

        # It was Saturday
        _day_of_week = 6

        _hour = 0
        _minute = 0
        _second = 0
        _subsecond = 0

    # Recalculate weekday from Sunday = 0 to Monday = 0 notation.
    return _year, _month, _day, (_day_of_week + 6) % 7, _hour, _minute, _second, _subsecond


if __name__ == "__main__":
    DEBUG = True
    print(get_local_datetime())
