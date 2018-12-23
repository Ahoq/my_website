from django import forms

class ContactForm(forms.Form):

    from_email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'class' : 'email'}))
    subject = forms.CharField(required=True,widget=forms.TextInput(attrs={'class' : 'subject'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class' : 'message'}))
    name = forms.CharField(required=False,widget=forms.TextInput(attrs={'class' : 'subject'}))
