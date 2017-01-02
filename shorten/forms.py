from django import forms
from .models import *
# class register(forms.Form):
#     username = models.CharField(max_length = 30,blank = True  ,null  = True)
#     password = models.CharField(max_length = 30,blank = True  ,null  = True)
#     password2 = models.CharField(max_length = 30,blank = True  ,null  = True)
#     email    = models.EmailField()


class login_form(forms.Form):
    username = forms.CharField(label = "Username")
    password = forms.CharField(label = "Password" , widget=forms.PasswordInput)







class register(forms.ModelForm):
    """
    Form for registering a new account.
    """
    password = forms.CharField(label = "Password" , widget=forms.PasswordInput)
    password1 = forms.CharField(label="Password (again)",widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password','password1',"email"]

    def clean(self):
        """
        Verifies that the values entered into the password fields match
        NOTE: Errors here will appear in ``non_field_errors()`` because it applies to more than one field.
        """
        print("this function been called")
        cleaned_data = super(register, self).clean()
        if 'password' in self.cleaned_data and 'password1' in self.cleaned_data:
            if self.cleaned_data['password'] != self.cleaned_data['password1']:
                print("the password not the same")
                # raise forms.ValidationError(['Invalid value'])
                self.add_error('password1',"Password does not match")
        return self.cleaned_data

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user


class inserturl(forms.ModelForm):
    def __init__(self, *args, **kwargs):
         self.user = kwargs.pop('user',None)
         super(inserturl, self).__init__(*args, **kwargs)
    class Meta:
        model  = URL
        fields = ["url","short"]
    def clean(self):
        """
        Verifies that the values entered into the password fields match
        NOTE: Errors here will appear in ``non_field_errors()`` because it applies to more than one field.
        """
        print("In model, the user that curently add url is ",self.user)
        print("this function been called")
        cleaned_data = super(inserturl, self).clean()
        url = URL.objects.filter(user = self.user, short = self.cleaned_data["short"])
        print("url",url)
        if url:
            self.add_error('short',"already have same shorten in url")
    def save(self, commit=True):
        print("trying to save")
        url = super(inserturl, self).save(commit=False)
        if commit:
            print("saved")
            url.save()
        return url
