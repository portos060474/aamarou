# - *- coding: utf- 8 - *-
from __future__ import unicode_literals
from django.db import models


class Registre(models.Model):
    registre_numbre = models.CharField(max_length=250)
    registre_type = models.CharField(max_length=250)
    registre_desc = models.CharField(max_length=500)
    registre_total = models.IntegerField(blank=True)
    registre_mtotal = models.IntegerField(blank=True)
    registre_ftotal = models.IntegerField(blank=True)

    def __unicode__(self):
        return self.registre_numbre + '     ' + self.registre_type


class Personne(models.Model):
    registre = models.ForeignKey(Registre, on_delete=models.CASCADE)
    NrActe = models.CharField(max_length=250)
    AnActe = models.CharField(max_length=100, default="1900")
    Prenom = models.CharField(max_length=100, null=True, blank=True)
    PrenomAr = models.CharField(max_length=100, blank=True)
    Nom = models.CharField(max_length=100, blank=True)
    NomAr = models.CharField(max_length=100, blank=True)
    Sexe = models.CharField(max_length=100, default="Masculin Feminin")
    Sexe_ar = models.CharField(max_length=100, default="ذكر انثى")
    Datenaissance = models.CharField(max_length=100, blank=True)
    Datenaissance_grg = models.CharField(max_length=100, blank=True)
    Datenaissance_hij = models.CharField(max_length=100, blank=True)
    Lieu_de_naissance = models.CharField(max_length=100, blank=True)
    Lieu_de_naissanceAr = models.CharField(max_length=100, blank=True)
    Mention_Marginale = models.CharField(max_length=1000, blank=True)
    Mention_MarginaleAr = models.CharField(max_length=1000, blank=True)
    Adresse = models.CharField(max_length=400, blank=True)
    Adresse_ar = models.CharField(max_length=400, blank=True)
    Nationalite = models.CharField(max_length=100, default="Marocaine")
    Nationalite_ar = models.CharField(max_length=100, default="مغربية")
    Profession = models.CharField(max_length=100, default="Sans")
    Profession_ar = models.CharField(max_length=100, default="بدون ")
    CIN = models.CharField(max_length=100, blank=True)
    Nom_de_pere = models.CharField(max_length=100, blank=True)
    Nom_de_pere_ar = models.CharField(max_length=100, blank=True)
    Nom_de_mere = models.CharField(max_length=100, blank=True)
    Nom_de_mere_ar = models.CharField(max_length=100, blank=True)
    Nationalite_pere = models.CharField(max_length=100, default="Marocaine")
    Nationalite_pere_ar = models.CharField(max_length=100, default="مغربية")
    Professionp = models.CharField(max_length=100, blank=True)
    Profession_pere_ar = models.CharField(max_length=100, blank=True)
    Nationalite_mere = models.CharField(max_length=100, default="Marocaine")
    Nationalite_mere_ar = models.CharField(max_length=100, default="مغربية")
    Profession_mere = models.CharField(max_length=100, blank=True)
    Profession_mere_ar = models.CharField(max_length=100, blank=True)
    Declarant = models.CharField(max_length=400, blank=True)
    DeclarantAr = models.CharField(max_length=400, blank=True)
    DeclarantNrAct = models.CharField(max_length=400, blank=True)
    Declarant_age = models.CharField(max_length=400, blank=True)
    Declarant_age_ar = models.CharField(max_length=400, blank=True)
    DeclarantProf = models.CharField(max_length=400, blank=True)
    Declarant_Prof_ar = models.CharField(max_length=400, blank=True)
    Declarant_Domicil = models.CharField(max_length=400, blank=True)
    Declarant_Domicil_ar = models.CharField(max_length=400, blank=True)
    Datedeclaration = models.CharField(max_length=100, blank=True)
    Declarant_relation = models.CharField(max_length=400, default="والده والدها")
    Datedeclaration_grg = models.CharField(max_length=100, blank=True)
    Datedeclaration_hij = models.CharField(max_length=100, blank=True)
    Etat_Civil = models.CharField(max_length=100, blank=True)
    Etat_Civil_ar = models.CharField(max_length=100, blank=True)
    Confirmation = models.BooleanField(default=False)

    def __unicode__(self):
        return self.NrActe + " - " + self.AnActe + "/ "+ self.Nom + "       " + self.Prenom + "  /  "  +    self.Datenaissance + " / "  + self.NomAr + "    " +self.PrenomAr


    def get_absolute_urls(self):
        return '/naissance/%s/' % self.id

