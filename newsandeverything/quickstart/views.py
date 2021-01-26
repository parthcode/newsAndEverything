from django.shortcuts import render

# Create your views here.
from quickstart.models import NewsDetails
from rest_framework import viewsets
from rest_framework import permissions

from quickstart.serializers import NewsSerializer


class NewsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = NewsDetails.objects.all()
    serializer_class = NewsSerializer
    # permission_classes = [permissions.IsAuthenticated]


# class GroupViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows groups to be viewed or edited.
#     """
#     queryset = Group.objects.all()
#     serializer_class = GroupSerializer
#     # permission_classes = [permissions.IsAuthenticated]