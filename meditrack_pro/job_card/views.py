from rest_framework import generics, permissions
from rest_framework.response import Response
from .models import JobCard
from .serializers import JobCardSerializer
from .permissions import IsAdminOrReadOnly  # Importing the custom permission

class JobCardListCreateView(generics.ListCreateAPIView):
    """
    API view to retrieve a list of job cards or create a new job card.

    - GET: List all job cards.
    - POST: Create a new job card (authenticated users only).
    """
    queryset = JobCard.objects.all()
    serializer_class = JobCardSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        """
        Automatically set the 'reported_by' field to the current user's 
        username when creating a new job card.
        """
        serializer.save(reported_by=self.request.user.username)

class JobCardDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    API view to retrieve, update, or delete a specific job card.

    - GET: Retrieve a job card by its ID.
    - PUT/PATCH: Update an existing job card (admin only).
    - DELETE: Delete a job card (admin only).
    """
    queryset = JobCard.objects.all()
    serializer_class = JobCardSerializer
    permission_classes = [IsAdminOrReadOnly]

    def delete(self, request, *args, **kwargs):
        """
        Override the delete method to restrict deletion of job cards to 
        admin users only.
        """
        job_card = self.get_object()
        if request.user.is_staff:
            job_card.delete()
            return Response(status=204)
        return Response(status=403, data={"detail": "Not authorized to delete this job card."})
