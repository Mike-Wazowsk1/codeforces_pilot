in_ = """
4
abacaba
aaaa
barbarmiakirkudu
abaabaababaab
"""
out = """
10
0
34
41
"""


def find_prefix_and_suffix(s):
    count = 0
    for i in range(1,len(s)+1):
        prefix = s[:i]
        suffix = s[-i:]
        if prefix != suffix:
            for j in range(len(s)):
                if prefix == s[j:j+len(prefix)] or suffix == s[j:j+len(suffix)]:
                    count+=1


    return count


def func():
    n = int(input())
    for i in range(n):
        print(find_prefix_and_suffix(str(input())))
func()