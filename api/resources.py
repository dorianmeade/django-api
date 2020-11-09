from tastypie.resources import ModelResource
from tastypie.authorization import Authorization
from api.models import Note


class NoteResource(ModelResource):
    class Meta:
        queryset = Note.objects.all() #query set = all notes
        resource_name = 'note' # name important for url
        authorization = Authorization()
        #can limit which fields returned with 
        #fields = ['title', 'body']