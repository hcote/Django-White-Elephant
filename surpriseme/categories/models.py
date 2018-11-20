from django.db import models

# Create your models here.
class Categories(models.Model):
    name = models.CharField(max_length=100, default='')
    body = models.TextField(blank=True)
    # making it so category names in backend UI aren't the default 'Categories Object (2)
    def __str__(self):
        return self.name
    # adding this so in the backend there are no double plurals
    class Meta:
        verbose_name_plural = 'Categories'