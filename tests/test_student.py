"""Behavioral regression tests for all nine workshop requirements."""

import io
from pathlib import Path
import subprocess
import sys
import unittest
from unittest.mock import patch

from test import Student, main


class StudentTests(unittest.TestCase):
    def setUp(self):
        self.student = Student("DEMO-01", "Example Student")

    def test_identity_strips_whitespace(self):
        student = Student(" DEMO-02 ", " Example Two ")
        self.assertEqual(student.student_id, "DEMO-02")
        self.assertEqual(student.name, "Example Two")

    def test_invalid_identity(self):
        for value in ("", "  ", None, 4, True):
            for field in ("id", "name"):
                with self.subTest(value=value, field=field):
                    with self.assertRaisesRegex(ValueError, "nonempty string"):
                        Student(value, "Name") if field == "id" else Student(
                            "ID", value)

    def test_multiple_numeric_grades_and_decimal_average(self):
        for grade in (95.0, 72.5, 0, 100):
            self.student.add_grade(grade)
        self.assertEqual(self.student.grades, (95.0, 72.5, 0, 100))
        self.assertAlmostEqual(self.student.average, 66.875)

    def test_invalid_grades_leave_data_unchanged(self):
        for grade in ("95", "Fifty", None, True, False, -1, 101,
                      float("nan"), float("inf"), -float("inf"), 1 + 2j):
            with self.subTest(grade=grade):
                with self.assertRaisesRegex(ValueError, "finite number"):
                    self.student.add_grade(grade)
                self.assertEqual(self.student.grades, ())

    def test_ungraded_results(self):
        self.assertIsNone(self.student.average)
        self.assertEqual(self.student.letter_grade, "N/A")
        self.assertEqual(self.student.status, "Not graded")
        self.assertIs(self.student.honor_roll, False)

    def test_continuous_letter_pass_and_honor_thresholds(self):
        cases = (
            (0, "F", "Failed", False), (59, "F", "Failed", False),
            (59.99, "F", "Failed", False), (60, "D", "Passed", False),
            (69, "D", "Passed", False), (69.99, "D", "Passed", False),
            (70, "C", "Passed", False), (79, "C", "Passed", False),
            (79.99, "C", "Passed", False), (80, "B", "Passed", False),
            (89, "B", "Passed", False), (89.99, "B", "Passed", False),
            (90, "A", "Passed", True), (100, "A", "Passed", True),
        )
        for grade, letter, status, honor in cases:
            with self.subTest(grade=grade):
                student = Student("ID", "Name")
                student.add_grade(grade)
                self.assertEqual(student.average, grade)
                self.assertEqual(student.letter_grade, letter)
                self.assertEqual(student.status, status)
                self.assertIs(student.honor_roll, honor)

    def test_remove_value_removes_first_duplicate(self):
        for grade in (95, 70, 95):
            self.student.add_grade(grade)
        self.student.remove_grade_by_value(95)
        self.assertEqual(self.student.grades, (70, 95))

    def test_missing_value_leaves_grades_unchanged(self):
        self.student.add_grade(80)
        with self.assertRaisesRegex(ValueError, "not found"):
            self.student.remove_grade_by_value(70)
        self.assertEqual(self.student.grades, (80,))

    def test_invalid_removal_values(self):
        self.student.add_grade(80)
        for value in (True, "80", -1, 101, float("nan"), float("inf")):
            with self.subTest(value=value):
                with self.assertRaises(ValueError):
                    self.student.remove_grade_by_value(value)
                self.assertEqual(self.student.grades, (80,))

    def test_remove_zero_based_index(self):
        for grade in (10, 20, 30):
            self.student.add_grade(grade)
        self.student.remove_grade_by_index(1)
        self.assertEqual(self.student.grades, (10, 30))
        self.student.remove_grade_by_index(0)
        self.assertEqual(self.student.grades, (30,))

    def test_invalid_indices_leave_grades_unchanged(self):
        self.student.add_grade(80)
        for index in (-1, 1, 9, True, False, 0.0, "0", None):
            with self.subTest(index=index):
                with self.assertRaises(ValueError):
                    self.student.remove_grade_by_index(index)
                self.assertEqual(self.student.grades, (80,))

    def test_removing_from_empty_student(self):
        with self.assertRaisesRegex(ValueError, "not found"):
            self.student.remove_grade_by_value(80)
        with self.assertRaisesRegex(ValueError, "out of range"):
            self.student.remove_grade_by_index(0)

    def test_honor_and_status_recompute_after_changes(self):
        self.student.add_grade(100)
        self.assertIs(self.student.honor_roll, True)
        self.student.add_grade(0)
        self.assertIs(self.student.honor_roll, False)
        self.assertEqual(self.student.status, "Failed")
        self.student.remove_grade_by_index(1)
        self.assertIs(self.student.honor_roll, True)
        self.assertEqual(self.student.status, "Passed")
        self.student.remove_grade_by_value(100)
        self.assertIsNone(self.student.average)
        self.assertIs(self.student.honor_roll, False)
        self.assertEqual(self.student.status, "Not graded")

    def test_students_have_independent_grades(self):
        other = Student("OTHER", "Other Student")
        self.student.add_grade(90)
        self.assertEqual(other.grades, ())

    def test_report_has_all_seven_fields(self):
        self.student.add_grade(95)
        self.student.add_grade(72.5)
        self.assertEqual(self.student.report(), (
            "Student ID: DEMO-01\n"
            "Student Name: Example Student\n"
            "Number of Grades: 2\n"
            "Average Grade: 83.75\n"
            "Letter Grade: B\n"
            "Pass/Fail: Passed\n"
            "Honor Roll: False"
        ))

    def test_ungraded_report(self):
        report = self.student.report()
        self.assertIn("Number of Grades: 0", report)
        self.assertIn("Average Grade: N/A", report)
        self.assertIn("Letter Grade: N/A", report)
        self.assertIn("Pass/Fail: Not graded", report)
        self.assertIn("Honor Roll: False", report)


class CLITests(unittest.TestCase):
    def run_cli(self, inputs):
        result = subprocess.run(
            [sys.executable, "test.py"], input=inputs,
            capture_output=True, text=True,
            cwd=Path(__file__).resolve().parents[1], timeout=10,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stderr, "")
        self.assertNotIn("Traceback", result.stdout)
        return result.stdout

    def test_normal_create_add_remove_and_summary(self):
        output = self.run_cli(
            "1\nDEMO-01\nExample Student\n"
            "2\nDEMO-01\n95\n2\nDEMO-01\n72.5\n5\nDEMO-01\n"
            "3\nDEMO-01\n95\n4\nDEMO-01\n0\n5\nDEMO-01\n0\n"
        )
        self.assertIn("Average Grade: 83.75", output)
        self.assertIn("Letter Grade: B", output)
        self.assertEqual(output.count("Grade removed."), 2)
        self.assertIn("Pass/Fail: Not graded", output)
        self.assertIn("Goodbye.", output)

    def test_invalid_inputs_recover_without_crashes(self):
        output = self.run_cli(
            "\n9\n5\nMISSING\n1\n\nExample Student\n"
            "1\nDEMO-01\n\n1\nDEMO-01\nExample Student\n"
            "1\nDEMO-01\n2\nDEMO-01\nFifty\n"
            "2\nDEMO-01\nnan\n2\nDEMO-01\ninf\n"
            "2\nDEMO-01\n101\n3\nDEMO-01\n95\n"
            "4\nDEMO-01\n-1\n4\nDEMO-01\ntext\n0\n"
        )
        for message in ("Choose an option", "was not found",
                        "Student ID must", "Name must",
                        "already exists", "finite number", "out of range"):
            with self.subTest(message=message):
                self.assertIn(message, output)
        self.assertGreaterEqual(output.count("Error:"), 12)

    def test_multiple_students_are_addressable(self):
        output = self.run_cli(
            "1\nDEMO-01\nExample One\n1\nDEMO-02\nExample Two\n"
            "2\nDEMO-02\n90\n5\nDEMO-01\n5\nDEMO-02\n0\n"
        )
        self.assertIn("Student Name: Example One", output)
        self.assertIn("Student Name: Example Two", output)
        self.assertIn("Pass/Fail: Not graded", output)
        self.assertIn("Honor Roll: True", output)

    def test_eof_is_graceful(self):
        for inputs in ("", "1\n", "1\nDEMO-01\nExample Student\n2\n"):
            with self.subTest(inputs=inputs):
                self.assertIn("Input ended. Goodbye.", self.run_cli(inputs))

    def test_keyboard_interrupt_is_graceful(self):
        with patch("builtins.input", side_effect=KeyboardInterrupt):
            with patch("sys.stdout", new_callable=io.StringIO) as output:
                main()
        self.assertIn("Input ended. Goodbye.", output.getvalue())


if __name__ == "__main__":
    unittest.main()
