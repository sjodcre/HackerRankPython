if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    def Average(lst): 
        return sum(lst) / len(lst) 

    print("{:.2f}".format(Average(student_marks[query_name])))

    
