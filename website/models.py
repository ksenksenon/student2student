from django.db import models

# Create your models here.

# Объявление
class Ad(models.Model):
    article = models.CharField(max_length=200)
    cost = models.IntegerField(default=0)
    description = models.CharField(max_length=2000)
    publisher = models.ForeignKey('User', on_delete=models.CASCADE)
    # 0 - нужна помощь, 1 - помогу
    ad_type = models.BooleanField(default=True)
    
    def __str__(self):
        return self.description

# Пользователь
class User(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    is_verified = models.BooleanField(default=False)
    rating = models.DecimalField(max_digits=3, decimal_places=2)
    balance = models.IntegerField(default=0)
    university_name = models.CharField(max_length=100)
    faculty_name = models.CharField(max_length=100)
    # 1 курс, 2 курс..., магистр, аспирант). Потом нужно сделать список доступных. Пока так
    degree = models.CharField(max_length=100)
    about = models.CharField(max_length=2000);
    
                                    