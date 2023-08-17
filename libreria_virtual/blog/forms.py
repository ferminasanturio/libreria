from django import forms

class ArticuloFormulario(forms.Form):
   titulo = forms.CharField(required=True, max_length=64)
   subtitulo = forms.CharField(required=True, max_length=64)
   cuerpo = forms.CharField(max_length=50000, required=True)
   autor = forms.CharField(required=True, max_length=256)
   fecha = forms.DateField(required=True)