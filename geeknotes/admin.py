from django.contrib import admin
from django.forms import ModelForm
from django.contrib.admin import ModelAdmin
from suit_redactor.widgets import RedactorWidget
from suit.widgets import AutosizedTextarea
from .models import *
import reversion

class NoteForm(ModelForm):
    class Meta:
        widgets = {
            'html': RedactorWidget(editor_options={'lang': 'fr'}),
            'content': AutosizedTextarea(attrs={'style': 'max-height: 600px; width: 100%; box-sizing : border-box;'}),
        }

class NoteAdmin(reversion.VersionAdmin):
    form = NoteForm

class FolderAdmin(admin.ModelAdmin):
    list_display = ('name', 'note_number')

    def note_number(self, obj):
        return "%d" % len(obj.notes.all())
    note_number.short_description = 'Notes'

admin.site.register(Note, NoteAdmin)
admin.site.register(Folder, FolderAdmin)