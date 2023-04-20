from django.shortcuts import render


def Authors(request):
    authors = ['William Shakespeare', 'JKRowling',
               'AgathaCristie', 'Nagib Mahfouz']
    context = {
        "list": authors
    }
    return render(request, "authors.html", context)


def view_author(request, name):
    context = {"author_name": name}
    return render(request,"author.html",context)

def view_harrypotter(request):
    return render(request,"harryPotter.html")