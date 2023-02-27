from django.db import models

from structure import fields


class Faculty(models.Model):
    id = fields.PositiveTinyAutoField(primary_key=True)
    financing = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        db_table = 'faculties'

    @property
    def acronym(self):
        return ''.join(
            word[0]
            for word in str(self.name).lower().split()
            if len(word) > 3
        )

    def __str__(self):
        return f'{self.name}'


class Department(models.Model):
    id = models.SmallAutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)
    building = models.IntegerField()
    financing = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )
    faculty = models.ForeignKey(Faculty, models.CASCADE)

    class Meta:
        db_table = 'departments'

    def __str__(self):
        return f'{self.name}'


class Curator(models.Model):
    id = fields.PositiveMediumAutoField(primary_key=True)
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)

    class Meta:
        db_table = 'curators'

    def __str__(self):
        return f'{self.name} {self.surname}'



class Subject(models.Model):
    id = models.SmallAutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        db_table = 'subjects'

    def __str__(self):
        return f'{self.name}'


class Teacher(models.Model):
    id = models.SmallAutoField(primary_key=True)
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    salary = models.DecimalField(
        max_digits=8,
        decimal_places=2
    )
    is_professor = models.BooleanField(default=0)
    subjects = models.ManyToManyField(
        Subject,
        through='Lecture',
    )

    class Meta:
        db_table = 'teachers'

    def __str__(self):
        return f'{self.name} {self.surname}'


class Lecture(models.Model):
    date = models.DateField()
    subject = models.ForeignKey(Subject, models.CASCADE)
    teacher = models.ForeignKey(Teacher, models.CASCADE)

    class Meta:
        db_table = 'lectures'

    def __str__(self):
        return f'{self.date} — {self.subject} ({self.teacher})'


class Student(models.Model):
    id = fields.PositiveMediumAutoField(primary_key=True)
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    rating = models.IntegerField()

    class Meta:
        db_table = 'students'

    def __str__(self):
        return f'{self.name} {self.surname}'


class Group(models.Model):
    id = fields.PositiveMediumAutoField(primary_key=True)
    name = models.CharField(max_length=10, unique=True)
    year = models.IntegerField()
    department = models.ForeignKey(Department, models.CASCADE)
    students = models.ManyToManyField(Student, db_table='groups_students')
    lectures = models.ManyToManyField(Lecture, db_table='groups_lectures')
    curators = models.ManyToManyField(Curator, db_table='groups_curators')

    class Meta:
        db_table = 'groups'

    def __str__(self):
        return f'({self.year}) {self.name}'

