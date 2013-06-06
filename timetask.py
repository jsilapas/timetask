#
# Define some utility functions / classes
#

#
# Main
#
if __name__ == "__main__":

    answer = "yes"
    tasks = {}

    #
    # Prompt loop
    #
    while answer == "yes":
        #Get user input
        task = raw_input("What is your first task?: ")
        tasktime = raw_input("How many minutes will it take?: ")

        #Add user input to dictionary and make pair:
        tasks["task"] = "tasktime"

        #Ask for more tasks
        answer = raw_input("Do you have any other tasks? (yes/no): ")

    #
    # Out of prompt loop
    #
    print tasks
