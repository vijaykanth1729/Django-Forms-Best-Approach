from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Book, Forum
from .forms import ContactForm, OurForum


@login_required(login_url='/accounts/login/')
def books_list(request):
    books = Book.objects.all()
    context = {
        'all_books':books
    }
    return render(request, 'books/list.html', context)


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('books:list')
    else:
        form = ContactForm()
    return render(request, 'books/contact.html', {'form':form})


def our_forum(request):
    if request.method == 'POST':
        form = OurForum(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password =  form.cleaned_data['password']
            address_1 = form.cleaned_data['address_1']
            address_2 = form.cleaned_data['address_2']
            city = form.cleaned_data['city']
            state = form.cleaned_data['state']
            zip = form.cleaned_data['zip_code']
            check_me_out = form.cleaned_data['check_me_out']
            data = Forum(email = email, password=password,
                         address_1=address_1, address_2=address_2,
                         city=city,state=state, zip=zip, check_me_out=check_me_out)
            data.save()
            return HttpResponse("<h2>Thanks for submitting</h2>")
    else:
        form = OurForum()
    return render(request, 'books/our_forum.html', {'form':form})

