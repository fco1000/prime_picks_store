from django.shortcuts import render

def contactsView(request):
    return render(request, 'contact.html')