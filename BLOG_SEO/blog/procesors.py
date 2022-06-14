from home.models import Home

#process to get the phone number and email
def home_contact(request):
    home = Home.objects.latest('created')
    return {
        'phone':home.phone,
        'correo':home.contact_email 
    }