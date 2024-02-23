from .models import Food
from django.shortcuts import render
from django.views.generic import ListView


# Create your views here.
# def home_movies(request):
#     context = {}
#     movies_list = Food.objects.all()
#     context['movies_list'] = movies_list
#     context['categories'] =
#     return render(request, "home_movies.html", context)
class Homepage(ListView):
    template_name = 'homepage.html'
    model = Food
