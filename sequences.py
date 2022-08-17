words = ['a', 'an', 'the']
print(f"{words = }\t{type(words) = }\t{len(words) = }\n")

listing = [1, 0.2, 'abcd', [4, 5], 6]
print(listing)
for elem in listing:
    print(elem, type(elem))
print()

print(f"{listing[3][1] = }")
print(f"{listing[1:3] = }")
print(f"{listing[1:2] = }\n")

print('listing[0] = 100')
listing[0] = 100
print(f"{listing}\t{id(listing) = }\n")

print("listing[-1] = 'six'")
listing[-1] = 'six'
print(f"{listing}\t{id(listing) = }\n")

print("listing[-3:-1] = [3, 0.4, 5, 0.6]")
listing[-3:-1] = [3, 0.4, 5, 0.6]
print(f"{listing}\t{id(listing) = }\n")

print("del listing[3]")
del listing[3]
print(f"{listing}\t{id(listing) = }\n")


new_listing = words + listing
print(f"{new_listing = }\n"
      f"{type(new_listing) = }\n"
      f"{len(new_listing) = }\n")

many_words = words * 3
print(f"{many_words = }\n"
      f"{type(many_words) = }\n"
      f"{len(many_words) = }\n")

l = []
print(f"{l = }\t{type(l) = }\t{len(l) = }\n")
for i in range(10, 100):
    if i % 11 == 0:
        # более медленый и более универсальный способ
        # l.append(i)
        # более быстрый и чаще всего более предпочтительный способ
        l += [i]
print(f"{l = }\t{type(l) = }\t{len(l) = }\n")

print(f"{id(l) = }")
print(f"{id(l.copy()) = }")
print(f"{l is l.copy() = }\n")

l.insert(1, 'twenty two')
l.append(22)
print(f"{l = }")

l.remove(22)
print(f"{l = }\n")


# кортеж
t = ()
t += (1,)
t += (2, 3)
t += (4, 5, 6, 3, 1)
print(f"{t = }\t{type(t) = }\t{len(t) = }\n")

# приведёт к ошибке
# t[2] = 0.3

print(f"{t.index(3) = }")
# приведёт к ошибке
# print(f"{t.index(33) = }")

print(f"{t.count(3) = }")
print(f"{t.count(6) = }")
