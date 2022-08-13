in_ = """
4
zaza
az
abacaba
ab
aaaaa
a
aaa
b
"""
out = """
6
14
0
6
"""


def count_good_substring(s, t):
    count = 0
    for i in range(len(s)):
        for j in range(i, len(s)):
            if t in s[i:j + 1]:
                break
            else:
                count += 1
    return count


def func():
    n = int(input())
    for i in range(n):
        s = input()
        t = input()
        print(count_good_substring(s, t))


func()
