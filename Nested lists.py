students = {}
for i in range(int(raw_input())):
    name = raw_input()
    grade = float(raw_input())
    if grade in students:
        students[grade].append(name)
    else:
        students[grade] = [name]
sorted_students = sorted(students.items())
for x in sorted(sorted_students[1][1]):
    print x
