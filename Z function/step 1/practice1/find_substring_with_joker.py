in_ = """
5
abacaba
a?a
test
?????
abaabaaab
a??a
ok
?
test
me
"""
out = """
3
0 2 4 
0

3
0 2 3 
2
0 1 
0

"""


def find_substring_with_joker(s, t):
    answ = []
    for i in range(len(s) - len(t) + 1):
        flag = True
        substring = s[i:i + len(t)]
        for j in range(len(t)):
            if t[j] == '?':
                continue
            elif t[j] != substring[j]:
                flag = False

        if flag:
            answ.append(i)
    return len(answ),answ


def func():
    n = int(input())
    for i in range(n):
        s = str(input())
        t = str(input())
        l,a = find_substring_with_joker(s,t)
        print(l)
        print(*a)


func()
