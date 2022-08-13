in_ = """
abacaba
a
aabbb
babaabbb
"""
out = """
0 0 1 0 3 0 1 
0 
0 1 0 0 0 
0 0 2 0 0 1 1 1 
"""


def simple_z(s):
    arr = [0] * len(s)
    for i in range(len(s)):
        substring = s[i:]
        count = 0
        for j in range(len(substring)):
            if s[j] != substring[j]:
                break
            else:
                count += 1
        arr[i] = count

    arr[0] = 0
    return arr


def func():
    s = input()
    print(*simple_z(s))


func()
