from django.shortcuts import render, get_object_or_404
from .serializer import PatientSerializer
from .serializer import FamilyMemberSerializer
from .serializer import MedicationSerializer
from .models import Patient
from .models import FamilyModel
from .models import Medication
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
# Create your views here.


###########################Patient Models############################################################################
########List and Add Patient Details#################
class ListAndAddPatient(APIView):
    def  get(self, request):
        data = Patient.objects.all()
        serializer= PatientSerializer(data,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializers= PatientSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data,status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

########Update Patient Details#################
class UpdatePatient(APIView):
    def get_object(self,pk):
        try:
            return Patient.objects.get(pk=pk)      
        except Patient.DoesNotxist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
    def get(self, request,pk):
        data=self.get_object(pk)
        serializer=PatientSerializer(data)
        return Response(serializer.data, status=status.HTTP_200_OK)    
        
    def put(self, request, pk):    
        data=self.get_object(pk)
        serializers= PatientSerializer(data,data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

########Retrive Patient Details#################
class RetrievePatient(APIView): 
    def get_object(self,pk):
        try:
            return Patient.objects.get(pk=pk)      
        except Patient.DoesNotxist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request,pk):
        data=self.get_object(pk)
        serializer=PatientSerializer(data)
        return Response(serializer.data, status=status.HTTP_200_OK)   
      
    def get(self, request, pk):
        data=self.get_object(pk)
        serializer = PatientSerializer(data)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    


########################Family Models#############################################################################
########List and Add Patient Family#################
class ListAndAddFamilyMembers(APIView):
    def get_object(self,pk):
        try:
            return Patient.objects.get(pk=pk)      
        except Patient.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk):
        data=self.get_object(pk)
        data1=data.family_members.all()
        serializer = FamilyMemberSerializer(data1, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, pk):
        data=self.get_object(pk)
        serializer = FamilyMemberSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(patient=data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

########Update Family Details#################
class UpdateFamilyMember(APIView):
    def get_object(self,pk):
        try:
            return FamilyModel.objects.get(pk=pk)      
        except FamilyModel.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk):
        data=self.get_object(pk)
        serializer = FamilyMemberSerializer(data)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, pk):
        data=self.get_object(pk)
        serializer = FamilyMemberSerializer(data, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

########Retrieve Family Details#################
class RetriveFamilyMember(APIView):
    def get_object(self,pk):
        try:
            return FamilyModel.objects.get(pk=pk)      
        except FamilyModel.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk):
        data=self.get_object(pk)
        serializer = FamilyMemberSerializer(data)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, pk):
        data=self.get_object(pk)
        serializer = FamilyMemberSerializer(data)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
        


#########################Medication##############################################################################
########List and Add Medication Details#################
class AddMedication(APIView):
    def get_object(self,pk):
        try:
            return Patient.objects.get(pk=pk)      
        except Patient.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk):
        data=self.get_object(pk)
        data1=data.medication.all()
        serializer = MedicationSerializer(data1, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, pk):
        data=self.get_object(pk)
        serializer = MedicationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(patient=data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

########Retrive Active Medication Details#################
class ActiveMedication(APIView):
    def get(self, request):
        medications = Medication.objects.filter(is_active=True)
        serializer = MedicationSerializer(medications, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

########Retrieve Medication Details#################
class RetrieveMedication(APIView):
    def get_object(self,pk):
        try:
            return Medication.objects.get(pk=pk)      
        except Medication.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk):
        data=self.get_object(pk)
        data1=data.medication.all()
        serializer = MedicationSerializer(data1, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def get(self, request, pk):
        data=self.get_object(pk)
        serializer = MedicationSerializer(data)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
########Change status active status to True/False Medication#################
class ChangeActiveStatusMedication(APIView):
    def get_object(self,pk):
        try:
            return Medication.objects.get(pk=pk)      
        except Medication.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk):
        data=self.get_object(pk)
        serializer = MedicationSerializer(data)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

    def patch(self, request, pk):
        data=self.get_object(pk)
        serializer = MedicationSerializer(data)
        medication = Medication.objects.filter(pk=pk).first()
        if medication:
            if medication.is_active:
                medication.is_active=False
            else:
                medication.is_active=True    
            medication.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)

####################Update Mediacation Details##################################
class UpdateMedication(APIView):
    def get_object(self,pk):
        try:
            return Medication.objects.get(pk=pk)      
        except Medication.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk):
        data=self.get_object(pk)
        serializer = MedicationSerializer(data)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request,pk):
        data=self.get_object(pk)
        serializer = MedicationSerializer(data, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
