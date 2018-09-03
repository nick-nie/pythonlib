import time


def elapsed_time(f):
    def wrapper():
        time1 = time.time()
        f()
        time2 = time.time()
        print('Elapsed Time: {0} ms'.format((time2 - time1) * 1000))
    return wrapper


@elapsed_time
def big_sum():
    num_list = []
    for n in (range(0, 1000)):
        num_list.append(n)
    print('Sum is: {0}'.format(sum(num_list)))


def main():
    big_sum()


if __name__ == "__main__":
    main()