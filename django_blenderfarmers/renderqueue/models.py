from django.db import models

# Create your models here.
class Job(models.Model):
    file_name = models.CharField('file name', max_length=255)
    created_on = models.DateTimeField('date uploaded')

    def __unicode__(self):
        return self.file_name

class Frame(models.Model):
    job = models.ForeignKey(Job)
    file_name = models.CharField('filename of frame', max_length=255)

    def __unicode__(self):
        return self.file_name
        
class Machine(models.Model):
    name = models.CharField('name of machine', max_length=255)
    os = models.CharField('operating system', max_length=255)
    os_version = models.CharField('operating system version', max_length=255)
    
    def __unicode__(self):
        return self.name
