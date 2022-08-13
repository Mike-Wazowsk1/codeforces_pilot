in_ = ['8',
       'woweffect',
       'abccbaabc',
       'testme',
       'strstr',
       'ababab',
       'abcdefg',
       'tetatet',
       'aaaaaaaaaaaaa']

out = [3, 6, 1, 1, 5, 1, 7, 13]


def find_prefix(s):
    max = 0
    for i in range(len(s) + 1):
        for j in range(len(s) + 1):
            if s[:i] == s[:j][::-1] and len(s[:i]) > max:
                max = len(s[:i])
    return max


def func():
    n = int(input())
    for i in range(n):
        print(find_prefix(str(input())))
func()
