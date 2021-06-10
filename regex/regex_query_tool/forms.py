from django import forms

class RegexForm(forms.Form):
    text        = forms.CharField(label="Insert text here", widget=forms.Textarea)
    regex_text  = forms.CharField(label="Regex here", widget=forms.Textarea)

    text.widget.attrs.update({
        'class':'form-control', 
        'cols': False, 
        'rows': False
    })

    regex_text.widget.attrs.update({
        'class': 'form-control', 
        'cols': False, 
        'rows': False
    })
