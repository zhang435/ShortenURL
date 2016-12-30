from django import forms
from .models import *
# class register(forms.Form):
#     username = models.CharField(max_length = 30,blank = True  ,null  = True)
#     password = models.CharField(max_length = 30,blank = True  ,null  = True)
#     password2 = models.CharField(max_length = 30,blank = True  ,null  = True)
#     email    = models.EmailField()

class register(forms.ModelForm):
    """
    Form for registering a new account.
    """
    password1 = forms.CharField(label="Password (again)")

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
                print("the passis not the same")
                # raise forms.ValidationError(['Invalid value'])
                self.add_error('password1',"incorect password")
        return self.cleaned_data

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user


class inserturl(forms.ModelForm):
    class Meta:
        model  = URL
        fields = ["url","short"]
