from multiprocessing import context
from django.shortcuts import render, redirect
from .forms import VenueForm
from .models import VenueListing

def AddVenue(request):
    form = VenueForm()
    template_name = 'filehandeling/form.html'
    if request.method == "POST":
        form = VenueForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('show_venueurl')
    context = {'form':form}
    return render(request, template_name, context)

def ShowVenue(request):
    obj = VenueListing.objects.all()
    template_name = 'filehandeling/table.html'
    context={'obj':obj}
    return render(request, template_name, context)

def DelView(request,id):
    obj = VenueListing.objects.get(id=id)
    template_name= 'filehandeling/confirm.html'
    context ={"obj":obj}
    if request.method == 'POST':
        obj.delete()
        return redirect('show_venueurl')
    return render(request, template_name, context)
# Create your views here.
