from django import forms


class SearchForm(forms.Form):
    first_name=forms.CharField(label="First_name",widget=forms.TextInput(attrs={'placeholder': 'Name'}))
    last_name=forms.CharField(label="Last_name",widget=forms.TextInput(attrs={'placeholder': 'Fater name'}))
    username=forms.CharField(label="User_name",widget=forms.TextInput(attrs={'placeholder': 'zain1'}))
    email=forms.EmailField(label="Email",widget=forms.TextInput(attrs={'placeholder': 'zain@gmail.com'}))
    password1=forms.IntegerField(label="Passward",widget=forms.TextInput(attrs={'placeholder': '12345678'}))
    password2=forms.IntegerField(label="Confrem Passward",widget=forms.TextInput(attrs={'placeholder': '12345678'}))


class DataStore(forms.Form):
    username=forms.CharField(label="User_name",widget=forms.TextInput(attrs={'placeholder': 'zain1'}))
    password=forms.IntegerField(label="Passward",widget=forms.TextInput(attrs={'placeholder': '12345678'}))

