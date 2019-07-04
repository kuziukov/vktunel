import math


def convert_size(size_bytes) -> str:
    names_of_size = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
    if size_bytes == 0:
        return "0B"

    log_of_bytes = int(math.log(size_bytes, 1000))
    number = round(size_bytes / math.pow(1000, log_of_bytes), 2)
    return "%s %s" % (number, names_of_size[log_of_bytes])
