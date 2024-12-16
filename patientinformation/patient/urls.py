from django.urls import path
from . import views

urlpatterns=[
    path('patient/',views.ListAndAddPatient.as_view(),name="list_patient"),
    path('patient/update/<int:pk>/',views.UpdatePatient.as_view(), name="add_patient"),
    path('patient/retrieve/<int:pk>/',views.RetrievePatient.as_view(), name="retrieve_patient"),
    path('family/<int:pk>/',views.ListAndAddFamilyMembers.as_view(),name="list_family"),
    path('family/update/<int:pk>/',views.UpdateFamilyMember.as_view(), name="update_family"),
    path('family/retrieve/<int:pk>/',views.RetriveFamilyMember.as_view(), name="retrieve_family"),
    path('medication/add/<int:pk>/', views.AddMedication.as_view(), name='add_medication'),
    path('medication/active/', views.ActiveMedication.as_view(), name='list_active_medications'),
    path('medication/retrieve/<int:pk>/', views.RetrieveMedication.as_view(), name='retrieve_medication'),
    path('medication/change/status/<int:pk>/', views.ChangeActiveStatusMedication.as_view(), name='toggle_medication_status'),
    path('medication/update/<int:pk>/', views.UpdateMedication.as_view(), name='update_medication'),
]

