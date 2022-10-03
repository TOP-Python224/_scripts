from json import dump, dumps, load, loads
from pprint import pprint

json_path1 = r'd:\G-Doc\Projects\GameDev\Zergen Studio\Biomorph-Resources\maps\first\first_test.json'
json_path2 = r'd:\G-Doc\Projects\GameDev\Zergen Studio\Biomorph-Resources\maps\first\first_test2.json'

with open(json_path1, encoding='utf-8') as f_in:
    data = load(f_in)

pprint(data)

with open(json_path1, encoding='utf-8') as f_in:
    string = loads(f_in.read())


data['_b_mountains']['changed'] = True

with open(json_path2, 'w', encoding='utf-8') as f_out:
    dump(data, f_out)

data['_b_mountains']['changed'] = None

with open(json_path2, 'w', encoding='utf-8') as f_out:
    f_out.write(dumps(data))
