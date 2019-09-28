from django.shortcuts import render
from vdata.models import Videogame
#pagination
from django.core.paginator import Paginator

# Create your views here.
def vdata_view(request):
    vdata_list = Videogame.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(vdata_list, 1000)
    try:
        vdata = paginator.page(page)
    except PageNotAnInteger:
        vdata = paginator.page(1)
    except EmptyPage:
        vdata = paginator.page(paginator.num_pages)

    return render(request, 'vdata/vdata.html', context={'vdata':vdata})