def mutate_string(string, position, character):
    mutable_str = list(string)
    mutable_str[position] = character
    return "".join(mutable_str)

if __name__ == '__main__':
    s = raw_input()
    i, c = raw_input().split()
    s_new = mutate_string(s, int(i), c)
    print s_new