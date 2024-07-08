from django.shortcuts import render

from .models import ChaiVariety

from django.shortcuts import get_object_or_404

# Create your views here.
def all_chai(request):
    
    chais = ChaiVariety.objects.all();
    
    return render(request, 'page/index.html', {'chais': chais})  



def chai_detail(request, chai_id):
    
    chai = get_object_or_404(ChaiVariety, pk=chai_id)
    
    return render(request, 'page/chai_detail.html', {'chai': chai})


def chai_store_view(request):
    return render(request, 'page/chai_stores.html')
