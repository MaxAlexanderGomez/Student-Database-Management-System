# Max Gomez
# Student score management program

names = []
student_ids = []
score_1 = []
score_2 = []
score_3 = []


def populate_arrays():
    """Collect information for four students."""

    # Prevent duplicate entries if P is selected again.
    names.clear()
    student_ids.clear()
    score_1.clear()
    score_2.clear()
    score_3.clear()

    for position in range(4):
        print(f"\nEntering student {position + 1} of 4")

        name = input("Please enter the student's name: ")
        student_id = input("Please enter the student's ID: ")

        try:
            first_score = float(input("Please enter the first score: "))
            second_score = float(input("Please enter the second score: "))
            third_score = float(input("Please enter the third score: "))
        except ValueError:
            print("Scores must be numbers. Please enter this student again.")
            return populate_arrays()

        names.append(name)
        student_ids.append(student_id)
        score_1.append(first_score)
        score_2.append(second_score)
        score_3.append(third_score)

    print("\nStudent information was successfully entered.")


def find_student_position():
    """Find and return a student's array position using the ID."""

    student_to_search = input("Please enter the student's ID: ")

    for position in range(len(student_ids)):
        if student_to_search == student_ids[position]:
            return position

    print("Student ID was not found.")
    return None


def display_student():
    """Display one student's information."""

    if not student_ids:
        print("No student information has been entered yet.")
        return

    position = find_student_position()

    if position is not None:
        print("\nStudent Information")
        print("-------------------")
        print(f"Name: {names[position]}")
        print(f"ID: {student_ids[position]}")
        print(f"First score: {score_1[position]:.2f}")
        print(f"Second score: {score_2[position]:.2f}")
        print(f"Third score: {score_3[position]:.2f}")


def average_grade(first_score, second_score, third_score):
    """Calculate and return the average of three scores."""

    return (first_score + second_score + third_score) / 3


def find_grade(average):
    """Return the letter grade for an average score."""

    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"


def calculate_grade():
    """Find a student and display the average and letter grade."""

    if not student_ids:
        print("No student information has been entered yet.")
        return

    position = find_student_position()

    if position is not None:
        average = average_grade(
            score_1[position],
            score_2[position],
            score_3[position]
        )

        letter_grade = find_grade(average)

        print(f"\nStudent: {names[position]}")
        print(f"Average score: {average:.2f}")
        print(f"Letter grade: {letter_grade}")


def update_student():
    """Update the name and scores for an existing student."""

    if not student_ids:
        print("No student information has been entered yet.")
        return

    position = find_student_position()

    if position is None:
        return

    print("Press Enter to keep the existing value.")

    new_name = input(f"Name [{names[position]}]: ")
    new_id = input(f"ID [{student_ids[position]}]: ")

    if new_name:
        names[position] = new_name

    if new_id:
        student_ids[position] = new_id

    try:
        new_score_1 = input(f"First score [{score_1[position]}]: ")
        new_score_2 = input(f"Second score [{score_2[position]}]: ")
        new_score_3 = input(f"Third score [{score_3[position]}]: ")

        if new_score_1:
            score_1[position] = float(new_score_1)

        if new_score_2:
            score_2[position] = float(new_score_2)

        if new_score_3:
            score_3[position] = float(new_score_3)

    except ValueError:
        print("A score was not updated because it was not a valid number.")
        return

    print("Student information was updated.")


def display_menu():
    """Display the menu and return the user's selection."""

    print("\n**** MENU OPTIONS ****")
    print("P - Populate student information")
    print("U - Update student information")
    print("D - Display student information")
    print("C - Calculate a student's grade")
    print("E - Exit")

    return input("Please enter your choice: ").strip().upper()


def main():
    """Run the student score program."""

    while True:
        choice = display_menu()

        if choice == "P":
            populate_arrays()
        elif choice == "U":
            update_student()
        elif choice == "D":
            display_student()
        elif choice == "C":
            calculate_grade()
        elif choice == "E":
            print("Thank you for using the program.")
            print("Bye")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
