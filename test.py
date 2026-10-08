"""Student grade management with validated inputs and a terminal interface."""

from numbers import Real


MIN_GRADE = 0
MAX_GRADE = 100
PASS_THRESHOLD = 60
HONOR_THRESHOLD = 90
LETTER_THRESHOLDS = (
    (HONOR_THRESHOLD, "A"), (80, "B"), (70, "C"), (PASS_THRESHOLD, "D"),
)


class Student:
    """Keep identity and grades; derive results from current grades."""

    def __init__(self, student_id: str, name: str):
        for label, value in (("Student ID", student_id), ("Name", name)):
            if not isinstance(value, str) or not value.strip():
                raise ValueError(f"{label} must be a nonempty string.")
        self.student_id = student_id.strip()
        self.name = name.strip()
        self._grades: list[Real] = []

    @property
    def grades(self) -> tuple[Real, ...]:
        """Expose grades without permitting unvalidated list mutations."""
        return tuple(self._grades)

    @staticmethod
    def _validate_grade(grade: Real) -> None:
        if (isinstance(grade, bool) or not isinstance(grade, Real)
                or not MIN_GRADE <= grade <= MAX_GRADE):
            raise ValueError("Grade must be a finite number from 0 to 100.")

    def add_grade(self, grade: Real) -> None:
        """Add one numeric grade in the inclusive range 0-100."""
        self._validate_grade(grade)
        self._grades.append(grade)

    def remove_grade_by_value(self, grade: Real) -> None:
        """Remove only the first matching grade, or leave grades unchanged."""
        self._validate_grade(grade)
        try:
            self._grades.remove(grade)
        except ValueError:
            raise ValueError("Grade value was not found.") from None

    def remove_grade_by_index(self, index: int) -> None:
        """Remove a grade using a nonnegative, zero-based index."""
        if isinstance(index, bool) or not isinstance(index, int):
            raise ValueError("Grade index must be a zero-based integer.")
        if not 0 <= index < len(self._grades):
            raise ValueError("Grade index is out of range (zero-based).")
        del self._grades[index]

    @property
    def average(self) -> float | None:
        return sum(self._grades) / len(self._grades) if self._grades else None

    @property
    def letter_grade(self) -> str:
        average = self.average
        if average is None:
            return "N/A"
        for threshold, letter in LETTER_THRESHOLDS:
            if average >= threshold:
                return letter
        return "F"

    @property
    def status(self) -> str:
        average = self.average
        if average is None:
            return "Not graded"
        return "Passed" if average >= PASS_THRESHOLD else "Failed"

    @property
    def honor_roll(self) -> bool:
        average = self.average
        return average is not None and average >= HONOR_THRESHOLD

    def report(self) -> str:
        """Format all seven required summary fields for terminal display."""
        average = self.average
        display_average = "N/A" if average is None else f"{average:.2f}"
        return (
            f"Student ID: {self.student_id}\n"
            f"Student Name: {self.name}\n"
            f"Number of Grades: {len(self._grades)}\n"
            f"Average Grade: {display_average}\n"
            f"Letter Grade: {self.letter_grade}\n"
            f"Pass/Fail: {self.status}\n"
            f"Honor Roll: {self.honor_roll}"
        )


def main() -> None:
    """Manage students in memory and report expected input errors."""
    students: dict[str, Student] = {}
    print("Student Grade Management (data is not saved after exit)")
    try:
        while True:
            print("\n1 Create student | 2 Add grade | 3 Remove by value")
            print("4 Remove by index (zero-based) | 5 Summary | 0 Exit")
            choice = input("Choice: ").strip()
            if choice == "0":
                print("Goodbye.")
                return
            try:
                if choice == "1":
                    student_id = input("Student ID: ").strip()
                    if student_id in students:
                        raise ValueError("Student ID already exists.")
                    student = Student(student_id, input("Student name: "))
                    students[student.student_id] = student
                    print("Student created.")
                elif choice in {"2", "3", "4", "5"}:
                    student_id = input("Student ID: ").strip()
                    if student_id not in students:
                        raise ValueError("Student ID was not found.")
                    student = students[student_id]
                    if choice == "2":
                        student.add_grade(float(input("Grade (0-100): ")))
                        print("Grade added.")
                    elif choice == "3":
                        student.remove_grade_by_value(float(input("Grade: ")))
                        print("Grade removed.")
                    elif choice == "4":
                        print(f"Grades (zero-based order): {student.grades}")
                        index = int(input("Grade index (zero-based): "))
                        student.remove_grade_by_index(index)
                        print("Grade removed.")
                    else:
                        print(student.report())
                else:
                    raise ValueError("Choose an option from 0 to 5.")
            except ValueError as error:
                print(f"Error: {error}")
    except (EOFError, KeyboardInterrupt):
        print("\nInput ended. Goodbye.")


if __name__ == "__main__":
    main()
