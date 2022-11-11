from django.contrib import admin
from .models import Product, Brand, Category, Stock

# Register your models here.

admin.site.register(Product)
admin.site.register(Brand)
admin.site.register(Category)
admin.site.register(Stock)

# add admin panel title name
admin.site.site_header = "Inventory Management System"

# add admin panel dark theme
admin.site.enable_nav_sidebar = True

# add admin panel footer name
admin.site.site_title = "Inventory Management System"

# add admin panel footer url
admin.site.site_url = "https://www.linkedin.com/in/abu-bakkar-siddik-17b860196/"

# add admin panel footer text
admin.site.index_title = "Welcome to Inventory Management System"
