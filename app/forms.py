from django import forms

gender=(('male','male'),('female','female'))
lang=(('english','english'),('tamil','tamil'),('telugu','telugu'))

class Employee(forms.Form):
    name=forms.CharField(max_length=50)
    number=forms.IntegerField(required=False)
    email=forms.EmailField()
    password=forms.CharField(max_length=10,widget=forms.PasswordInput)
    address=forms.CharField(max_length=200,widget=forms.Textarea(attrs={'cols':30,'rows':3}))
    gender=forms.ChoiceField(choices=gender,widget=forms.RadioSelect)
    language=forms.MultipleChoiceField(choices=lang,widget=forms.CheckboxSelectMultiple)
    #time=forms.TimeField()
    #data=forms.DateField()
    #datatime=forms.DateTimeField()