from django.db import models
import json
from django.contrib.auth import get_user_model
User = get_user_model()
import datetime

# Create your models here.
class Categories(models.Model):
    name = models.CharField(max_length=100, default='')
    body = models.TextField(blank=True)
    # making it so category names in backend UI aren't the default 'Categories Object (2)'
    def __str__(self):
        return self.name
    # adding this so in the backend there are no double plurals
    class Meta:
        verbose_name_plural = 'Categories'

class Group(models.Model):
    name = models.CharField(max_length=100, default='')
    description = models.TextField(blank=True)
    owner = models.ForeignKey(User, related_name='group_owner', on_delete=models.CASCADE, null=True, blank=True)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    price_range = models.IntegerField(blank=True, default='')
    max_members = models.IntegerField(blank=True)
    start_date = models.DateField(auto_now=False, auto_now_add=False, blank=False)
    months = models.IntegerField(blank=True)
    members = models.ManyToManyField(User, related_name='members', blank=True)
    member_ids = models.CharField(max_length=5, default='', blank='')
    def __str__(self):
        return self.name

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=50, default='')
    address_two = models.CharField(max_length=10, default='', blank=True)
    city = models.CharField(max_length=50, default='')
    state = models.CharField(max_length=2, default='')
    zipcode = models.CharField(max_length=5, default='')
    
    # groups = models.ManyToManyField(Group, related_name='groups_a_part_of', blank=True)
    # within these groups they have ID's of user they are sending gifts to