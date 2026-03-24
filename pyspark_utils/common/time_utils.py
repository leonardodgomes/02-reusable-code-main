from datetime import datetime

def now():
    return datetime.utcnow()


def timestamp_str():
    return datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
