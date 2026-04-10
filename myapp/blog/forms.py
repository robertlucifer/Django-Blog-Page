from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
class Contactform(forms.Form):
    name = forms.CharField(label="Name", max_length=100)
    email = forms.EmailField(label="Email")
    message = forms.CharField(label="Message")
    
    
class Registerform(forms.ModelForm):
    username = forms.CharField(label="Username",max_length=100, required=True)
    email = forms.CharField(label="Email",max_length=100, required=True)
    password = forms.CharField(label="Password",max_length=100, required=True)
    password_confirm = forms.CharField(label="Confirm Password",max_length=100, required=True)
    
    class Meta:
        model = User
        fields = ['username','email','password']
    
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password") 
        password_confirm = cleaned_data.get("password_confirm")
        
        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError("Passwords do not match")
        
class Loginform(forms.Form):
    username = forms.CharField(label="Username", max_length=100, required=True)
    password = forms.CharField(label="Password",max_length=100, required=True)
    
    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')
        
        if username and password:
            self.user_cache = authenticate(username = username, password = password)
            if self.user_cache is None:
                raise forms.ValidationError("Invalid User name and password")
            
        return cleaned_data
    
class Forgotpassword(forms.Form):
    email = forms.CharField(label="Email",max_length=100, required=True)
    
    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        self.user_cache = User.objects.filter(email=email).first()
        if not self.user_cache:
            raise forms.ValidationError("Email Does not exist")
        
        return cleaned_data
    
class Resetpassword(forms.Form):
    new_password = forms.CharField(label="new_password", max_length=100, required=False)
    confirm_password = forms.CharField(label="new_password", max_length=100, required=False)
    
    def clean(self):
        cleaned_data = super().clean()
        new_password = cleaned_data.get("new_password") 
        confirm_password = cleaned_data.get("confirm_password")
    
        if new_password and confirm_password and new_password != confirm_password:
            raise forms.ValidationError("Passwords do not match")