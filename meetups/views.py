from django.shortcuts import render, redirect

from .models import Meetup, Participant
from .forms import RegistrationForm


# Create your views here.

def index(request):
    # meetups = [
    #     {'title': 'A First Meetup', 'location':'Pakistan', 'slug':'a-first-meetup'},
    #     {'title': 'A Second Meetup', 'location':'Kashmir', 'slug':'a-second-meetup'}
    # ]
    meetups = Meetup.objects.all()  # fetch all instances of Meetup in database

    return render(request, 'meetups/index.html', {
        'meetups': meetups
    })

# # Older approach (before admin)
# def meetup_details(request, meetup_slug):
#     print(meetup_slug)
#     selected_meetup = {
#         'title': 'A first Meetup',
#         'description': 'This is the first meetup!'
#     }

#     return render(request, 'meetups/meetup-details.html', {
#         'meetup_title': selected_meetup['title'],
#         'meetup_description': selected_meetup['description']
#     })

def meetup_details(request, meetup_slug):

    try:
        selected_meetup = Meetup.objects.get(slug=meetup_slug)  # get used to get one specific instance only
        if(request.method == 'GET'):
            registration_form = RegistrationForm()
        else:
            registration_form = RegistrationForm(request.POST)
            if registration_form.is_valid():
                # participant =  registration_form.save() #due to save(), if we use same email with another meeting, we will get error
                userEmail = registration_form.cleaned_data['email']
                participant, was_created = Participant.objects.get_or_create(email=userEmail) #if email is not already created then create one
                selected_meetup.participants.add(participant)
                return redirect('confirm-registration', meetup_slug=meetup_slug) # return after saving data to database, pass the name of path in redirect()

        return render(request, 'meetups/meetup-details.html', {
            'meetup_found': True,
            'meetup': selected_meetup,
            'form': registration_form
            })

    except Exception as exc:
        return render(request, 'meetups/meetup-details.html', {
            'meetup_found': False       
        })
    

def confirmRegistration(request, meetup_slug):
    meetup = Meetup.objects.get(slug=meetup_slug)
    return render(request, 'meetups/registration-successful.html', {
        'organizer_email': meetup.organizer_email
    })
