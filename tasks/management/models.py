from django.db import models

# Create your models here.
class Task(models.Model):

  PENDING = 'PE'
  IN_PROGRESS = 'IP'
  DONE = 'DO'
  statusOptions = [(PENDING, 'Pending'), (IN_PROGRESS, 'In progress'), (DONE,'Done')]

  id = models.AutoField(primary_key=True, unique=True)
  name = models.CharField(db_column='task_name', max_length=100)
  description = models.TextField(db_column='task_desc', null=True)
  deadline = models.DateTimeField(db_column='task_deadline')
  status = models.CharField(db_column='task_status', choices = statusOptions, max_length=2, default=PENDING)

  class Meta:
    db_table = 'tasks'
    ordering = ['-deadline']