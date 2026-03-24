def trigger_once(writer):
    return writer.trigger(once=True)


def trigger_processing_time(writer, interval="10 seconds"):
    return writer.trigger(processingTime=interval)


def trigger_continuous(writer, interval="1 second"):
    return writer.trigger(continuous=interval)
