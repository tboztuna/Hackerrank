from collections import OrderedDict


def merge_the_tools(string, k):
    for x in range(0,len(string),k):
        str = string[x:x + k]
        print ''.join(list(OrderedDict.fromkeys(str)))


if __name__ == '__main__':
    string, k = raw_input(), int(raw_input())
    merge_the_tools(string, k)