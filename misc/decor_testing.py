import time


def time_measure(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        print(f"func {func.__name__} with args {args}, and kwargs {kwargs} took {time.time() - start}")
        return res
    return wrapper


@time_measure
def count_to(sec: int):
    for i in range(sec):
        print(i+1)
        time.sleep(1)


if __name__ == '__main__':
    count_to(3)
