
from django.shortcuts import render
from django.http import HttpResponse
from Base_App.models import BookTable, AboutUs, ItemList, Items, Feedback

# Create your views here.

def HomeView(request):
    items = Items.objects.all()
    list_items = ItemList.objects.all()
    reviews = Feedback.objects.all()
    return render(request, 'home.html', {'items': items, 'list': list_items, 'review': reviews})

def AboutView(request):
    data = AboutUs.objects.all()
    return render(request, 'about.html', {'data': data})

def MenuView(request):
    items = Items.objects.all()
    list_items = ItemList.objects.all()
    return render(request, 'menu.html', {'items': items, 'list': list_items})
 
def BookTableView(request):
    if request.method == 'POST':
        name = request.POST.get('user_name')
        phone_number = request.POST.get('phone_number')
        email = request.POST.get('user_email')
        total_person = request.POST.get('total_person')
        booking_date = request.POST.get('booking_date')

        # Validate inputs
        if (
            name and 
            len(phone_number) == 10 and 
            email and 
            total_person.isdigit() and 
            int(total_person) > 0 and 
            booking_date
        ):
            data = BookTable(
                Name=name,
                Phone_number=phone_number,
                Email=email,
                Total_person=int(total_person),
                Booking_date=booking_date
            )
            data.save()
    
    return render(request, 'book_table.html')

def FeedbackView(request):
    return render(request, 'feedback.html')
