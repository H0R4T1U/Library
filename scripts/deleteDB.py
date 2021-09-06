# scripts/deleteDB.py

from django.db.models.base import Model
from main.models import Carte

def run():
    carti = Carte.objects.all()
    carti.delete()