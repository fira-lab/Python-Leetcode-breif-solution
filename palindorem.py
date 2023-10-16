t = 6

test_cases = [
    "cbabc",
    "ab",
    "zza",
    "ba",
    "a",
    "nutforajaroftuna"
]

for i in range(t):
    a = test_cases[i].strip()

    if a != a[::-1]:
        print("YES")
        print(a + a[0])
    else:
        print("NO")
print('t',t)