import re
import traceback
from ast import Delete
from turtle import home
from unicodedata import name

from django.http import HttpResponse
from django.shortcuts import redirect, render

from .models import Book

# Create your views here.


def homepage(request):
    # return HttpResponse('<img src="media/Downloads/Sign1.jpg" width="500" height="600">')
    print(request.method)
    # print(request.GET)
    print(request.POST)
    if request.method == "POST":
        if not request.POST.get("bid"):
            try:
                book_name = request.POST["bname"]
                book_price = request.POST["bprice"]           #####fetch data from .html file and display O/P in terminal
                book_qty = request.POST["bqty"]
                # print(book_name,type(book_price),book_qty)           #####type is str
                Book.objects.create(name = book_name ,price = book_price,quantity = book_qty)
                return redirect("homepage")
            except ValueError as msg:    
                print("Please Enter Data /Insufficient data")
                return redirect("homepage")    
        else:
            
            bid = request.POST.get("bid")
            book_obj = Book.objects.get(id=bid)  
            book_obj.name =  request.POST["bname"]        ######Edit wala code
            book_obj.price = request.POST["bprice"] 
            book_obj.quantity = request.POST["bqty"]
            book_obj.save()
            return redirect("show_all_books")
            


    elif request.method == "GET":    
        return render(request,template_name="home.html")
    pass


def show_all_books(request):
    all_books = Book.objects.all()
    data = {"books": all_books}
    return render(request,"show_books.html", context =data )


def edit_data(request,id):
    book = Book.objects.get(id = id)
    data = {"single_book": book}
    return render(request, template_name="home.html" ,context=data)    


def delete_data(request,id):
    print(request.method)
    if request.method == "POST":
        try:
            book = Book.objects.get(id=id)
        except Book.DoesNotExist as er_msg:
            # print(er_msg)
            print(traceback.print_exc())
        else:
            book.delete()
        return redirect("show_all_books")
    else:
        return HttpResponse(f"Request Method: {request.method} not allowed....!! Only POST method alllowed")    

    




