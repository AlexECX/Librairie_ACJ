from django.contrib import admin

from .models import Book, Author, Genre
# from .models import Book_Author

# Register your models here.



# Admin modification for ManyToMany fields
# class BookAuthorsInline(admin.TabularInline):
#     model = Book.authors.through

# class BookGenresInline(admin.TabularInline):
#     model = Book.genres.through

# class BookAdmin(admin.ModelAdmin):
#     list_display = ('title', 'pub_date')
#     #filter_horizontal = ("authors",)
#     search_fields = ('title'),
#     fields = ('title', 'pub_date', 'synopsis',)
#     # inlines = (BookAuthorsInline, BookGenresInline)
#     # exclude = ('authors','genres')

class BookAdmin(admin.ModelAdmin):
    filter_horizontal = ("authors", "genres")

admin.site.register(Author)
#admin.site.register(Book_Author)
admin.site.register(Genre)
admin.site.register(Book, BookAdmin)

