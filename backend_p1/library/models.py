from django.db import models
from django.urls import reverse
import uuid


class Genre(models.Model):
    name = models.CharField(max_length=50, help_text="Enter the Genre name")

    class Meta:
        ordering = ['name']



    def __str__(self):
        return self.name


class Language(models.Model):
    name = models.CharField(
        max_length=50, help_text="Enter the book language")

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey("Author", on_delete=models.RESTRICT)
    summary = models.TextField(
        max_length=1000, help_text="Enter a brief book description")
    isbn = models.CharField('ISBN', max_length=50,
                            unique=True, help_text="Enter the ISBN of the book")
    genre = models.ManyToManyField(
        Genre, help_text="Select genre for your book")
    language = models.ForeignKey('Language', on_delete=models.RESTRICT)

    class Meta:
        ordering = ['title', 'author']

    def __str__(self):
        return self.title

    def display_genre(self):
        return ','.join(genre.name for genre in self.genre.all()[:3])

    display_genre.short_description = 'Genre'


    def get_absolute_url(self):
        return reverse("book-details", args=[str(self.id)])


class BookInstance(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                          help_text="Unique id for particular books")
    due_back = models.DateField(auto_now=False, auto_now_add=False)
    LOAN_STATUS = (
        ('m', 'Maintainance'),
        ('a', 'Available'),
        ('o', 'On loan'),
        ('r', 'Reserved'),
    )
    status = models.CharField(max_length=1, choices=LOAN_STATUS,
                              null=True, default='m', help_text="Book availability")
    book = models.ForeignKey('Book', on_delete=models.RESTRICT)

    class Meta:
        ordering = ['due_back']

    def __str__(self):
        return f'{self.id} ({self.book.title})'


class Author(models.Model):
    first_name = models.CharField(
        max_length=100, help_text="Enter your first name")
    last_name = models.CharField(
        max_length=100, null=True, blank=True, help_text="Enter your last name")
    d_birth = models.DateField("Date of Birth",
        auto_now=False, auto_now_add=False, null=True, blank=True)
    d_dead = models.DateField( "Dead",
        auto_now=False, auto_now_add=False, null=True, blank=True)

    class Meta:
        ordering = ['last_name', 'first_name']

    def __str__(self):
        return f'{self.last_name} {self.first_name}'
