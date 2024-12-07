# from django.shortcuts import render
# from django.http import HttpResponse
# from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from  django.core.mail import EmailMessage, send_mail
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes, force_str


# Create your views here.
def home(request):
    return render(request,'authentication/index.html')
def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        
        if User.objects.filter(username=username):
            messages.error(request, "Username already exist! Please try some other username.")
            return redirect('home')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email Already Registered!!")
            return redirect('home')
        
        if len(username)>20:
            messages.error(request, "Username must be under 20 charcters!!")
            return redirect('home')
        
        if pass1 != pass2:
            messages.error(request, "Passwords didn't matched!!")
            return redirect('home')
        
        if not username.isalnum():
            messages.error(request, "Username must be Alpha-Numeric!!")
            return redirect('home')
        
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        # myuser.is_active = False
        # myuser.is_active = False
        myuser.save()
        messages.success(request, "Your Account has been created succesfully!! Please check your email to confirm your email address in order to activate your account.")
        
        return redirect('signin')
        
        
    return render(request, "authentication/signup.html")
def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']
        
        user = authenticate(username=username, password=pass1)
        
        if user is not None:
            login(request, user)
            fname = user.first_name
            # messages.success(request, "Logged In Sucessfully!!")
            return render(request, "authentication/index.html",{"fname":fname})
        else:
            messages.error(request, "Bad Credentials!!")
            return redirect('home')
    
    return render(request, "authentication/signin.html")

def signout(request):
    logout(request)
    messages.success(request, "Logged Out Successfully!!")
    return redirect('home')

# add train
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import TrainForm


def add_train(request):
    if request.method == 'POST':
        form = TrainForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Train added successfully!")
            return redirect('add_train')  # Redirect back to the same page after successful submission
        else:
            messages.error(request, "Error adding train. Please try again.")
    else:
        form = TrainForm()
    return render(request, 'add_train.html', {'form': form})


# seat aavalibilty
# from django.shortcuts import render, redirect
# from django.contrib import messages
# from .models import Train, Booking
# from .forms import SeatBookingForm

# def book_seat(request):
#     if request.method == 'POST':
#         form = SeatBookingForm(request.POST)
#         if form.is_valid():
#             source = form.cleaned_data['source']
#             destination = form.cleaned_data['destination']
#             num_seats = form.cleaned_data['num_seats']

#             # Find the train that matches the source and destination
#             try:
#                 train = Train.objects.get(source=source, destination=destination)
#             except Train.DoesNotExist:
#                 messages.error(request, "No train found for this route.")
#                 return redirect('book_seat')

#             # Check if enough seats are available
#             if train.total_seats >= num_seats:
#                 # Update the train seat availability
#                 train.total_seats -= num_seats
#                 train.save()

#                 # Create a new booking entry
#                 booking = Booking(user=request.user, train=train, source=source, destination=destination, booked_seats=num_seats)
#                 booking.save()

#                 messages.success(request, f"Successfully booked {num_seats} seat(s) on {train.train_name}.")
#                 return redirect('book_seat')
#             else:
#                 messages.error(request, "Not enough seats available.")
#                 return redirect('book_seat')
#     else:
#         form = SeatBookingForm()

#     return render(request, 'bookseat.html', {'form': form})


from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Train, Booking
from .forms import SeatBookingForm

def book_seat(request):
    trains = None
    selected_train = None

    if request.method == 'POST':
        form = SeatBookingForm(request.POST)
        source = request.POST.get('source')
        destination = request.POST.get('destination')
        train_id = request.POST.get('train_id')
        num_seats = request.POST.get('num_seats')

        if source and destination and not train_id:
            # Fetch trains between source and destination
            trains = Train.objects.filter(source=source, destination=destination)
            if not trains.exists():
                messages.error(request, "No trains available for this route.")
        elif train_id and num_seats:
            try:
                selected_train = Train.objects.get(id=train_id)
            except Train.DoesNotExist:
                messages.error(request, "Selected train does not exist.")
                return redirect('book_seat')

            num_seats = int(num_seats)
            if selected_train.total_seats >= num_seats:
                # Proceed with booking
                selected_train.total_seats -= num_seats
                selected_train.save()

                booking = Booking(
                    user=request.user,
                    train=selected_train,
                    source=source,
                    destination=destination,
                    booked_seats=num_seats
                )
                booking.save()

                messages.success(request, f"Successfully booked {num_seats} seat(s) on {selected_train.train_name}.")
                return redirect('book_seat')
            else:
                messages.error(request, "Not enough seats available.")
        else:
            messages.error(request, "Please provide complete information.")
    else:
        form = SeatBookingForm()

    return render(request, 'bookseat.html', {'form': form, 'trains': trains, 'selected_train': selected_train})
