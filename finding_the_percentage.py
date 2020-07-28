if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    vals = student_marks[query_name]
    summy = sum(vals)
    # for i in vals:
    #     summy += i
    avg = summy / len(vals)
    print('{0:.2f}'.format(avg))
