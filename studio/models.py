from django.db import models

class Instructor(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField(blank=True)
    photo = models.ImageField(upload_to='instructors/', blank=True)  # Optional photo upload

    def __str__(self):
        return self.name

class YogaClass(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE, related_name='classes')
    date = models.DateTimeField()
    capacity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.title} - {self.date.strftime('%Y-%m-%d %H:%M')}"
