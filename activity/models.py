from django.db import models

class Employee(models.Model):
    emp_id              = models.CharField(max_length=31, unique=True)
    real_name           = models.CharField(max_length=61)
    active              = models.BooleanField(default=True)
    created_at          = models.DateTimeField(auto_now_add=True)
    updated_at          = models.DateTimeField(auto_now=True)
    
    class Meta:
        indexes         = [
            models.Index(fields=('emp_id',)),
        ]   
        ordering        = ('emp_id',)

    def __str__(self):
        return '%s(%s)' % (self.real_name, self.emp_id)

class EmployeeActivity(models.Model):
    employee            = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='employee')
    tz                  = models.CharField(max_length=61)
    start_time          = models.DateTimeField()
    end_time            = models.DateTimeField()
    created_at          = models.DateTimeField(auto_now_add=True)
    updated_at          = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = (('employee','start_time','end_time'),)
        indexes         = [
            models.Index(fields=('employee','start_time','end_time')),    
        ]
