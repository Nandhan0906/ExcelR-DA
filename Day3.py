#DAY3

"""Write a Python program that takes a student's marks in three subjects as input.
If the average is greater than or equal to 90, print "Grade: A".
If the average is between 80 and 89, print "Grade: B".
If the average is between 70 and 79, print "Grade: C".
Otherwise, print "Grade: Fail"."""

subject1=int(input("Enter first subject: "))
subject2=int(input("Enter second subject: "))
subject3=int(input("Enter third subject: "))
average=(subject1+subject2+subject3)//3
print("Average of three subjects is:",average)
if average>=90:
    print("Grade: A")
elif average>=80 and average<=89:
    print("Grade: B")
elif average>=70 and average<=79:
    print("Grade: C")
else:
    print("Grade: Fail")