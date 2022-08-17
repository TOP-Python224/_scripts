alph = 'a\nb\nc\nd e\nf\ng\ni'
eol = '\n'
print(f'{alph = }\n')

print(f'{alph.split() = }')
print(f'{alph.split(" ") = }')
print(f'{alph.split(eol) = }')
print(f'{alph.split(" " + eol) = }')
print(f'{alph.split("def") = }')
print(f'{alph.split("d e") = }\n')

print(f'{alph.split(maxsplit=2) = }')
print(f'{alph.split(eol, 4) = }\n')


passwd = """root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/bin/sh
bin:x:2:2:bin:/bin:/bin/sh
sys:x:3:3:sys:/dev:/bin/sh
sync:x:4:65534:sync:/bin:/bin/sync
games:x:5:60:games:/usr/games:/bin/sh
man:x:6:12:man:/var/cache/man:/bin/sh
genndalf:x:100:100:genndalf:/home/genndalf:/bin/bash"""

# print(f'{passwd.split(eol) = }\n')

users = []
for line in passwd.split('\n'):
    # print(line.split(':'))
    users += [line.split(':')[0]]
print(users, end='\n\n')


print(' '.join(['abc', 'def']))
print('12 XII'.join(['abc', 'def']), end='\n\n')

print('\n'.join(users), end='\n\n')

print('\n'.join(('a1', 'a2')), end='\n\n')
