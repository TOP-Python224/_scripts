
def person_about(name: str):
    print(f'Информация о владельце: {name}')


def pet_about(name: str):
    print(f'Информация о питомце: {name}')


about = (person_about, pet_about)

while True:
    person_name = input('\n > ')
    pet_name = input(' > ')

    names = (person_name, pet_name)

    for func, name in zip(about, names):
        func(**{'name': name})

