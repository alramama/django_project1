from django.db import models

class FilesAdmin(models.Model):
    adminulodw = models.FileField(upload_to='media')
    title = models.CharField(max_length=220)
    def __str__(self):
        return self.title