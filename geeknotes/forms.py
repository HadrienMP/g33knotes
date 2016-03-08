from django import forms
from datetimewidget.widgets import DateTimeWidget
from .models import *
from multiupload.fields import MultiFileField

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'create_date', 'content', 'tags', 'folder']
        widgets = {
            #Use localization and bootstrap 3
            'create_date': DateTimeWidget(attrs={'id':"create_date"}, usel10n = True, bootstrap_version=3)
        }

class FolderForm(forms.ModelForm):
    class Meta:
        model = Folder
        exclude = ['slug']
        
class MoveFolderForm(forms.Form):
    folder = forms.ModelChoiceField(queryset=Folder.objects.all(), empty_label=None)
    notes = forms.MultipleChoiceField(choices=(), required=True, widget=forms.CheckboxSelectMultiple)
    
    
class ImportForm(forms.Form):
    files = MultiFileField(min_num=1, max_num=25, max_file_size=1024*1024*5)