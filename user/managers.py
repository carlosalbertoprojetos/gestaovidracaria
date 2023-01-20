from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import UserManager


class DefaultUserManager(UserManager):

    def create_user(self, email, option, password=None, is_staff=False, is_superuser=False, is_active=True):
    
        user_obj = self.model(
            email=self.normalize_email(email),
        )
        user_obj.set_password(password)
        user_obj.username = email
        user_obj.option = option
        user_obj.is_active = is_active
        user_obj.is_staff = is_staff
        user_obj.is_superuser = is_superuser
        user_obj.save(using=self._db)
        return user_obj

    def create_superuser(self, email, password=None):
        user = self.create_user(
            email=email,
            password=password,
            option='0',
            is_staff=True,
            is_superuser=True
        )
        return user
