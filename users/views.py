from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import logout

def logoutView(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))