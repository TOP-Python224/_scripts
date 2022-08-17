for code in range(1072, 1104):
    print(f"chr({code}) = {chr(code)!r}")
print(f"\n{ord('ё') = }\n")

alphabet1 = {}
for code in range(1072, 1078):
    alphabet1[chr(code)] = code - 1071

alphabet2 = {'ё': 7}

alphabet3 = {}
for code in range(1078, 1104):
    alphabet3[chr(code)] = code - 1070

alphabet = alphabet1 | alphabet2 | alphabet3
print(alphabet)
