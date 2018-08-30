SUFFIX = {1000: ['KB', 'MB', 'GB', 'TB'],
          1024: ['KiB', 'MiB', 'GiB', 'TiB']}


def approximate_size(size, a_kilobyte_is_1024_bytes=False):
    """
    Convert a file size to human-readable form.
    :param memory:
    :param a_kilobyte_is_1024_bytes: -- if True, use multiples of 1024
                                        if False(default), use multiples of 1000
    :return: string
    """
    if size < 0:
        raise ValueError('value should be non-negative')
    multiple = 1024 if a_kilobyte_is_1024_bytes else 1000
    for suffix in SUFFIX[multiple]:
        size /= multiple
        if size < multiple:
            return '{0:.1f} {1}'.format(size, suffix)
    raise ValueError('value too large')

# if __name__ == '__main__':
#     # print(approximate_size(-1, True))
#     print(approximate_size(1000, False))
#     print(approximate_size(4096, a_kilobyte_is_1024_bytes=True))
#     print(approximate_size(10000000, True))
#     print(approximate_size(1000000000000000000, True))
