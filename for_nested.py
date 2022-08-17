for i in range(3):
    print('итерация внешнего цикла')
    for j in range(4):
        print('\tитерация внутреннего цикла')
        print(f"\t{i = }\t{j = }")
    print()


for _ in range(10):
    for _ in range(10):
        for _ in range(10):
            for _ in range(10):
                for _ in range(10):
                    for _ in range(10):
                        print()
