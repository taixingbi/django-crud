from django.shortcuts import render, redirect, HttpResponse

from .models import BookList
from django.http import JsonResponse

from django.core import serializers
from django.forms.models import model_to_dict
import json

import logging

logging.basicConfig( filename= 'test.log', level= logging.DEBUG )


# Create your views here.
def api_post(request):
    id=8
    book = BookList.objects.get(pk=id)
    book.title = 'test'
    book.price = 100
    book.author = 'hunter'
    book.save()

    books = BookList.objects.all()


    data = {
        'name': 'Vitor',
        'location': 'Finland',
        'is_active': True,
        'count': 28
    }
    
    logging.warn('------------test logging------------')

    return JsonResponse(data)

def api_get(request):
    return redirect('/')


def index(request):
    books = BookList.objects.all()

    print(   "---->", books.get( id=8 )	  )

    context = {
        'books': books
    }


    return render(request, 'index.html', context)

def create(request):
    print(request.POST)
    title = request.GET['title']
    price = request.GET['price']
    author = request.GET['author']
    book_details = BookList(title=title, price=price, author=author)
    book_details.save()
    return redirect('/')


def add_book(request):

    return render(request, 'add_book.html')



def delete(request, id):
    books = BookList.objects.get(pk=id)
    books.delete()
    return redirect('/')

def edit(request, id):
    books = BookList.objects.get(pk=id)
    context = {
        'books': books
    }
    return render(request, 'edit.html', context)


def update(request, id):
    books = BookList.objects.get(pk=id)
    books.title = request.GET['title']
    books.price = request.GET['price']
    books.author = request.GET['author']


    books.save()
    return redirect('/')

