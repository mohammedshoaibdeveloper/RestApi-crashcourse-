from django.test import TestCase
from .models import Author, Book

class AuthorModelTestCase(TestCase):
    def setUp(self):
        self.author = Author.objects.create(
            firstname='John',
            lastname='Doe',
            birth_date='1980-01-01'
        )
    
    def test_author_creation(self):
        self.assertTrue(isinstance(self.author, Author))
        self.assertEqual(self.author.firstname, 'John')
        self.assertEqual(self.author.lastname, 'Doe')
        self.assertEqual(self.author.birth_date, '1980-01-01')

class BookModelTestCase(TestCase):
    def setUp(self):
        self.author = Author.objects.create(
            firstname='Jane',
            lastname='Doe',
            birth_date='1981-01-01'
        )
        self.book = Book.objects.create(
            author=self.author,
            title='My First Book',
            category='Fiction',
            published='2000-01-01',
            price='19.99',
            rating=4
        )

    def test_book_creation(self):
        self.assertTrue(isinstance(self.book, Book))
        self.assertEqual(self.book.title, 'My First Book')
        self.assertEqual(self.book.category, 'Fiction')
        self.assertEqual(self.book.published, '2000-01-01')
        self.assertEqual(self.book.price, '19.99')
        self.assertEqual(self.book.rating, 4)

from datetime import datetime, date
class BookModelTestCase(TestCase):
    def setUp(self):
        Author.objects.create(
            firstname='John',
            lastname='Doe',
            birth_date='1980-01-01'
        )
        Author.objects.create(
            firstname='Jane',
            lastname='Doe',
            birth_date='1981-01-01'
        )
        Book.objects.create(
            author=Author.objects.get(firstname='John'),
            title='My First Book',
            category='Fiction',
            published='2000-01-01',
            price='19.99',
            rating=4
        )

    def test_all_data(self):
        authors = Author.objects.all()
        self.assertEqual(authors.count(), 2)

        books = Book.objects.all()
        self.assertEqual(books.count(), 1)
        self.assertEqual(books[0].author.firstname, 'John')
        self.assertEqual(books[0].title, 'My First Book')
        self.assertEqual(books[0].category, 'Fiction')
        expected_date = date(2000, 1, 1)
        self.assertEqual(books[0].published, expected_date)
        self.assertEqual(str(books[0].price), '19.99')
        self.assertEqual(books[0].rating, 4)


