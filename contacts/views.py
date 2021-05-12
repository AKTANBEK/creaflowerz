from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import generics
from .models import Contact
from .serializers import ContactSerializer


class ContactAPIView(generics.RetrieveAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


# class ContactViewSet(viewsets.ModelViewSet):
#     queryset = Contact.objects.all()
#     serializer_class = ContactSerializer
#     # http_method_names = ['get']