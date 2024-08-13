from rest_framework import generics
from .models import JobCard
from .serializers import JobCardSerializer

class JobCardListCreateView(generics.ListCreateAPIView):
    queryset = JobCard.objects.all()
    serializer_class = JobCardSerializer

class JobCardRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = JobCard.objects.all()
    serializer_class = JobCardSerializer
