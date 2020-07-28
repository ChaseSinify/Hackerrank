if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr = sorted(arr)
    s = arr[-1]
    i = 1
    while arr[-i] == s:
        i += 1
    print(arr[-i])
