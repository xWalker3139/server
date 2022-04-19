from django.contrib import admin
from .models import Post, Customer, Comment

admin.site.register(Post)
admin.site.register(Customer)
admin.site.register(Comment)

# Register your models here.
