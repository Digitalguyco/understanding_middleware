from django.http  import HttpResponse

# Create your views here.

def home(request):
    user_ip = request.META.get('HTTP_X_FORWARDED_FOR') # Shows the IP Address of the user

    return HttpResponse(f'This Now Your New IP Address: {user_ip}')

