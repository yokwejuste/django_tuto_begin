import datetime
from django.shortcuts import render

# For a simple view, we use


def index(request):
    context = {'today': datetime.date.today(), 'year': datetime.date.year}
    return render(request, "index.html", context)
