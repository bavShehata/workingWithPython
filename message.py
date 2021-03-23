names =  input("Please enter the names, separated by a comma: ").split(",")
assignments =  input("Please enter the number of assignments, separated by a comma: ").split(",")
grades =  input("Please enter the grades, separated by a comma: ").split(",")

# message string to be used for each student
# HINT: use .format() with this string in your for loop

message = "Hi {},\n\nThis is a reminder that you have {} assignments left to \
submit before you can graduate. You're current grade is {} and can increase \
to {} if you submit all assignments before the due date.\n\n"

# write a for loop that iterates through each set of names, assignments, and grades to print each student's message

for i in range(len(names)):
    print(message.format(names[i],assignments[i],grades[i],100))