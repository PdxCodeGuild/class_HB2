from webbrowser import get
from django.shortcuts import render
from .forms import ShortenForm
from .models import Shorten
import random
import string

# Create your views here.
def short_url(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def shortening(request):    
    if request.method == 'POST':        
        form = ShortenForm(request.POST, request.FILES)
        if form.is_valid():
            url = form['webpage'].value()
            form.save() 
            return render(request, 'lab_02/result.html', {'form':form})

    else:
        shorty = short_url()
        form = ShortenForm(initial={'shorty':shorty})       
                  
    context = {
        'form':form,
    }

    return render(request, 'lab_02/entry.html', context)

