from django import forms


class Register(forms.Form):
    user_name = forms.CharField(max_length=100,
                                 widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':
                                                               'User Name'}))

    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder':
                                                                 '***************'}))

    repeat_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder':
                                                                        '**************'}))

    email_address = forms.CharField(max_length=100,
                                    widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':
                                                                  'Email Address'}))


class Login(forms.Form):
    email_address = forms.CharField(max_length=100,
                                    widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':
                                                                  'Email'}))
    password = forms.CharField(max_length=100,
                               widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder':
                                                                 'Password'}))
    remember = forms.BooleanField(required=False)


class Post(forms.Form):
    text = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'post_body'}))
