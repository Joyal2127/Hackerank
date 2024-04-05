if __name__ == '__main__':
    score_list = []
    result = []

    for _ in range(int(input())):
        name = input()
        score = float(input())
        score_list.append(score)
        result.append([name, score])

    score_list.sort()
    second_lowest_score = None

    for score in score_list:
        if score != score_list[0]:
            second_lowest_score = score
            break

    names_with_second_lowest = []

    for name, score in result:
        if score == second_lowest_score:
            names_with_second_lowest.append(name)

    names_with_second_lowest.sort()

    for name in names_with_second_lowest:
        print(name)

