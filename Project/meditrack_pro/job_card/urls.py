from django.urls import path
from .views import JobCardListCreateView, JobCardDetailView

urlpatterns = [
    path('job-cards/', JobCardListCreateView.as_view(), name='job-card-list-create'),
    path('job-cards/<int:pk>/', JobCardDetailView.as_view(), name='job-card-detail'),
]
