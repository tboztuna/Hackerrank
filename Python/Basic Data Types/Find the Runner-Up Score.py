if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())
    max = max(arr)
    arr.sort()
    for i in arr:
        if i < max:
            second_max = i

    print second_max
