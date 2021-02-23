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
    # list of columns to display
    list_display = ('last_name', 'first_name', 'd_birth', 'd_dead')
    # list inside a () is displayed in singel row, flex-row
    fields = ['first_name', 'last_name', ('d_birth', 'd_dead')]


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')


@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    # adding filter panel
    list_filter = ('status', 'due_back')
    # column list to display
    list_display = ('book', 'status', 'due_back', 'id')

    # grouping in seperate container
    fieldsets = (
        (None, {
            "fields": (
                'book', 'id',
            )
        }),
        ('Avaliability', {
            "fields": (
                'status', 'due_back'
            )
        }),
    )
