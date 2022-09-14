from pprint import pprint


families = {
    frozenset({'ivan', 'anna'}): [
        {'yarik': 7, 'potap': 4},
        {
            'income': 130000,
            'burden': {
                'mortgage': {
                    'total': 8500000, 
                    'period': 20, 
                    'percent': 0.07,
                    'annuitet': True
                }
            }
        }
    ],
    frozenset({'konstantin', 'alisa'}): [
        {},
        {
            'income': 115000,
            'burden': {
                'credit': {
                    'total': 235000, 
                    'period': 1, 
                    'percent': 0.23,
                    'annuitet': False
                }
            }
        }
    ]
}


def count_children(families_data: dict) -> dict:
    res = {}
    for family, data in families_data.items():
        family = ','.join(family)
        children_number = len(data[0])
        res[family] = children_number
    return res


print(count_children(families))



def dict_referencing(data: dict) -> dict:
    return data

new_dict = dict_referencing(families)
print(f'\n{new_dict is families = }\n')


def global_dict_change(data: dict) -> None:
    data['new_super_unique_key'] = hash('new_super_unique_key')

global_dict_change(families)
pprint(families)
