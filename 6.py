def split_and_join(line):
    s = line.split(" ")
    b = "-"
    c = b.join(s)
    return c

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)