from django.shortcuts import render, redirect
from .forms import SlaveForm
from .models import Slave
from django.core.paginator import Paginator

def add_slave(request):
    if request.method == 'POST':  
        form = SlaveForm(request.POST, request.FILES)  
        if form.is_valid():
            form.save()  
            return redirect('slave_list')  
    else:  
        form = SlaveForm()
    return render(request, 'add_slave.html', {'form': form})


def slave_list(request):
    # Get all slaves from the database, ordered by newest first
    slaves = Slave.objects.all().order_by('-created_at')  
    
    # Paginate the list (10 slaves per page)
    paginator = Paginator(slaves, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    print(page_obj[0].photo, page_obj[1].photo)
    return render(request, 'slave_list.html', {'page_obj': page_obj})

