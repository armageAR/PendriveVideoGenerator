from django import forms


from .models import Video, Category


class VideoForm(forms.ModelForm):

    class Meta:
        model = Video
        fields = ['title', 'category', 'videoFile']
        labels = {
            'title': 'Titulo',
            'category': 'Categoria',
            'videoFile': 'Archivo'
        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'autofocus': True}),
            # 'videoFile': forms.TextInput(attrs={'class': 'form-control'}),
            #'category': forms.ModelChoiceField(queryset=Category.objects.all(),to_field_name="name"),
        }
