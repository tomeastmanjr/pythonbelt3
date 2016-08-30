from __future__ import unicode_literals
from django.db import models
import bcrypt

class UserManager(models.Manager):
    def register(self, reg_data):
        errors = []
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
        if user:
            errors.append("Email already exists. Please enter a different email")
        if not len(full_name) >2:
            errors.append("Please enter a valid name at least 3 characters")
        if not len(username) >2:
            errors.append("Please enter a valid username at least 3 characters")
        if not len(password)>7:
            errors.append("Please enter a valid password at least 8 characters")
        if not password == confirm_password:
            errors.append("Make sure password and confirm password are matching")
        if not date_hired:
            errors.append("Please enter a hired date")
        if errors:
            return (False, errors)
        else:
            u = self.create(full_name=full_name, username=username, date_hired=date_hired, password=hashed)
            print u
            print reg_data
            return (True,u)

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
