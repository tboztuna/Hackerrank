def split_and_join(line):
    splitted_str = line.split(" ")
    return "-".join(splitted_str)

if __name__ == '__main__':
    line = raw_input()
    result = split_and_join(line)
    print result