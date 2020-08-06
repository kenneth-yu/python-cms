from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .models import UserModel, Component, Page, Website
from .serializers import UserSerializer, GroupSerializer, UserModelSerializer, ComponentModelSerializer, PageModelSerializer, WebsiteModelSerializer

class ComponentViewSet(viewsets.ModelViewSet):
    queryset = Component.objects.all()
    serializer_class = ComponentModelSerializer

class PageViewSet(viewsets.ModelViewSet):
    queryset = Page.objects.all()
    serializer_class = PageModelSerializer

class WebsiteViewSet(viewsets.ModelViewSet):
    queryset = Website.objects.all()
    serializer_class = WebsiteModelSerializer

class UserModelViewSet(viewsets.ModelViewSet):
    serializer_class = UserModelSerializer
    queryset = UserModel.objects.all()

    def get_queryset(self):
        username = self.request.query_params.get('username')
        queryset = UserModel.objects
        if(username):
            queryset = queryset.filter(username=username)

        return queryset.all()
        

class UserViewSet(viewsets.ModelViewSet):
    #API endpoint that allows users to be viewed or edited.
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    #API endpoint that allows groups to be viewed or edited.
    queryset = Group.objects.all()
    serializer_class = GroupSerializer