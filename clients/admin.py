from django.contrib import admin
from .models import *

class ClientTypeAdmin (admin.ModelAdmin):    
    list_display = [field.name for field in ClientType._meta.fields]
    list_display_links = ('id', 'name_type')    

    class Meta:
        model = ClientType

admin.site.register(ClientType, ClientTypeAdmin)  

class ClientAdmin (admin.ModelAdmin):    
    list_display = [field.name for field in Client._meta.fields]
    list_display_links = ('id', 'name')
    list_filter = ['name']	
    search_fields = ('name', 'code_client')
    
    class Meta:
        model = Client

admin.site.register(Client, ClientAdmin)  