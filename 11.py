if __name__ == '__main__':
    n = int(input())
    student_marks = []
    
    # Inputting student names and marks
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks.append((name, scores))
    
    query_name = input()
    
    # Finding the student's scores and calculating the average
    for name, scores in student_marks:
        if name == query_name:
            average_score = sum(scores) / len(scores)
            print("{:.2f}".format(average_score))
            break
