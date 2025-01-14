from django.db import models

class JobCard(models.Model):
    """
    Model representing a job card for documenting repair or maintenance tasks 
    for medical equipment.
    """
    job_number = models.AutoField(primary_key=True, verbose_name="Job Number")
    request_number = models.PositiveIntegerField(verbose_name="Request Number", unique=True)
    reporting_date = models.DateField(verbose_name="Reporting Date")
    department = models.CharField(max_length=255, verbose_name="Department")
    ward = models.CharField(max_length=255, verbose_name="Ward")
    reported_by = models.CharField(max_length=255, verbose_name="Reported By")
    equipment_name = models.CharField(max_length=255, verbose_name="Equipment Name")
    model = models.CharField(max_length=255, verbose_name="Model")
    brand = models.CharField(max_length=255, verbose_name="Brand")
    serial_number = models.CharField(max_length=255, verbose_name="Serial Number")
    fault_reported = models.TextField(verbose_name="Fault Reported")
    diagnosis = models.TextField(verbose_name="Diagnosis")
    action_done = models.TextField(verbose_name="Action Done")
    required_spare_parts = models.TextField(verbose_name="Required Spare Parts")

    def __str__(self):
        """
        String representation of the JobCard model, showing the job number 
        and equipment name.
        """
        return f"JobCard {self.job_number} - {self.equipment_name}"

    class Meta:
        verbose_name = "Job Card"
        verbose_name_plural = "Job Cards"
        ordering = ['-reporting_date', 'job_number']
