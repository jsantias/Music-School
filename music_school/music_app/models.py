"""
Manages the MySQL database tables.
"""

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

#Creates UserProfile table using the variables specified as columns
class UserProfile(models.Model):
    SKILLS_CHOICES = [('Beginner','Beginner'), ('Intermediate', 'Intermediate'), ('Expert', 'Expert')]
    GENDER_CHOICES = [('M', 'Male'),('F', 'Female')]
    gender = models.CharField(choices=GENDER_CHOICES, max_length=1, blank=False)
    age = models.IntegerField(null=False)
    email = models.CharField(max_length=250)
    address = models.CharField(max_length=250)
    skill_level = models.CharField(choices=SKILLS_CHOICES,max_length=12, blank=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=False, related_name='profile')

    def __str__(self):
        return self.user.username

#Creates admin table using the variables specified as columns
class admin(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=18)

#Creates instrument table using the variables specified as columns
class instrument(models.Model):
    instrument_name = models.CharField(max_length=250)
    quantity = models.IntegerField(null=True)

##Creates teacher table using the variables specified as columns
class teacher(models.Model):
    name = models.CharField(max_length=250, null=False)
    room = models.IntegerField(null=False)

#Creates schedule table using the variables specified as columns
class schedule(models.Model):
    teacher = models.ForeignKey(teacher, on_delete=models.CASCADE)
    Instrument = models.CharField(max_length=100)
    Date = models.DateField()
    Time = models.TimeField(auto_now=False, auto_now_add=False)
    Lesson_id = models.CharField(max_length=100, null=False)
    Language = models.CharField(max_length=100)
    Booked = models.CharField(max_length=100)

#Creates bookings table using the variables specified as columns
class Bookings(models.Model): #shows student's bookings
	student = models.ForeignKey(User, on_delete=models.CASCADE)
	schedule = models.ForeignKey(schedule, on_delete=models.CASCADE)

#Creates invoice table using the variables specified as columns
class invoice(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	receipt = models.IntegerField(null=False)
