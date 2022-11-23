from django.contrib.auth.base_user import  BaseUserManager

class  UserManager(BaseUserManager):

    #we want to use this during migrations so make it true
    use_in_migrations = True  

    #write  a method to create user
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Email is required..")

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    # write a method to create superuser  
    def create_superuser(self, email, password, **extra_fields):
        #set the fields for super user 
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(('super user must have is staf true'))

        return self.create_user(email, password, **extra_fields)

         