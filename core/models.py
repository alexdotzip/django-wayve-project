from django.db import models

# Create your models here.
class OrgId(models.Model):
    name = models.CharField(max_length = 20)
    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length = 100)

    def __str__(self):
        return self.name

class Journal(models.Model):
    title = models.CharField(max_length = 100)
    orgid = models.ForeignKey(OrgId, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return self.title
