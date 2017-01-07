# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404
from .models import Registre
from django.template import loader
from django.http import HttpResponse
from .models import Personne
from django.template.loader import get_template
from django.template import Context
from django.http import Http404, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

import MySQLdb



@login_required()
def rnaissance(request):
    #all_registres = Registre.objects.all().order_by("registre_numbre")
    #a = Personne.objects.count()
    #return render(request, 'Nregistre.html', {'all_registres' : all_registres},a)

    all_registres = Registre.objects.all().order_by("registre_numbre")
    a = Personne.objects.count()

    context = {
        "all_registres" : all_registres,
        "counter" : a ,
        "title": "List of posts"
     }
    return render(request, 'naissance/Nregistre.html', context)


@login_required()
def anaissance(request, registre_id):
    registre = get_object_or_404(Registre, pk=registre_id)
    return render(request, 'naissance/Nactes.html', {'registre': registre})

@login_required()
def get_actenaissance(request, NrActe, AnActe ):
    conn = MySQLdb.connect (host = "127.0.0.1", user = "root", passwd = "your_mysql_password", db = "ecm" ,charset='utf8',use_unicode=True)
    cursor = conn.cursor()
    cursor.execute ("select Prenom,Nom, Datenaissance,Lieu_de_naissance,Nationalite,Profession,Etat_Civil, CIN, Datedeclaration, NomAr,Nom_de_pere, Nom_de_mere ,PrenomAr,Etat_Civil_ar,Declarant,DeclarantAr,Profession_ar,Nationalite_ar,Lieu_de_naissanceAr,Nom_de_pere_ar,Nom_de_mere_ar,Sexe,Sexe_ar,Adresse,Adresse_ar,Mention_Marginale,Mention_MarginaleAr  from naissance_personne where NrActe = '"+NrActe+"' and AnActe = '"+AnActe+"'")

    if cursor.rowcount == 0:
        html = "<html><body> There is no Course with number </body></html>"
    else:
        row = cursor.fetchone()
        t = get_template('naissance/NacteDetail.html')
        c = Context({ 'NrActe' : NrActe,'AnActe' : AnActe, 'Prenom' : row[0], 'Nom' : row[1], 'Datenaissance' : row[2], 'Lieu_de_naissance' : row[3], 'Nationalite' : row[4], 'Profession' : row[5]
                      , 'Etat_Civil' : row[6], 'CIN': row[7], 'Datedeclaration' : row[8],'NomAr':row[9], 'Nom_de_pere' : row[10]
                        ,'Nom_de_mere':row[11], 'PrenomAr' : row[12],'Etat_Civil_ar' : row[13], 'Declarant' : row[14],
                      'DeclarantAr': row[15],'Profession_ar' : row[16], 'Nationalite_ar' : row[17], 'Lieu_de_naissanceAr':row [18],
                      'Nom_de_pere_ar':row[19],'Nom_de_mere_ar':row[20],'Sexe':row[21],'Sexe_ar':row[22], 'Adresse':row[23],'Adresse_ar':row[24],'Mention_Marginale':row[25],'Mention_MarginaleAr':row[26]})
        html = t.render(c)
        return HttpResponse(html)

@login_required()
def confirm (request, registre_id):
    registre = get_object_or_404(Registre, pk=registre_id)
    try:
        selected_personne = registre.personne_set.get(pk=request.POST['personne'])

    except (keyError, Personne.DoesNotExist):
        return render(request, 'naissance/NacteDetail.html', {
           'registre': registre,
            'error_message' : "You did not select a valid song"
        })

    else:
        selected_personne.is_favorite = True
        selected_personne.save()
        return render(request, 'naissance/NacteDetail.html', {'registre': registre})



