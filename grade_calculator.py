def get_valid_marks():
    while True:
        try:
            marks = int(input("Enter marks (0-100): "))
            if 0 <= marks <= 100:
                return marks
            else:
                print("Marks must be between 0 and 100. Try again.")
        except ValueError:
            print("Invalid input! Please enter a number.")


def calculate_grade(marks):
    if marks >= 90:
        return "A", "Excellent work! Keep shining 🌟"
    elif marks >= 80:
        return "B", "Very Good! Keep it up 👍"
    elif marks >= 70:
        return "C", "Good effort! You can do even better 😊"
    elif marks >= 60:
        return "D", "You passed. Keep practicing 💪"
    else:
        return "F", "Don't give up! Try harder next time 🔥"


def main():
    student_name = input("Enter student name: ")
    marks = get_valid_marks()

    grade, message = calculate_grade(marks)

    print("\nRESULT FOR:", student_name)
    print("Marks:", marks, "/100")
    print("Grade:", grade)
    print("Message:", message)


main()