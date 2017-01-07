
from django.contrib import admin
from .models import Registre, Personne

class PersonneAdmin(admin.ModelAdmin):
    search_fields = ('Nom','Prenom','NomAr','PrenomAr' ,'NrActe','AnActe','Datenaissance')
    list_display=('Nom','Prenom','NomAr','PrenomAr' ,'NrActe','AnActe','Datenaissance')

class RegistreAdmin(admin.ModelAdmin):
    search_fields = ('registre_numbre', 'registre_total')
    list_display = ('registre_numbre', 'registre_total')


admin.site.register(Personne,PersonneAdmin)
admin.site.register(Registre,RegistreAdmin)
