from django.urls import path

from . views import(
    styleGuide,
    tags,
    atoms,
    molecules,
    organisms, 
    templates,
    pages,
    )
app_name = 'library'

urlpatterns = [
    path('', styleGuide, name='styleGuide'),
    path('tags/', tags, name='tags'),
    path('atoms/', atoms, name='atoms'),
    path('molecules/', molecules, name='molecules'),
    path('organisms/', organisms, name='organisms'),
    path('templates/', templates, name='templates'),
    path('pages/', pages, name='pages'),
]