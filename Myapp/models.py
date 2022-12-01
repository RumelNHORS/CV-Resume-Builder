from django.db import models


class ResumeProfile(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.CharField(max_length=100)
    school = models.CharField(max_length=100)
    result = models.CharField(max_length=100)
    collage = models.CharField(max_length=100)
    degree = models.CharField(max_length=100)
    uni_versity = models.CharField(max_length=100, blank=True)
    skill = models.TextField(max_length=500)
    work_exprince = models.TextField(max_length=500)
    about_you = models.TextField(max_length=1000)

    def __str__(self):
        return self.name