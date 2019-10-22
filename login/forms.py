from django import forms

# These will be greatly modified if not deleted
class LoginForm(forms.Form):
    user = forms.CharField(
        max_length=32,
        widget=forms.TextInput(attrs={
            "class": "login-input",
            "placeholder": "Username"
        })
    )
    password = forms.CharField(
        max_length=64,
        widget=forms.PasswordInput(attrs={
            "class": "login-input",
            "placeholder": "Password"
        })
    )