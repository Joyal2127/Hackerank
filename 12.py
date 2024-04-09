if __name__ == '__main__':
    N = int(input())
    l = []

    for i in range(N):
        user = input().split()
        command = user[0]
        if command == "insert":
            l.insert(int(user[1]), int(user[2]))
        elif command == "print":
            print(l)
        elif command == "remove":
            l.remove(int(user[1]))
        elif command == "append":
            l.append(int(user[1]))
        elif command == "sort":
            l.sort()
        elif command == "pop":
            l.pop()
        elif command == "reverse":
            l.reverse()
