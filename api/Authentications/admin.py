from django.contrib import admin
from .models import CustomUser  # Import your model

class YourModelAdmin(admin.ModelAdmin):
    # Define the fields you want to display in the admin list view
    list_display = ('email', 'username',)

    # Add any filters you want to use in the admin list view
    list_filter = ('email', 'username',)

    # Add search fields for quick searching in the admin
    search_fields = ('email', 'username',)

    # Add any additional configurations or customizations as needed

# Register your model with the admin site
admin.site.register(CustomUser, YourModelAdmin)
