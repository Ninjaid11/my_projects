from django.db import models


def example_func():
    return ["1", "faf", "ad"]


# Дитина (один до одного)
class Child(models.Model):
    id = models.AutoField(primary_key=True)
    age = models.IntegerField(default=18)
    email = models.EmailField(default=255, unique=True)
    fav_toy = models.CharField(max_length=255, blank=False, default="")

    def __str__(self):
        return f"Child {self.id}, Age: {self.age}"


class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    student_card_number = models.CharField(max_length=50, unique=True)
    email = models.EmailField(blank=True)
    group = models.ForeignKey('Group', on_delete=models.CASCADE, related_name="students", blank=True, null=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Group(models.Model):
    group_number = models.CharField(max_length=20)
    gaslo = models.CharField(max_length=255, blank=True)
    meeting_room = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.group_number


class LibraryCard(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE)
    issue_date = models.DateField()
    expiration_date = models.DateField()
    price = models.FloatField()

    def __str__(self):
        return f'Card for {self.student.first_name} {self.student.last_name}'


class Literature(models.Model):
    title = models.CharField(max_length=255)
    genre = models.CharField(max_length=100)
    publication_date = models.DateField()
    year_of_publication = models.IntegerField()

    def __str__(self):
        return self.title


class BookCheckout(models.Model):
    library_card = models.ForeignKey(LibraryCard, on_delete=models.CASCADE)
    literature = models.ForeignKey(Literature, on_delete=models.CASCADE)
    checkout_date = models.DateField()
    librarian_name = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.library_card.student.first_name} {self.library_card.student.last_name} - {self.literature.title}'