from __future__ import unicode_literals
from django.db import models
import bcrypt

class UserManager(models.Manager):
    def register(self, reg_data):
        full_name = reg_data['full_name']
        username = reg_data['username']
        date_hired = reg_data['date_hired']
        password = reg_data['password']
        confirm_password = reg_data['confirm_password']
        hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
        try:
            user = self.get(username=username)
        except:
            user = False
        if len(full_name) >2 and date_hired and len(password) >7 and password == confirm_password and not user:
            u = self.create(full_name=full_name, username=username, date_hired=date_hired, password=hashed)
            print u
            print reg_data
            return (True,u)
        return (False,"Try again using at least 3 characters in name and username and double check your password matches and has 8 characters or more")

    def login(self, log_data):
        username = log_data['username']
        user = self.filter(username=username)
        password = log_data['password']
        if len(user) and bcrypt.hashpw(password.encode(), user[0].password.encode()) == user[0].password:
            return (True, user[0])
        return (False, 'Password or username are incorrect')



class User(models.Model):
    full_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    date_hired = models.DateField()
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
