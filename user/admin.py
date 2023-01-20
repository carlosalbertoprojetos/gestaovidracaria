from django.contrib import admin

from .models import User


# class ContactAdmin(admin.TabularInline):
#     model = Contact
#     extra = 0


# class SocialMediaAdmin(admin.TabularInline):
#     model = SocialMedia
#     extra = 0


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'option', 'is_active', 'last_login')
    # inlines = [
    #     ContactAdmin,
    #     SocialMediaAdmin,
    # ]
    readonly_fields = ('last_login',)
    fields = ['option', ('email', 'is_active')]
