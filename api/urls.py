from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r"clients", views.ClientViewSet)
router.register(r"newsletters", views.NewsletterViewSet)
router.register(r"messages", views.MessageViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('clients/', views.ClientsListCreateAPIView.as_view(), name='clients'),
    path('clients/<str:id>/', views.ClientDetailAPIView.as_view(), name='client-details'),
    path('clients/<str:id>/update/', views.ClientUpdateAPIView.as_view(), name='client-update'),
    path('clients/<str:id>/delete/', views.ClientDeleteAPIView.as_view(), name='client-delete'),
    path('newsletters/', views.NewslettersListCreateAPIView.as_view(), name='newsletters'),
    path('newsletters/<str:id>/', views.NewslettersDetailAPIView.as_view(), name='newsletter-details'),
    path('newsletters/<str:id>/update', views.NewslettersUpdateAPIView.as_view(), name='newsletter-update'),
    path('newsletters/<str:id>/delete', views.NewslettersDeleteAPIView.as_view(), name='newsletter-delete'),
    path('messages/', views.MessagesListAPIView.as_view(), name='messages'),
]