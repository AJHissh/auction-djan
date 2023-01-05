from django.contrib import admin

# Register your models here.

from .models import User,Listings



# Register your models here.

class ListingAdmin(admin.ModelAdmin):
    list_display = ("id" , "category",  "item_name", "price", "image")
    
class UserAdmin(admin.ModelAdmin):
    list_display = ("id" , "username", "email", "first_name", "last_name", "last_login", "is_active")


admin.site.register(User, UserAdmin)
# admin.site.register(Comments)
admin.site.register(Listings, ListingAdmin)
# admin.site.register(Bids)