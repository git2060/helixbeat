from rest_framework import serializers
from .models import Patient
from .models import FamilyModel
from .models import Medication


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model=Patient
        fields=['id', 'name', 'date_of_birth', 'gender']


class FamilyMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = FamilyModel
        fields = ['id', 'patient', 'related_patient', 'relation']


class MedicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medication
        fields = ['id', 'patient', 'medication_name', 'dosage', 'timings', 'is_active', 'prescribed_at']



