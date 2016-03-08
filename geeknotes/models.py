# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext as _
from django.utils import timezone
from taggit_autosuggest.managers import TaggableManager
from mistune import markdown
from django.dispatch import receiver
from django.db.models.signals import pre_save
from django.template.defaultfilters import slugify
from filer.fields.file import FilerFileField
from filer.fields.image import FilerImageField

class Folder(models.Model):
    name = models.CharField(_("Nom"), max_length=255)
    slug = models.SlugField(_("URL"), blank=True)
    icon = FilerImageField(null=True, blank=True, related_name="foler_image")
    fa = models.CharField(_(u"FA Icon"), blank=True, max_length=100)
    
    def __unicode__(self):
        return "%s : %s" % (self.name, len(self.notes.all()))

class Note(models.Model):
    title = models.CharField(_("Titre"), max_length=255)
    slug = models.SlugField(_("URL"), blank=True)
    create_date = models.DateTimeField(_("Date"), default=timezone.now)
    auto_create_date = models.DateTimeField(auto_now_add=True)
    auto_update_date = models.DateTimeField(auto_now=True)
    content = models.TextField(_("Note"))
    html = models.TextField(blank=True)
    tags = TaggableManager()
    
    folder = models.ForeignKey(Folder, related_name="notes", default=1)
    
    def __unicode__(self):
        return "%s" % self.title
    
    class Meta:
        ordering = ['-create_date']

class Attachment(models.Model):
    file = FilerFileField(related_name="attachment_file")
    
    note = models.ForeignKey(Note, related_name="attachments")
    
@receiver(pre_save, sender=Note)
def post_note_save(sender, instance, *args, **kwargs):
    instance.slug = slugify(instance.title)
    instance.html = markdown(instance.content)
    
@receiver(pre_save, sender=Folder)
def post_folder_save(sender, instance, *args, **kwargs):
    instance.slug = slugify(instance.name)
    