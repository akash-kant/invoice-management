from django.urls import path, include
from . import views
from .views import InvoiceAPIView

urlpatterns = [
    path('', include('rest_framework.urls', namespace='rest_framework')),
    path('invoices/', InvoiceAPIView.as_view(), name='invoices'),
]