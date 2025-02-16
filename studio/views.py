from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.core.paginator import Paginator
from .forms import ContactForm
from .models import YogaClass

# Yoga Detail View
def yoga_detail(request, pk):
    yoga_class = get_object_or_404(YogaClass, pk=pk)  # Fetch the yoga class by primary key or return 404
    return render(request, 'yoga_detail.html', {'yoga_class': yoga_class})

# Yoga List View with Pagination
def yoga(request):
    yoga_classes = YogaClass.objects.all()  # Fetch all yoga classes from the database
    paginator = Paginator(yoga_classes, 5)  # Show 5 classes per page
    page_number = request.GET.get('page')  # Get the current page number from the URL query string
    page_obj = paginator.get_page(page_number)  # Get the corresponding page object
    return render(request, 'yoga.html', {'page_obj': page_obj})

# Homepage View
def index(request):
    return render(request, 'index.html')  # Render index.html template

# Contact Form View
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Process the form data (e.g., send an email or log it)
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            # For now, just print the data to the console (you can replace this with email sending logic)
            print(f"Name: {name}, Email: {email}, Message: {message}")

            # Redirect to a success page
            return redirect('success')
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})

# Success Page View
def success(request):
    return HttpResponse('Thank you for your message!')
