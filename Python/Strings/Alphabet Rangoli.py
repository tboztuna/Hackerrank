import string


def print_rangoli(size):
    alpha = string.ascii_lowercase

    L = []
    for i in range(size):
        s = "-".join(alpha[i:size])
        L.append((s[::-1] + s[1:]).center(4 * n - 3, "-")) # Thanks to Martin Boissier
    print('\n'.join(L[:0:-1] + L))


if __name__ == "__main__":
    n = int(raw_input())
    print_rangoli(n)
