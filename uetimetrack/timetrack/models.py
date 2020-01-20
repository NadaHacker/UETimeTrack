from django.db import models
from django.contrib.auth.models import User
from datetime import date


# Create your models here.
class TimeEntry(models.Model):
    # Username of the student that submitted the entry
    # username_submitted = models.CharField(max_length=100)
    username_submitted = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    # The status of the entry
    status = (
        'Submitted',
        'Denied',
        'Approved',
    )

    # Username of the student leader that reviewed the entry
    username_student_leader = models.CharField(max_length=100)

    # The date the entry was submitted
    # date_submitted = models.DateField()
    date_submitted = date.today()

    # The time listed for the specific time entry
    time_entered = models.TimeField()

