from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'application': 'Shop All Day',
        'name': 'Kayla Agrata Budiawan',
        'class': 'PBP C'
    }

    return render(request, "main.html", context)
