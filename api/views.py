from django.shortcuts import render
from rest_framework import generics
from rest_framework.mixins import CreateModelMixin, ListModelMixin
from rest_framework import viewsets
from core.models import Client, Newsletter, Message
from .serializers import ClientSerializer, NewsletterSerializer, MessageSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

# Create your views here.

############# ------------------------------ Router Viewsets ------------------------------  #############

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    filterset_fields = ('mobile_code',)
    search_fields = ('mobile_code',)

class NewsletterViewSet(viewsets.ModelViewSet):
    queryset = Newsletter.objects.all()
    serializer_class = NewsletterSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    filterset_fields = ('id',)
    search_fields = ('id',)

class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    filterset_fields = ('id', 'newsletter_id')
    search_fields = ('id', 'newsletter_id')

############# ------------------------------ Client Views ------------------------------  #############

class ClientsListCreateAPIView(generics.ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class ClientDetailAPIView(generics.RetrieveAPIView):
    lookup_field = "id"
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class ClientUpdateAPIView(generics.UpdateAPIView):
    lookup_field = "id"
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class ClientDeleteAPIView(generics.DestroyAPIView):
    lookup_field = "id"
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

############# ------------------------------ Newsletter Views ------------------------------  #############

class NewslettersListCreateAPIView(generics.ListCreateAPIView):
    queryset = Newsletter.objects.all()
    serializer_class = NewsletterSerializer

class NewslettersDetailAPIView(generics.RetrieveAPIView):
    lookup_field = "id"
    queryset = Newsletter.objects.all()
    serializer_class = NewsletterSerializer

class NewslettersUpdateAPIView(generics.UpdateAPIView):
    lookup_field = "id"
    queryset = Newsletter.objects.all()
    serializer_class = NewsletterSerializer

class NewslettersDeleteAPIView(generics.DestroyAPIView):
    lookup_field = "id"
    queryset = Newsletter.objects.all()
    serializer_class = NewsletterSerializer


############# ------------------------------ Message Views ------------------------------  #############
class MessagesListAPIView(generics.ListAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer