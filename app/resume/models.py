from django.db import models

# Create your models here.
class Job(models.Model):
    title = models.CharField(max_length=255, unique=False)
    company = models.CharField(max_length=255, unique=False)
    start = models.DateField()
    current = models.BooleanField(default=True)
    end = models.DateField()
    slug = models.SlugField(max_length=255, unique=True)

    def __str__(self):
        return self.slug

class Duty(models.Model):
    duty = models.CharField(max_length=255, unique=False)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=255, unique=True)
    weight = models.IntegerField(default=0, unique=False)
    
    def __str__(self):
        return self.duty

class SubDuty(models.Model):
    subduty = models.CharField(max_length=255, unique=False)
    duty = models.ForeignKey(Duty, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=255, unique=True)
    weight = models.IntegerField(default=0, unique=False)
    
    def __str__(self):
        return self.subduty

class Technology(models.Model):
    tech = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True)
    weight = models.IntegerField(default=0, unique=False)
    
    def __str__(self):
        return self.tech

class TechBullet(models.Model):
    bullet = models.CharField(max_length=255, unique=False)
    tech = models.ForeignKey(Technology, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=255, unique=True)
    weight = models.IntegerField(default=0, unique=False)

    def __str__(self):
        return self.bullet
        
class Link(models.Model):
    link = models.CharField(max_length=255, unique=True)
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True)
    weight = models.IntegerField(default=0, unique=False)

    def __str__(self):
        return self.name

class Certifications(models.Model):
    cert = models.CharField(max_length=255, unique=True)
    link = models.CharField(max_length=255, unique=True)
    badge = models.ImageField(upload_to="images/", default="images/480px-No_image_available.svg.png")
    slug = models.SlugField(max_length=255, unique=True)
    
    def __str__(self):
        return self.cert