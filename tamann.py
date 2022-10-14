batch1=["aniket","tamanna","priya","amrita"]
student=open("navgurukul.txt","w")
student.write("\n")
student.write("\n")
student.write("\n")
for student in batch1:
    print(student)
student.write("\n")
student.write("\n")
student.close()
