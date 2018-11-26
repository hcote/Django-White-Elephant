from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

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

class Group(models.Model):
    owner = models.ForeignKey(User, related_name='group_owner', on_delete=models.CASCADE)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    max_num = models.IntegerField()
    members = models.ManyToManyField(User, related_name='members', blank=True)
