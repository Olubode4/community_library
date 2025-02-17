from django.contrib import admin

# Register your models here.
from catalog.models import Author, Genre, Book, BookInstance, Language


class BooksInline(admin.TabularInline):
    model = Book


class AuthorAdmin(admin.ModelAdmin):
    list_display = ("last_name", "first_name", "date_of_birth", "date_of_death")
    fields = ["first_name", "last_name", ("date_of_birth", "date_of_death")]
    inlines = [BooksInline]


class BooksInstanceInline(admin.TabularInline):
    model = BookInstance


# Register the Admin classes for Book using the decorator
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "display_genre")

    inlines = [BooksInstanceInline]


# Register the Admin classes for BookInstance using the decorator
@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ("book", "status", "borrower", "due_back", "id")
    list_filter = ("status", "due_back")
    fieldsets = (
        (None, {"fields": ("book", "borrower", "imprint", "id")}),
        ("Availability", {"fields": ("status", "due_back")}),
    )


admin.site.register(Author, AuthorAdmin)
admin.site.register(Genre)
admin.site.register(Language)
