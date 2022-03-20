from django.db import models

class Registration(models.Model):
    aid_db = models.AutoField(primary_key=True)
    patientName_db = models.CharField(max_length=100)
    phoneNo_db = models.CharField(max_length=13)
    doctorName = models.CharField(max_length=100)
    specialist_db = models.CharField(max_length=100)
    day_db = models.CharField(max_length=100)
    time_db = models.CharField(max_length=100)
    AM_PM_db = models.CharField(max_length=100,default="AM/PM")
    fees_db = models.IntegerField()
    tokenNo_db = models.IntegerField()

    def __str__(self):
        return self.patientName_db