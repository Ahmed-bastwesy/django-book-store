from multiprocessing import context
import os
from django.shortcuts import get_object_or_404, redirect, render

from books.forms import CreateAuthorForm, CreateBookForm, EditBookForm
from .models import Book ,Author
from django.http import HttpResponse




def index (request):
    context={
        "books":Book.objects.all()
    }
    return render (request,"books/index.html",context=context)

def bookDetails (request , bookId):
    book = get_object_or_404(Book , id = bookId)
    image=  os.path.basename(book.image.__str__())
    context={
        "book" : book,
        "image" :image
    }
    return render (request,"books/bookDetails.html",context=context)

def authorDetails (request , authorId):
    author = get_object_or_404(Author , id = authorId)
    book = Book.objects.filter(Author_id = authorId).all()
    number_of_books=len(book)
    context={
        "books" : book,
        "author" : author,
        "number_of_books":number_of_books
    }
    return render (request,"books/authorDetails.html",context=context)

def createBook (request):
    if request.method == "POST":
        form = CreateBookForm(request.POST , request.FILES)
        if form.is_valid():
            name=form.cleaned_data['name']
            publish_date=form.cleaned_data['publish_date']
            add_to_site=form.cleaned_data['add_to_site']
            author=form.cleaned_data['author']
            price=form.cleaned_data['price']
            appropriate=form.cleaned_data['appropriate']
            # image=form.cleaned_data['image']
            book=Book.objects.create(name=name, publish_date=publish_date, add_to_site=add_to_site, Author=author,price=price, appropriate=appropriate )
            # book=form.save()
            return redirect("books")
    else:
     form = CreateBookForm(request.POST)
    return render(request,"books/createBook.html",context={"form":form})

def createAuthor (request):
    if request.method == "POST":
        forms = CreateAuthorForm (request.POST)
        if forms.is_valid():
            name=forms.cleaned_data['name']
            author=Author.objects.create(name=name)
            return redirect("books")
    else:
     forms = CreateAuthorForm()
    return render(request,"books/createAuthor.html",context={"forms":forms})

def removeBook(request,book_id):
    book = Book.objects.filter(id = book_id).delete()
    return redirect("books")

def editBook (request,book_id):
    book= get_object_or_404(Book, id=book_id)
    if request.method == "POST":
        form = EditBookForm(request.POST , instance=book)
        if form.is_valid():
            book=form.save()
            return redirect('book_list' , bookId=book.id)
    else:
     form = EditBookForm(instance=book)
    return render(request,"books/createBook.html",context={"form":form})






