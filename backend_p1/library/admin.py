from django.contrib import admin
from .models import Author, Book, BookInstance, Genre, Language

# Register your models here.
"""
admin.site.register(Book)
admin.site.register(Author)
admin.site.register(BookInstance)
"""
admin.site.register(Genre)
admin.site.register(Language)

# admin.site.register(Author, AuthorAdmin)       or    this lower on to register your model


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'd_birth', 'd_dead')
    fields = ['first_name', 'last_name', ('d_birth', 'd_dead')]


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')


@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_filter = ('status', 'due_back')
    list_display = ('book', 'status', 'due_back', 'id')
