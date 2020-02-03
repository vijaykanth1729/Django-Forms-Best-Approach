from django import forms
from .models import Contact

#using formhelpers and layouts for OurForum class..
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout,Submit,Row,Column


class ContactForm(forms.ModelForm):
    choice_list = (('m', 'Male'),
                   ('f', 'Female'),
                   )
    INTEGER_CHOICES = [tuple([x, x]) for x in range(1, 32)]
    gender = forms.ChoiceField(label='Please provide your Gender', widget=forms.RadioSelect, choices=choice_list)
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Enter email id'}))
    gender1 = forms.MultipleChoiceField(required=True, label='Check this Gender Field',
                                        widget=forms.CheckboxSelectMultiple, choices=choice_list)
    #age = forms.CharField(label='Please provide your age', widget=forms.Select(choices=INTEGER_CHOICES))
    #start_date = forms.DateField(widget=forms.SelectDateWidget())
    class Meta:
        model = Contact
        fields = ['name','email','phone_number','message']

    # clean_<field_name>

    def clean_name(self, *args, **kwargs):
        name = self.cleaned_data.get('name')
        if not 'ajay' in name:
            raise forms.ValidationError("Please provide the name as only ajay")
        return name


class OurForum(forms.Form):
    STATES = (
        ('','Choose...'),
        ('ap', 'AndhraPradesh'),
        ('ts', 'Telangana'),
        ('ks', 'Karntaka'),
        ('tn', 'TamilNadu'),
    )
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder':'Email'}))
    password = forms.CharField(widget=forms.PasswordInput, max_length=20, min_length=8)
    address_1 = forms.CharField(label='Address', widget=forms.TextInput(attrs={'placeholder':'1234 Main St'}))
    address_2 = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Apartment, studio, or floor'}))
    city = forms.CharField()
    state = forms.ChoiceField(choices=STATES)
    zip_code = forms.CharField(label='Zip')
    check_me_out = forms.BooleanField(required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('email', css_class='form-group col-md-6 mb-0'),
                Column('password', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            'address_1',
            'address_2',
            Row(
                Column('city', css_class='form-group col-md-6 mb-0'),
                Column('state', css_class='form-group col-md-4 mb-0'),
                Column('zip_code',css_class='form-group col-md-2 mb-0'),
                css_class='form-row'
            ),
            'check_me_out',
            Submit('submit','Send Us',css_class='btn btn-info btn-lg btn-block')

        )
