print('Перечислите до трёх участников записи: ')

participant1, participant2, participant3 = '', '', ''
participant1 = input('1. ')
if participant1:
    participant2 = input('2. ')
    if participant2:
        participant3 = input('3. ')
print()

if 'вокал' in participant1 or 'вокал' in participant2 or 'вокал' in participant3:
    print('LDC', end='')

if 'гитар' in participant1 + participant2 + participant3:
    print(' + SDC', end='')

if 'ударн' in participant1 + participant2 + participant3:
    print(' + DrumKit')
