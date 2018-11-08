def insert(a):
    for i in range(1, len(a)):
        current = 0
        while current < i:
            if a[i] < a[current]:
                a[current], a[i]= a[i] , a[current]
            current = current + 1
    return a

print (insert([12,54,66,43,11,33,34,33,1,45]))
Projects/SP-Midterm-Exam
C:\Users\PC\Projects\SP-Midterm-Exam