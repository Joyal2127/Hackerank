if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))


    b = set(arr)
    sort = sorted(b)

    print(sort[-2])
