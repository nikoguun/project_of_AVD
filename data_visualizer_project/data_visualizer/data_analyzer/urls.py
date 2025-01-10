from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.upload_csv, name='upload_csv'),
    
   path('visualize/', views.visualize_data, name='visualize_data'),
    path('display/', views.display_csv, name='display_csv'),  # Page d'affichage
   
]
