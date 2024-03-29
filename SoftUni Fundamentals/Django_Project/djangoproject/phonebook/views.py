from django.shortcuts import render, redirect
from djangoproject.phonebook.models import Contact


def create_contact(request):
    name = request.POST.get('name')
    number = request.POST.get('number')
    contact = Contact(
        name=name,
        number=number,
    )
    contact.save()
    return redirect('landing-page')


def landing_page(request):
    contact = Contact.objects.all()
    context = {'contacts': contact}
    return render(request, 'phonebook/index.html', context)
