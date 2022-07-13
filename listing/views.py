from django.shortcuts import render,redirect
from .models import Listing
from .forms import ListingForm

# Create your views here.

def listing_list(request):
    listings = Listing.objects.all()
    context = {
        "listings": listings 
    }
    return render(request, "listings.html", context)

def listing_retrieve(request, pk):
    
    listings = Listing.objects.get(id=pk)
    context = {
        "listings": listings
    }
    return render(request, "listing.html", context)

def listing_create(request):
    form = ListingForm()
    if request.method == "POST":
        form = ListingForm(request.POST,request.FILES)
        if form.is_valid:
            form.save()
            return redirect("/")
    
    context = {
        "form": form
    }
    return render(request, "listing_create.html", context)

def listing_update(request,pk):
    listings = Listing.objects.get(id=pk)
    form = ListingForm(instance=listings)
    if request.method == "POST":
        form = ListingForm(request.POST,instance=listings, files=request.FILES)
        if form.is_valid:
            form.save()
            return redirect("/")
    
    context = {
        "form": form
    }
    return render(request, "listing_update.html", context)

def listing_delete(request, pk):
    listing = Listing.objects.get(id=pk)
    listing.delete()
    return redirect("/")