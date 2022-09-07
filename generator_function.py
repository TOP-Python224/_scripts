def reverse_counter(start: int, step: int = 1):
    while start >= 0:
        yield start
        start -= step


gen_counter = reverse_counter(10)
print(f'{gen_counter = }\n{type(gen_counter) = }\n')

# for n in gen_counter:
    # print(n, end=' ')

print(gen_counter.__next__())
print(gen_counter.__next__())
print(gen_counter.__next__())
print(gen_counter.__next__())
print(gen_counter.__next__())
print(gen_counter.__next__())
print(gen_counter.__next__())
print(gen_counter.__next__())
print(gen_counter.__next__())
print(gen_counter.__next__())
print(gen_counter.__next__())
