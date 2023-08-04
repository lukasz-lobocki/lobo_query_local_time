import ujson as json
import urequests as requests

DEBUG = False
_api_url = "http://worldtimeapi.org/api/ip"


def _query_local_timestring(api_url: str) -> tuple[str, str]:
    try:
        _response = requests.get(api_url)
        _data = json.loads(_response.text)

        if _response.status_code == 200:
            _datetime = _data.get("datetime", "N/A")
            _day_of_week = _data.get("day_of_week", "N/A")
            return _datetime, _day_of_week
        else:
            DEBUG and print("Error:", _data.get("error", "Unknown error"))
            return None
    except Exception as e:
        DEBUG and print("An error occurred:", e)
        return None


def get_local_datetime():
    _local_timestring, _day_of_week = _query_local_timestring(_api_url)

    if _local_timestring:
        _date_part, _time_part = _local_timestring.split("T")
        _time_part, _ = _time_part.split("+")
        DEBUG and print(
            "_local_timestring {ts}; "
            "_date_part {dp}, "
            "_time_part {tp}".format(
                ts=_local_timestring,
                dp=_date_part,
                tp=_time_part))

        date_components = _date_part.split("-")
        time_components = _time_part.split(":")

        year = int(date_components[0])
        month = int(date_components[1])
        day = int(date_components[2])

        hour = int(time_components[0])
        minute = int(time_components[1])
        second = int(float(time_components[2]))

        return year, month, day, (_day_of_week + 6) % 7, hour, minute, second, 0


if __name__ == "__main__":
    DEBUG = True
    print(get_local_datetime())
