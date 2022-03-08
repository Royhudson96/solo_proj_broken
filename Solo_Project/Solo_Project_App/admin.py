from django.contrib import admin
from .models import *


admin.site.register(User)


admin.site.register(Portfolio)


admin.site.register(Order)


admin.site.register(Cart)

admin.site.register(CartItem)