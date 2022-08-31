data = ['a', 'ba', 'ab', 'z', 'p', 'xvc', 'aa', 'dery', 'qwerty']

data_sorted = sorted(data)
print(data_sorted, end='\n\n')

data_len_sorted = sorted(data, key=lambda s: len(s)*1000 + sum(ord(c) for c in s))
print(data_len_sorted, end='\n\n')

data_len_sorted = sorted(data, key=len)
d = {
    len(elem): [s for s in data if len(s) == len(elem)] 
    for elem in data_len_sorted
}
data_len_alph_sorted = [
    elem 
    for ls in (sorted(l) for l in d.values()) for elem in ls
]
print(data_len_alph_sorted, end='\n\n')
