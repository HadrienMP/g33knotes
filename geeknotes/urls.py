from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^taggit_autosuggest/', include('taggit_autosuggest.urls')),
    url(r'^search', include('haystack.urls')),
    
    # Folders urls
    url(r'^$', 'geeknotes.views.folders.list', name='folders_list'),
    url(r'^folder/create$', 'geeknotes.views.folders.create', name='folders_create'),
    url(r'^(?P<folder_slug>[\w-]+)$', 'geeknotes.views.notes.list', name='list'),
    
    # Notes urls
    url(r'^notes/import$', 'geeknotes.views.notes.import_notes', name='import_notes'),
    url(r'^note/(?P<slug>[\w-]+)$', 'geeknotes.views.notes.read_no_folder', name='read'),
    url(r'^(?P<folder_slug>[\w-]+)/(?P<slug>[\w-]+)$', 'geeknotes.views.notes.read', name='read'),
    url(r'^(?P<folder_slug>[\w-]+)/(?P<slug>[\w-]+)/edit$', 'geeknotes.views.notes.edit', name='edit'),
    url(r'^(?P<folder_slug>[\w-]+)/(?P<slug>[\w-]+)/delete$', 'geeknotes.views.notes.delete', name='delete'),
    url(r'^(?P<folder_slug>[\w-]+)/note/create$', 'geeknotes.views.notes.create', name='create'),
    url(r'^(?P<folder_slug>[\w-]+)/notes/move$', 'geeknotes.views.notes.move', name='notes_move'),
)
