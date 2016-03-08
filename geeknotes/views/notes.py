# -*- coding: utf-8 -*-
from django.http import HttpResponseRedirect
from django.shortcuts import HttpResponse, render
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext as _
from django.contrib import messages
from ..models import *
from ..forms import *
from taggit.models import Tag


TEMPLATE_FOLDER = 'notes/'
    
def list(request, folder_slug):
    folder = get_object_or_404(Folder, slug=folder_slug)
    
    if request.GET and request.GET.get('tag'):
        notes = folder.notes.filter(tags__slug__in=[request.GET.get('tag')])
    else:
        notes = folder.notes.all()
    
    form_notes = [(note.slug, note.title) for note in notes]
    move_form = MoveFolderForm()
    move_form.fields['notes'].choices = form_notes
    
    data = {
        'notes': notes, 
        'move_form' : move_form, 
        'folder': folder,
        'tags': Tag.objects.filter(note__folder=folder).distinct()
    }
    
    return render(request, TEMPLATE_FOLDER + 'list.html', data)
    
def move(request, folder_slug):
    folder = get_object_or_404(Folder, slug=folder_slug)
    
    if request.method == 'POST':
        
        notes = folder.notes.all()
        form_notes = [(note.slug, note.title) for note in notes]
        
        form = MoveFolderForm(request.POST)
        form.fields['notes'].choices = form_notes
        
        if form.is_valid():
            target_folder = form.cleaned_data['folder']
            
            Note.objects.filter(slug__in=form.cleaned_data['notes']).update(folder=target_folder)
            
            messages.success(request, _('Notes moved'))
            return HttpResponseRedirect(reverse('list', args=(folder_slug,)))
        else:
            print form.errors
            
    
    return HttpResponseRedirect(reverse('list', args=(folder_slug,)))
    
    
def read(request, folder_slug, slug):
    return render(request, TEMPLATE_FOLDER + 'read.html', prepare_note_data(slug, folder_slug))
    
def read_no_folder(request, slug):
    note = get_object_or_404(Note, slug=slug)
    return HttpResponseRedirect(reverse('read', args=(note.folder.slug, note.slug)))
    
def delete(request, folder_slug, slug):
    note = get_object_or_404(Note, slug=slug)
    note.delete()
    messages.success(request, _('Note deleted'))
    return HttpResponseRedirect(reverse('list'))
    
    
def create(request, folder_slug):
    
    folder = get_object_or_404(Folder, slug=folder_slug)
    previous_note = folder.notes.all()[:1]
    
    if request.method == 'POST':
        form = NoteForm(data=request.POST)
        if form.is_valid():
            note = form.save()
            messages.success(request, _('Note saved'))
            print note.slug
            return HttpResponseRedirect(reverse('edit', args=(note.folder.slug, note.slug,)))
        else:
            print form.errors
            
    else:
        form = NoteForm(initial={'folder': folder})
        
    data = {
        'form': form,
        'previous_note': previous_note,
        'folder': folder,
    }
    
    return render(request, TEMPLATE_FOLDER + 'edit.html', data)
    
def edit(request, folder_slug, slug):
    data = prepare_note_data(slug, folder_slug)
    note = data['note']
    
    if request.method == 'POST':
        form = NoteForm(data=request.POST, instance=note)
        if form.is_valid():
            note = form.save()
            messages.success(request, _('Note saved'))
            print note.slug
            return HttpResponseRedirect(reverse('edit', args=(data['folder'].slug, note.slug,)))
        else:
            print form.errors
    
    else:
        form = NoteForm(instance=note)
        
    data['form'] = form
    return render(request, TEMPLATE_FOLDER + 'edit.html', data)
    
    
def import_notes(request):
    form = ImportForm()
    
    if request.method == 'POST':
        form = ImportForm(data=request.POST)
        
        for file in form.cleaned_data['files']:
            print file
    
    data = {'form': form}
    return render(request, TEMPLATE_FOLDER + 'import.html', data)
    
    
def prepare_note_data(slug, folder_slug):
    note = get_object_or_404(Note, slug=slug)
    folder = get_object_or_404(Folder, slug=folder_slug)
    data = {
        'note': note,
        'next_note': folder.notes.filter(create_date__gt=note.create_date).order_by('create_date')[:1],
        'previous_note': folder.notes.filter(create_date__lt=note.create_date).order_by('-create_date')[:1],
        'folder': folder,
    }
    
    return data