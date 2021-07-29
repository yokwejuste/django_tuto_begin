import datetime
from django.shortcuts import render

# For a simple view, we use


def index(request):
    today = datetime.date.today()
    return render(request, "index.html")


