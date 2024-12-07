from django import forms
from .models import Train

class TrainForm(forms.ModelForm):
    class Meta:
        model = Train
        fields = ['train_name', 'source', 'destination', 'total_seats']  # Include total_seats
        widgets = {
            'train_name': forms.TextInput(attrs={'class': 'form-control'}),
            'source': forms.TextInput(attrs={'class': 'form-control'}),
            'destination': forms.TextInput(attrs={'class': 'form-control'}),
            'total_seats': forms.NumberInput(attrs={'class': 'form-control'})  # Widget for total_seats
        }


from django import forms
from .models import Train

class SeatBookingForm(forms.Form):
    source = forms.CharField(max_length=255)
    destination = forms.CharField(max_length=255)
    num_seats = forms.IntegerField(min_value=1)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['source'].widget.attrs.update({'placeholder': 'Enter source station'})
        self.fields['destination'].widget.attrs.update({'placeholder': 'Enter destination station'})
        self.fields['num_seats'].widget.attrs.update({'placeholder': 'Number of seats'})

# from django import forms

# class BookingForm(forms.Form):
#     source = forms.CharField(max_length=255)
#     destination = forms.CharField(max_length=255)
#     num_seats = forms.IntegerField(min_value=1)
