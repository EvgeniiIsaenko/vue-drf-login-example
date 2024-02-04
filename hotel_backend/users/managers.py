from django.contrib.auth.base_user import BaseUserManager

# custom manager which uses email instead of a username
class CustomUserManager(BaseUserManager):
    # custom user creator
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("No email")
        
        user = self.model(
            email = self.normalize_email(email),
            **extra_fields
        )
        user.set_password(password)
        user.save()

        return user

    # custom superuser creator
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("is_staff attribute is 'False'")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("is_superuser attribute is 'False'")
        
        return self.create_user(email, password, **extra_fields)
