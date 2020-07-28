from django.shortcuts import render
from .models import Jobs
from .forms import FindForm
from django.core.paginator import Paginator
# Create your views here.


def home_view(request):
    form = FindForm()
    return render(request, 'scrapping/home.html', {'form': form})


def list_view(request):
    form = FindForm()
    city = request.GET.get('city')
    language = request.GET.get('language')
    context = {'city': city, 'language': language, 'form': form}
    if city or language:
        _filter = {}
        if city:
            _filter['city__slug'] = city
        if language:
            _filter['language__slug'] = language
        qs = Jobs.objects.filter(** _filter)
        paginator = Paginator(qs, 10)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context['object_list'] = page_obj
    return render(request, 'scrapping/list.html', context)
