from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):

    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")

        # Normalize the email address
        email = self.normalize_email(email)

        # Create a new user model instance
        user = self.model(email=email, **extra_fields)

        # Set the password if provided
        user.set_password(password)

        # Save the user to the database
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        # Ensure is_superuser and is_staff are True for superuser
        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        # Create a new superuser
        return self.create_user(email, password, **extra_fields)