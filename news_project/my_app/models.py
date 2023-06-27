from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator
from datetime import datetime
# Create your models here.

class CustomUser(AbstractUser):
    personal_id = models.CharField(unique=True, max_length=155, null=True, blank=True)
    age = models.IntegerField(null=True, blank=True, validators=[MinValueValidator(5), MaxValueValidator(140)])
    city = models.CharField(null=True, blank=True, max_length=155)
    USER_CHOICES = [
        ('basic_user', 'Basic'),
        ('reporter', 'Reporter'),
        ('editor', 'Editor'),
        ('staff', 'Staff'),
        ('super_admin', 'Super Admin')
    ]

    user_type = models.CharField(max_length=20, choices=USER_CHOICES, null=True, blank=True)

    groups = models.ManyToManyField(
        'auth.Group',
        blank=True,
        related_name='person_set',
        related_query_name='person',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        blank=True,
        related_name='person_set',
        related_query_name='person',
    )

class Post(models.Model):
    title = models.CharField(max_length=155)
    body = models.TextField(max_length=9999)
    writer = models
    CATEGORY_CHOICES = [
        ("news", "חדשות"),
        ("sport", "ספורט"),
        ("television", "טלויזיה"),
        ("economy", "כלכלה"),
        ("health", "בריאות"),
        ("worldwide", "עולם"),
        ("fasion", "אופנה"),
        ("digital", "דיגיטל"),
        
        
    ]
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    post_date_time = models.DateTimeField(auto_now_add=True, editable=False)
    writer = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title[0:12]} | {self.category}"