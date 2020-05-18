from django.shortcuts import render, redirect
from .forms import BookForm
from .models import Book

# Create your views here.
def booklist_list(request):
    context = {'booklist_list' : Book.objects.all()}
    return render(request,"booklist_register/booklist_list.html", context)

def booklist_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = BookForm()
        else:
            booklist = Book.objects.get(pk=id)
            form = BookForm(instance = booklist)
        return render(request,"booklist_register/booklist_form.html",{'form':form})
    else:
        if id == 0:
            form = BookForm(request.POST)
        else:
            booklist = Book.objects.get(pk=id)
            form = BookForm(request.POST, instance= booklist)
        if form.is_valid():
            form.save()
        return redirect('/booklist/list')

def booklist_delete(request,id):
    booklist = Book.objects.get(pk=id)
    booklist.delete()
    return redirect('/booklist/list')  