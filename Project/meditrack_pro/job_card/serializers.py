from rest_framework import serializers
from .models import JobCard

class JobCardSerializer(serializers.ModelSerializer):
    """
    Serializer for the JobCard model, converting it to and from JSON format.
    """

    class Meta:
        model = JobCard
        fields = '__all__'
