from django.test import TestCase

# Create your tests here.
class BaseTest(TestCase):

    def setUp(self):
        super().setUp()

    def tearDown(self):
        super().tearDown()

    def test_harness(self):
        return

