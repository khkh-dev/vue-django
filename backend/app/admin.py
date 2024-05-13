from django.contrib import admin

# Register your models here.
from .models import User, UserToken, Note


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "first_name",
        "last_name",
        "email",
        "username",
        "image",
    ]


@admin.register(UserToken)
class UserTokenAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "user_id",
        "token",
        "created_at",
        "expired_at",
    ]


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "title",
        "text",
        "created_at",
        "updated_at",
        "user",
    ]
