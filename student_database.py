# Max Gomez
# Student score management program

# Five ARRAYS to be used total. One for name and ID

NamesArray = []
IdArray = []

# Score arrays
Score1Array = []
Score2Array = []
Score3Array = []


# Function to populate arrays
def PopulateArray():

    # For loop in the range of 4 values
    for position in range(0, 4):

        # Name array
        name = input("Please enter a student's name :\n")
        NamesArray.append(name)

        # ID array
        IDs = input("Please enter the student's ID:\n")
        IdArray.append(IDs)

        # First score
        firstscore = input("Please enter first score:\n")
        Score1Array.append(firstscore)

        # Second score
        secondscore = input("Please enter scond score:\n")
        Score2Array.append(secondscore)

        # Third score
        thirdscore = input("Please enter third score:\n")
        Score3Array.append(thirdscore)


# Function to search for a student
def SearchAccount():

    studenttosearch = input("Please enter the ID of the student:\n")

    # Search through all students
    for position in range(0, 4):

        if (studenttosearch == IdArray[position]):

            print("The student name is: " + NamesArray[position])
            print("ID is: " + IdArray[position])
            print("First score is: " + str(Score1Array[position]))
            print("Second score is: " + str(Score2Array[position]))
            print("Third score is: " + str(Score3Array[position]))

            break


# Find average grade
def Averagegrade(firstscore, secondscore, thirdscore):

    total = firstscore + secondscore + thirdscore / 3
    return total


# Function for letter grading
def findgrade(total):

    grade = ""

    # Over 90 for A
    if (total >= 90):
        grade = "A"

    # Between 80 and 89
    elif (total >= 80 and total < 89):
        grade = "B"

    # Between 70 and 79
    elif (total >= 70 and total < 79):
        grade = "C"

    # Between 60 and 69
    elif (total >= 60 and total < 69):
        grade = "D"

    # Below 60
    elif (total < 60):
        grade = "F"

    return grade


# Function to display menu
def displaymenu():

    print("**** MENU OPTIONS ****")
    print("Type P to populate the student information.")
    print("Type U to update student Information")
    print("Type D to display the student information.")
    print("Type C to calculate the Grade.")
    print("Type E to exit")

    response = input("Please enter your choice:\n")
    return response


# Main program
choice = displaymenu()

while (choice != ""):

    # Populate arrays
    if (choice == "P"):
        PopulateArray()

    # Search for a student
    elif (choice == "D"):
        SearchAccount()

    # Exit
    elif (choice == "E"):
        print("Thank you for using the program.")
        print("Bye")
        break

    # Invalid choice
    else:
        print("Invalid choice. Please try again!")

    # Display menu again
    choice = displaymenu()

# FINAL
