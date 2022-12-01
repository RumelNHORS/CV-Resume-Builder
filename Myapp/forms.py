from . models import ResumeProfile
from django import forms

class ProfileForm(forms.ModelForm):
    class Meta:
        model = ResumeProfile
        fields = ('name', 'phone', 'email', 'address', 'school', 'result', 'collage', 'degree', 'uni_versity', 'skill', 'work_exprince', 'about_you')

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['class'] = 'form-control'
        self.fields['phone'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['address'].widget.attrs['class'] = 'form-control'
        self.fields['school'].widget.attrs['class'] = 'form-control'
        self.fields['result'].widget.attrs['class'] = 'form-control'
        self.fields['collage'].widget.attrs['class'] = 'form-control'
        self.fields['degree'].widget.attrs['class'] = 'form-control'
        self.fields['uni_versity'].widget.attrs['class'] = 'form-control'
        self.fields['skill'].widget.attrs['class'] = 'form-control'
        self.fields['work_exprince'].widget.attrs['class'] = 'form-control'
        self.fields['about_you'].widget.attrs['class'] = 'form-control'
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'


"""        widgets = {
			'name': forms.CharField(attrs={'class': 'form-control'}),
            'phone': forms.CharField(attrs={'class': 'form-control'}),
            'email': forms.EmailField(attrs={'class': 'form-control'}),
            'address': forms.CharField(attrs={'class': 'form-control'}),
            'school': forms.CharField(attrs={'class': 'form-control'}),
            'result': forms.CharField(attrs={'class': 'form-control'}),
            'collage': forms.CharField(attrs={'class': 'form-control'}),
            'degree': forms.CharField(attrs={'class': 'form-control'}),
            'uni_versity': forms.CharField(attrs={'class': 'form-control'}),
            'skill': forms.TextInput(attrs={'class': 'form-control'}),
            'work_exprince': forms.Textarea(attrs={'class': 'form-control'}),
            'about_you': forms.Textarea(attrs={'class': 'form-control'}),
			
        }"""
"""
def __init__(self, *args, **kwargs):
    super(ProfileForm, self).__init__(*args, strip=True, **kwargs)
    self.fields['name'].widget.attrs['class'] = 'form-control'
    self.fields['phone'].widget.attrs['class'] = 'form-control'
    self.fields['email'].widget.attrs['class'] = 'form-control'
    self.fields['address'].widget.attrs['class'] = 'form-control'
    self.fields['school'].widget.attrs['class'] = 'form-control'
    self.fields['result'].widget.attrs['class'] = 'form-control'
    self.fields['collage'].widget.attrs['class'] = 'form-control'
    self.fields['degree'].widget.attrs['class'] = 'form-control'
    self.fields['uni_versity'].widget.attrs['class'] = 'form-control'
    self.fields['skill'].widget.attrs['class'] = 'form-control'
    self.fields['work_exprince'].widget.attrs['class'] = 'form-control'
    self.fields['about_you'].widget.attrs['class'] = 'form-control'
    for field in self.fields:
        self.fields[field].widget.attrs['class'] = 'form-control'
"""
"""
        def _init_(self, *args, **kwargs):
            super(ProfileForm, self)._init_(*args, **kwargs)
            self.fields['first_name'].widget.attrs['placeholder'] = 'Enter First Name'
            self.fields['last_name'].widget.attrs['placeholder'] = 'Enter last Name'
            self.fields['phone_number'].widget.attrs['placeholder'] = 'Enter Phone Number'
            self.fields['email'].widget.attrs['placeholder'] = 'Enter Email Address'
            for field in self.fields:
                self.fields[field].widget.attrs['class'] = 'form-control'
                
 """