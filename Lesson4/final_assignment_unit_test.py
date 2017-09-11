import unittest
import Lesson4.final_assignment as finalAssignment


class FinalAssignmentUnitTest(unittest.TestCase):
    def test_ritprijs_without_discount(self):
        result = finalAssignment.ritprijs(20, False, 100)
        self.assertEqual(result, 100 * 0.80)

    def test_ritprijs_with_weekend_discount(self):
        result = finalAssignment.ritprijs(20, True, 100)
        self.assertEqual(result, (100 * 0.80) * 0.60)

    def test_ritprijs_with_low_age(self):
        result = finalAssignment.ritprijs(10, False, 100)
        self.assertEqual(result, (100 * 0.80) * 0.70)

    def test_ritprijs_with_high_age(self):
        result = finalAssignment.ritprijs(70, False, 100)
        self.assertEqual(result, (100 * 0.80) * 0.70)

    def test_ritprijs_with_low_age_in_weekend(self):
        result = finalAssignment.ritprijs(10, True, 100)
        self.assertEqual(result, (100 * 0.80) * 0.65)

    def test_ritprijs_with_high_age_in_weekend(self):
        result = finalAssignment.ritprijs(70, True, 100)
        self.assertEqual(result, (100 * 0.80) * 0.65)


if __name__ == '__main__':
    unittest.main()
