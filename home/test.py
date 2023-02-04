from django.test import TestCase
from .models import Author

class AuthorTestCase(TestCase):
    def setUp(self):
        Author.objects.create(nickname='shoaib', firstname='Muhammad',lastname='Shoaib',birth_date="2003-06-16")
        
    def test_my_model(self):
        my_model = Author.objects.get(nickname='shoaib', firstname='Muhammad',lastname='Shoaib',birth_date="2003-06-16")
        self.assertEqual(my_model.firstname, 'Muhammad')


