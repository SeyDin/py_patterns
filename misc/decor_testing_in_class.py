import time


def time_measure(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        print(args[0].class_attr)
        print(f"func {func.__name__} with args {args}, and kwargs {kwargs} took {time.time() - start}")
        return res
    return wrapper


class A:
    class_attr = 1

    @time_measure
    def count_to(self, sec: int):
        for i in range(sec):
            print(i+1)
            time.sleep(1)

    # тут не получится получить инфу о классе
    @staticmethod
    @time_measure
    def count_to(sec: int):
        for i in range(sec):
            print(i + 1)
            time.sleep(1)


if __name__ == '__main__':
    A.count_to(3)
