from django import forms
class SearchForm(forms.Form):
    first_name=forms.CharField(initial="text")
    last_name=forms.CharField(initial="text")
    username=forms.CharField(initial="text")
    email=forms.EmailField(initial="----@gmail.com")
    password1=forms.IntegerField()
    password2=forms.IntegerField()

    

   
      



    def clean_Rollno(self,*args,**kwargs):
        Rollno=self.cleaned_data.get("Rollno")
        if Rollno<10:
            raise forms.ValidationError("Roll no must be greater then 10")
        return Rollno

    def clean_Name(self,*args,**kwargs):
        Name=self.cleaned_data.get("Name")
        if len(Name)<6:
            raise forms.ValidationError("inshure that name must be contain atleast 5 charector")
        return Name