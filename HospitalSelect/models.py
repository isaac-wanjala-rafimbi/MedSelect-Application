from django.db import models

# Create your models here.
# models.py


class County(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Constituency(models.Model):
    name = models.CharField(max_length=255)
    county = models.ForeignKey(County, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Specialization(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Hospital(models.Model):
    name = models.CharField(max_length=255)
    county = models.ForeignKey(County, on_delete=models.CASCADE)
    constituency = models.ForeignKey(Constituency, on_delete=models.CASCADE)
    specializations = models.ManyToManyField(Specialization)
    photo = models.ImageField(upload_to='hospital_photos/', null=True, blank=True)
    nhif_coverage = models.BooleanField(default=False)
    contact_phone = models.CharField(max_length=15, null=True, blank=True)
    contact_email = models.EmailField(null=True, blank=True)
    country = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name
