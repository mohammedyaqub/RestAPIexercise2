from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework import permissions
from post.app1.serializers import UserSerializer
from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from rest_framework import authentication, permissions
from rest_framework.views import APIView


#to get all  users as list or GET


class ListUsers(APIView):
    """
    View to list all users in the system.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAdminUser]
#list == array
    def get(self, request, format=None):
        # list of all users, by list comprehension 
        usernames = [user.username for user in User.objects.all()]
        return Response(usernames)
