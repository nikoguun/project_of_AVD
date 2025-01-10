from django.urls import include, path

urlpatterns = [
    path('analyzer/', include('data_analyzer.urls')),
]
