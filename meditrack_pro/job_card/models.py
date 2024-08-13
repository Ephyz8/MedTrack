from django.db import models

class JobCard(models.Model):
    job_number = models.IntegerField()
    request_number = models.IntegerField()
    reporting_date = models.DateField()
    department = models.CharField(max_length=255)
    ward = models.CharField(max_length=255)
    reported_by = models.CharField(max_length=255)
    equipment_name = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    brand = models.CharField(max_length=255)
    serial_number = models.CharField(max_length=255)
    fault_reported = models.TextField()
    diagnosis = models.TextField()
    action_done = models.TextField()
    required_spare_parts = models.TextField()

    def __str__(self):
        return f"JobCard {self.job_number} - {self.equipment_name}"
