from django.urls import path
from .views import FlowerAPIView

urlpatterns = [
    path('', FlowerAPIView.as_view())
]
