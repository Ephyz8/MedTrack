from django.urls import path
from .views import JobCardListCreateView, JobCardRetrieveUpdateDeleteView

urlpatterns = [
    path('', JobCardListCreateView.as_view(), name='job_card_list_create'),
    path('<int:pk>/', JobCardRetrieveUpdateDeleteView.as_view(), name='job_card_detail'),
]
