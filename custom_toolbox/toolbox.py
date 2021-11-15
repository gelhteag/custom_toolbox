from datetime import timezone
from datetime import datetime

def unix_to_datetime(unix_time):
#     '''unix_to_datetime(1622505700)=> ''2021-06-01 12:01am''''
    ts = int(unix_time/1000 if len(str(unix_time)) > 10 else unix_time) # /1000 handles milliseconds
    return datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d %l:%M%p').lower()
