from django.db import models


class Document(models.Model):
    name=models.CharField(max_length=50)
    file = models.FileField(upload_to='files/')

    def __str__(self):
        return self.name