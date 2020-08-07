from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .models import UserModel, Component, Page, Website
from .serializers import UserSerializer, GroupSerializer, UserModelSerializer, ComponentModelSerializer, PageModelSerializer, WebsiteModelSerializer

class CustomViewSet(viewsets.ModelViewSet):
    queryset = Component.objects.all()

    def get_queryset(self):
        queryset = self.model.objects
        filters = dict(zip(self.request.GET.keys(), self.request.GET.values()))

        if(bool(filters)):
            queryset = queryset.filter(**filters)
        return queryset.all()

class ComponentViewSet(CustomViewSet):
    queryset = Component.objects.all()
    serializer_class = ComponentModelSerializer
    model = Component

class PageViewSet(CustomViewSet):
    queryset = Page.objects.all()
    serializer_class = PageModelSerializer
    model = Page

class WebsiteViewSet(CustomViewSet):
    queryset = Website.objects.all()
    serializer_class = WebsiteModelSerializer
    model = Website

class UserModelViewSet(CustomViewSet):
    serializer_class = UserModelSerializer
    queryset = UserModel.objects.all()
    model = UserModel

class UserViewSet(viewsets.ModelViewSet):
    #API endpoint that allows users to be viewed or edited.
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
    #API endpoint that allows groups to be viewed or edited.
    queryset = Group.objects.all()
    serializer_class = GroupSerializer