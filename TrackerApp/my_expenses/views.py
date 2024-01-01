from django.shortcuts import render

# Create your views here.
def homepage(request):
    return str("Homepage")


def download_csv(request):
    return "Download csv"