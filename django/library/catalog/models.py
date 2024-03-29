from django.db import models
# pip install transliterate
from transliterate import translit


class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    def initials(self, dot='.'):
        return f'{str(self.first_name)[0]}{dot}{str(self.last_name)[0]}{dot}'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, models.CASCADE)

    def __str__(self):
        return f'{self.title}'


class Publisher(models.Model):
    name = models.CharField(max_length=50)
    authors = models.ManyToManyField(Author)
    books = models.ManyToManyField(Book)

    @property
    def translit_lc(self):
        return translit(
            str(self.name).lower(),
            language_code='ru',
            reversed=True
        )

    def __str__(self):
        return f'{self.name}'

