from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Event(models.Model):
    name = models.CharField(max_length=200)
    venue = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Speaker(models.Model):
    name = models.CharField(max_length=200)
    short_bio = models.TextField()
    event = models.ManyToManyField(Event, through='Schedule')

    def __str__(self):
        return self.name


class Schedule(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    start_time = models.TimeField()
    end_time = models.TimeField()
    theme = models.CharField(max_length=200)
    speaker = models.ForeignKey(Speaker, on_delete=models.CASCADE)

    def __str__(self):
        return self.theme
