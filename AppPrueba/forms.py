from django import forms

class CasasFormulario(forms.Form):
    escaleras=forms.BooleanField()
    numero=forms.IntegerField(required=True)
    cant_ventanas=forms.IntegerField()

class MascotasFormulario(forms.Form):
    nombre=forms.CharField()
    edad=forms.IntegerField(required=True)
    animal=forms.CharField()

class VecinosFormulario(forms.Form):
    nombre=forms.CharField()
    numero=forms.IntegerField(required=True)
    apellido=forms.CharField()