from django.db import models
# Create your models here.

class Patient(models.Model):
    choices = [
        ('male','male'),
        ('female','female'),
    ]
    name = models.CharField(max_length=20)
    date_of_birth = models.DateField()
    gender = models.CharField(choices=choices,max_length=6)

    def __str__(self):
        return self.name
    

class FamilyModel(models.Model):
    patient = models.ForeignKey(Patient, related_name='family_members', on_delete=models.CASCADE, null=True)
    related_patient = models.ForeignKey(Patient, related_name='related_to', on_delete=models.CASCADE, null=True)
    relation = models.CharField(max_length=50,null=True)

    def __str__(self):
        return f"{self.patient.name} - {self.relation} - {self.related_patient.name}"


class Medication(models.Model):
    patient = models.ForeignKey(Patient, related_name='medication', on_delete=models.CASCADE, null=True)
    medication_name = models.CharField(max_length=200)
    dosage = models.CharField(max_length=100)
    timings = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)
    prescribed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.medication_name} - {self.dosage} - {self.timings}"
