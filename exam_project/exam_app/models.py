from django.db import models

# მერვე დავალების პროექტს მივამატე ახალი

class Author(models.Model):
    name = models.CharField(max_length=100)
    birth_year = models.IntegerField()
    is_alive = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.TextField()
    pages = models.PositiveIntegerField()
    published_date = models.DateField()

    def __str__(self):
        return self.title


class Publisher(models.Model):
    company_name = models.CharField(max_length=100)
    founded = models.DateTimeField()
    employees = models.FloatField()

    def __str__(self):
        return self.company_name
