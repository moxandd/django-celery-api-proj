from django.urls import path
from . import views

urlpatterns = [
    path('test/<int:newsletter_id>/', views.test_view, name='test-view'),
]