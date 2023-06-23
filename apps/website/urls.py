from django.urls import path

from . views import(index, enrol, courses, discover)

app_name = 'website'

urlpatterns = [
    path('', index, name='index'),
    path('enrol', enrol, name='enrol'),
    path('courses', courses, name='courses'),
    path('discover', discover, name='discover'),
]
