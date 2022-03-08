from django.db import models
import re

class UserManager(models.Manager):
    def create_validator(self, reqPost, reqFILES):
        errors = {}
        if len(reqPost['first_name']) < 2:
            errors['first_name'] = "First name must be at least 3 characters"
        if len(reqPost['last_name']) < 2:
            errors['last_name'] = "Last name must be at least 3 characters"
        if len(reqFILES) == 0:
            errors['profile_pic'] = "Please upload a profile picture"
        if len(reqPost['city']) < 2:
            errors['city'] = "City name must be at least 3 characters"
        if len(reqPost['states']) < 1:
            errors['states'] = "Please choose a state"
        if len(reqPost['email']) < 6:
            errors['email'] = "Email must be at least 7 characters"
        # if len(reqPost['bio']) < 10:
        #     errors['bio'] = "Bio must be at least 10 characters"
        if len(reqPost['password']) < 8:
            errors['password'] = "Password must be at least 9 characters"
        if reqPost['password'] != reqPost['password_conf']:
            errors['match'] = "Passwords do no match"
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(reqPost['email']):
            errors['regex'] = "Email is in wrong format"
        users_with_email = User.objects.filter(email=reqPost['email'])
        if len(users_with_email) >= 1:
            errors['dep']: "Email taken, please create another one"
        return errors
    def create_validator_update(self, reqPost, reqFILES):
        errors = {}
        if len(reqPost['first_name']) < 2:
            errors['first_name'] = "First name must be at least 3 characters"
        if len(reqPost['last_name']) < 2:
            errors['last_name'] = "Last name must be at least 3 characters"
        if len(reqPost['city']) < 2:
            errors['city'] = "City name must be at least 3 characters"
        if len(reqPost['states']) < 1:
            errors['states'] = "Please choose a state"
        if len(reqPost['email']) < 6:
            errors['email'] = "Email must be at least 7 characters"
        if len(reqPost['password']) < 8:
            errors['password'] = "Password must be at least 9 characters"
        if reqPost['password'] != reqPost['password_conf']:
            errors['match'] = "Passwords do no match"
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(reqPost['email']):
            errors['regex'] = "Email is in wrong format"
        users_with_email = User.objects.filter(email=reqPost['email'])
        if len(users_with_email) >= 1:
            errors['dep']: "Email taken, please create another one"
        return errors
    def create_validator_update_two(self, reqPost, reqFILES):
        errors = {}
        if len(reqPost['bio']) < 10:
            errors['bio'] = "Bio name must be at least 10 characters"
        return errors

class PortfolioManager(models.Manager):
    def portfolio_validator(self, reqPost):
        errors = {}
        if len(reqPost['title']) < 2:
            errors['title'] = "Title must be at least 3 characters"
        if not isinstance(reqPOST['price'], float):
            errors['price'] = "Please use digits and decimals only."
        elif (reqPOST['price']).find(".")>0:
            if len((reqPOST['price']).split(".")[1])!=2:
                errors['price'] = "There should be two digits to the right of the decimal."
        return errors


class User(models.Model):
    first_name = models.TextField()
    last_name = models.TextField()
    profile_pic = models.ImageField(null=True, blank=True, upload_to="images/")
    city = models.TextField()
    state = models.CharField(max_length=2)
    email = models.EmailField()
    bio = models.TextField(default='Please update your bio!')
    website = models.TextField(blank = True, null=True)
    password = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

class Portfolio(models.Model):
    title = models.CharField(max_length=55)
    price = models.DecimalField(decimal_places=2, max_digits=5)
    portfolio_image = models.ImageField(null=True, blank=True, upload_to="images/")
    content_creator = models.ForeignKey(User, related_name="user_portfolio", on_delete = models.CASCADE)
    portfolio_item = models.ManyToManyField(User, related_name="all_portfolio_items")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = PortfolioManager()

class Order(models.Model):
    quantity_ordered = models.IntegerField(default=0)
    total_price = models.DecimalField(decimal_places=2, max_digits=6)
    portfolio_order = models.ForeignKey(Portfolio, related_name="item_of_portfolio", on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Cart(models.Model):
    user = models.ForeignKey(User, default=None, blank=True, null=True, related_name="carts", on_delete=models.CASCADE)
    total_price = models.DecimalField(decimal_places=2, max_digits=6)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, related_name="items_in_cart", on_delete = models.CASCADE)
    item = models.ForeignKey(Portfolio, related_name="cart_items", on_delete = models.CASCADE)
    quantity = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Media(models.Model):
    facebook = models.TextField(default="N/A")
    linkedin = models.TextField(default="N/A")
    instagram = models.TextField(default="N/A")
    twitter = models.TextField(default="N/A")
    user_media = models.ForeignKey(User, related_name="user_social_media", on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)