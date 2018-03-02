def capitalize(string):
    list_str = list(string)
    for i in range(len(list_str)):
        if i == 0:
            list_str[0] = list_str[0].upper()
        if list_str[i] == " ":
            list_str[i+1] = list_str[i+1].upper()
    return "".join(list_str)

if __name__ == '__main__':
    string = raw_input()
    capitalized_string = capitalize(string)
    print capitalized_string