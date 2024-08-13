from rest_framework import serializers
from .models import JobCard

class JobCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobCard
        fields = '__all__'
