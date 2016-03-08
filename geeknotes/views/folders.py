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

TEMPLATE_FOLDER = 'folders/'

def list(request):
    folders = Folder.objects.all()
    return render(request, TEMPLATE_FOLDER + 'list.html', {'folders': folders})
    
def create(request):
    
    if request.method == 'POST':
        form = FolderForm(data=request.POST)
        if form.is_valid():
            folder = form.save()
            print folder
            messages.success(request, _('Folder saved'))
            return HttpResponseRedirect(reverse('folders_list'))
        else:
            print form.errors
            
    else:
        form = FolderForm()
    
    return render(request, TEMPLATE_FOLDER + '_create.html', {'form': form})