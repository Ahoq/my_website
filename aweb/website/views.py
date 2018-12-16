from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from website.forms import ContactForm


def email(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ['ahoq@student.sjcny.edu'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('thanks')
    return render(request, "website/email.html/", {'form': form})

def thanks(request):

    return HttpResponse(request,'website/index.html')

def home(request):

	return render(request, 'website/index.html')

def about(request):

	return render(request, 'website/about.html')




##f1f7c8: body
##50991d: header, thumbnail
##eddfb6: header a link













