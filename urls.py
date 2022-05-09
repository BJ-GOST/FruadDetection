from django.urls import path
from . import views

urlpatterns = [
path('', views.api_overview, name='api-overview'),
path('fraud-list', views.fraud_detector, name='detect-fraud'),
path('check-fraud', views.check_fraud, name='check-fraud')
]