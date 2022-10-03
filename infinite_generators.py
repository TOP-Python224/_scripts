from itertools import count, cycle, repeat

# for n in count(1):
    # print(n)


# for n in cycle(range(1, 10)):
    # print(n, end=' ')


for n in repeat('abc', 10):
    print(n, end=' ')


def my_count(start: int, step: int = 1):
    while True:
        yield start
        start += step

