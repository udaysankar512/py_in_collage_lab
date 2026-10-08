class Result_Display:

    def calculate_grade(self, marks):
        if 90 <= marks <= 100:
            return "A"
        elif 80 <= marks <= 89:
            return "B"
        elif 70 <= marks <= 79:
            return "C"
        elif 60 <= marks <= 69:
            return "D"
        elif 0 <= marks < 60:
            return "F"
        else:
            raise ValueError("Marks must be between 0 and 100.")

    def output(self, subject_marks):
        if not subject_marks:
            raise ValueError("No subject marks provided.")

        total_marks = sum(subject_marks.values())
        total_subjects = len(subject_marks)
        percentage = (total_marks / (total_subjects * 100)) * 100
        overall_grade = self.calculate_grade(percentage)

        print("=" * 50)
        print("                STUDENT GRADE CARD")
        print("=" * 50)
        print(f"{'Subject':<15} {'Marks':<8} {'Grade'}")
        print("-" * 50)

        for subject, marks in subject_marks.items():
            grade = self.calculate_grade(marks)
            print(f"{subject:<15} {marks:<8} {grade}")

        print("-" * 50)
        print(f"Total Marks: {total_marks}/{total_subjects * 100}")
        print(f"Percentage: {percentage:.2f}%")
        print(f"Overall Grade: {overall_grade}")
        print("=" * 50)


if __name__ == "__main__":
    subject_names = ["Math", "Science", "English", "Computer", "History"]
    marks = {}

    for subject in subject_names:
        while True:
            try:
                value = float(input(f"Enter marks for {subject}: "))
                if 0 <= value <= 100:
                    marks[subject] = value
                    break
                else:
                    print("Marks must be between 0 and 100. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a numeric value.")

    card = Result_Display()
    card.output(marks)
