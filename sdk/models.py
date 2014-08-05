from django.db import models

# Create your models here.
class LogParser(models.Model):
    keywords = models.CharField(max_length = 30)
    filepath = models.FileField(upload_to = './upload/')

    def __unicode__(self):
        return '<{0} {1}>'.format(self.keywords, self.filepath)