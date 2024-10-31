from django.db import models



LEVELS = (
    ('Basic','Basic'),
    ('Intermediate','Intermediate'),
    ('Experienced', 'Experienced'),
)


class Frontend(models.Model):
    name = models.CharField(max_length=20)
    level = models.CharField(max_length=30, choices=LEVELS, null=True)

    def __str__(self):
        return self.name

class Backend(models.Model):
    name = models.CharField(max_length=50)
    level = models.CharField(max_length=30, choices=LEVELS, null=True)

    def __str__(self):
        return self.name

class Project(models.Model):
    name = models.CharField(max_length=20, null=True)
    image = models.ImageField(upload_to='media', null=True)
    git_repo = models.CharField(max_length=200,null=True)
    live_demo = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name

