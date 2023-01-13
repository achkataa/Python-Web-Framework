from time import sleep


def slow_task(n):
    result = 0
    for i in range(n):
        sleep(1)
        result += i
    print(result)
