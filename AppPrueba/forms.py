from django import forms

class CasasFormulario(forms.Form):
    escaleras=forms.BooleanField()
    numero=forms.IntegerField(required=True)
    cant_ventanas=forms.IntegerField()