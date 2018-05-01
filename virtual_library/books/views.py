from django.shortcuts import render, redirect


from books.models import Book, Author, Genre
# from books.models import Book_Author
# Create your views here.


def search(request, keyword:str=None):

    if keyword == None:
        try:
            keyword=request.POST['research']
            return redirect("books:search", keyword)
            #search(keyword)
        except (KeyError):
            context = { 'error_message': "Error in the search" }
            return render(request, 'books/search_result.html', context)
    else:
        keyword = keyword.replace("%20", " ")
        books_and_authors = []
        books = []
        authors = []

        #The keyword is a name of an author
        books_by_author = Book.objects.filter(authors__name__icontains=keyword)
        if books_by_author:
            for b1 in books_by_author:
                books.append((b1.id, b1.title))

        #The keyword is a title of a book
        books_by_title = Book.objects.filter(title__icontains=keyword)
        if books_by_title:
            for b2 in books_by_title:
                books.append((b2.id, b2.title))

        #The keyword is a genre
        books_by_genre = Book.objects.filter(genres__name__icontains=keyword)
        if books_by_genre:
            for b3 in books_by_genre:
                books.append((b3.id, b3.title))

        #Getting the authors of the books
        if books:
            for b in books:
                authors = []
                authors_of_book_queryset = Author.objects.filter(book__title=b[1])
                if authors_of_book_queryset:
                    for a1 in authors_of_book_queryset:
                        authors.append(a1.name)
                    books_and_authors.append((b[0], b[1], authors))

        context = {
            'books_and_authors': books_and_authors,
            'keyword': keyword
            }

        return render(request, 'books/search_result.html', context)

def get_info(request, book_id):

    authors_of_book = []
    genres_of_book = []

    book_to_display = Book.objects.get(id=book_id)

    authors_of_book_queryset = Author.objects.filter(book__title=book_to_display.title)
    authors_of_book = list(authors_of_book_queryset)

    genre_of_book_queryset = Genre.objects.filter(book__title=book_to_display.title)
    genres_of_book = list(genre_of_book_queryset)

    context = {
        'book_to_display': book_to_display,
        'authors_of_book': authors_of_book,
        'genres_of_book': genres_of_book,
    }
    return render(request, 'books/book_info.html', context)