from django.contrib import admin

# Register your models here.

from .models import User,Listings



# Register your models here.

class ListingAdmin(admin.ModelAdmin):
    list_display = ("id" , "category",  "item_name", "price")



admin.site.register(User)
# admin.site.register(Comments)
admin.site.register(Listings, ListingAdmin)
# admin.site.register(Bids)