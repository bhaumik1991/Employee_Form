from django.db import models


class Employee(models.Model):
    full_name = models.CharField(max_length=20)
    email = models.EmailField(max_length=20)
    image = models.ImageField(upload_to='media/profile/')
    gender = models.CharField(max_length=10,)
    status = models.CharField(max_length=6)

    def __str__(self):
        return self.full_name

    def delete(self, *args, **kwargs):
        self.image.delete()
        super().delete(*args, **kwargs)

