from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.apps import apps
from django.shortcuts import get_object_or_404
from .models import Customer
# Create your views here.

# TODO: Create a function for each path created in customers/urls.py. Each will need a template as well.


def index(request):
    # The following line will get the logged-in in user (if there is one) within any view function
    all_customers = Customer.objects.all()
    user = request.user()
    context = {
        'all_customers': all_customers
    }

    try:
        # This line inside the 'try' will return the customer record of the logged-in user if one exists
        logged_in_customer = Customer.objects.get(user=user)
    except:
        # TODO: Redirect the user to a 'create' function to finish the registration process if no customer record found
        
        return HttpResponseRedirect(reverse('customers:index.html', context))
    # It will be necessary while creating a Customer/Employee to assign request.user as the user foreign key
def create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        street_address = request.POST.get('street_address')
        postal_code = request.POST.get('postal_code')
        weekly_pickup = request.POST.get('weekly_pickup')
        one_time_pickup = request.POST.get('one_time_pickup')
        suspend_start = request.POST.get('suspend_start')
        suspend_end = request.POST.get('suspend_end')
        new_customers = Customer(name=name,  street_address=street_address, postal_code=postal_code, weekly_pickup=weekly_pickup, one_time_pickup=one_time_pickup, suspend_start=suspend_start, suspend_end=suspend_end)
        new_customers.save()
        return HttpResponseRedirect(reverse('customers:index'))
    else:
        # print(user)
        return render(request, 'customers/index.html')
        