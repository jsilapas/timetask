# Create an empty dictionary
tasks={}                                                                                                                                               
#Get user input
task = raw_input("What is your first task?:")
tasktime = raw_input("How many minutes will it take?:")

#Add user input to dictionary and make pair:
tasks["task"] = "tasktime"

#Ask for more tasks
answer = raw_input("Do you have any other tasks?:")

if answer == "yes":
    #loop to the beginning?
else:
    pass

print tasks
