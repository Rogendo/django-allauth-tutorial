from django.shortcuts import render
from django.views.generic import TemplateView


class Home(TemplateView):
    template_name = 'home.html'

# def Home(request):
#     return render(request, 'config/home.html')