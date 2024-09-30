import unittest

# Тест пройден Сначала тесты, потом разработка
from Behavioral import Student, Outside, Inside, Window, Walk
class TestStudent(unittest.TestCase):

    def setUp(self):
        self.student = Student()

    def test_initial_state(self):
        self.assertEqual(self.student.where(), "Студент не в ВУЗе")

    def test_state_inside(self):
        self.student.set_state(Inside())
        self.assertEqual(self.student.where(), "Студент учится")

    def test_state_window(self):
        self.student.set_state(Window())
        self.assertEqual(self.student.where(), "Студент в ВУЗе, но сейчас у него окно")

    def test_state_outside(self):
        self.student.set_state(Outside())
        self.assertEqual(self.student.where(), "Студент не в ВУЗе")

    def test_state_walk(self):
        self.student.set_state(Walk())
        self.assertEqual(self.student.where(), "Студент в пути")

if __name__ == "__main__":
    unittest.main()
