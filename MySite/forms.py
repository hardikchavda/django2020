from django import forms
from MySite.models import Stud_info

city_data = [
    ('rkt', 'Rajkot'),
    ('amd', 'Ahmedabad'),
    ('sur', 'Surat'),
    ]


class FormName(forms.Form):
    s_name = forms.CharField(
        label="Full Name", max_length=10, required=True, initial="H1233")
    s_pwd = forms.CharField(label="Password", max_length=10, required=True)
    s_age = forms.IntegerField(label="Age", required=True)
    s_address = forms.CharField(
        label="Address", max_length=255, required=False, widget=forms.Textarea)
    s_email = forms.EmailField(label="Email", required=True)
    s_birthdate = forms.DateField(
        label="BirthDate", required=False, widget=forms.SelectDateWidget())
    s_city = forms.ChoiceField(label="City", choices=city_data, required=False)
    s_rmb = forms.BooleanField(
        label="Remember Me", required=True, initial=False)


class NewStudent(forms.ModelForm):

    # s_name = models.CharField(max_length=264,unique=True, verbose_name="Name")
    # s_age = models.IntegerField(default=18,null=False,verbose_name="Age")
    # s_city = models.CharField(default="Rajkot",choices=city_data,max_length=50,verbose_name="City")
    # s_address=models.CharField(max_length=500,verbose_name="Address")
    # s_phone = models.IntegerField(blank=True,null=True,verbose_name="Phone Number")

    class Meta:
        model = Stud_info
        #fields = {"s_name"}
        labels = {
            "s_name":"Student Name",
            "s_age":"Min Age",
        }
        error_messages={
            "s_name": {
                "required":"This field is required for data",
                "max-length":"this title is too long",
            },
        }
        fields = '__all__'
        # exclude = ["s_phone"]


