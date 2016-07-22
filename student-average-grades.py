# Creating average

student1 = input("Test score for student 1: ")
student1 = int (student1)

student2 = input("Test score for student 2: ")
student2 = int (student2)

student3 = input("Test score for student 3: ")
student3 = int (student3)

student4 = int(input("Test score for student 4: "))
student5 = int(input("Test score for student 5: "))

# Calculate the average score

average = (student1 + student2 + student3 + student4 + student5) / 5

if student1 > student2 and student1 > student3 and student1 > student4 and student1 > student5:
    print ("%d was the highest score" % (student1))

if student2 > student1 and student2 > student3 and student2 > student4 and student2 > student5:
    print ("%d was the highest score" % (student2))

if student3 > student1 and student3 > student2 and student3 > student4 and student3 > student5:
    print ("%d was the highest score" % (student3))

if student4 > student1 and student4 > student2 and student4 > student3 and student4 > student5:
    print ("%d was the highest score" % (student4))

if student5 > student1 and student5 > student2 and student5 > student3 and student5 > student4:
    print ("%d was the highest score" % (student5))

# Print averages

print ("Average test score is %d!" % (average))
