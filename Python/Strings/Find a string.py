def count_substring(string, sub_string):
    str_count = 0
    for i in range(len(string)):
        new_str = string[i:len(sub_string)+i]
        if new_str == sub_string and len(new_str) == len(sub_string):
            str_count = str_count + 1
    return str_count

if __name__ == '__main__':
    string = raw_input().strip()
    sub_string = raw_input().strip()

    count = count_substring(string, sub_string)
    print count