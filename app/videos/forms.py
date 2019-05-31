from django import forms


from .models import Video


class VideoForm(forms.ModelForm):
    title = forms.CharField(label='Titulo', widget=forms.TextInput(
        attrs={"placeholder": "Video title", "class": "form-control"}))
    category = forms.

    class Meta:
        model = Video
        fields = [
            'title', 'category', 'videoFile'

        ]
