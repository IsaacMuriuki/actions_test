from django.test import TestCase


class MyTestCase(TestCase):
    def test_something(self):
        self.assertEqual(True, True)

    def testSthElse(self):
        self.assertEqual(False, False)

    def test(self):
        one = 1
        self.assertEqual(one, 1)

