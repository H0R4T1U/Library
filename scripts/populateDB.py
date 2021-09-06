# scripts/populateDB.py
import os

# Create your views here.
from main.models import Carte

def run():
    module_dir = os.path.dirname(__file__)  # get current directory
    file_path = os.path.join(module_dir, 'carti.txt')
    with open(file_path,'r',encoding='utf-8') as file:
        line = file.readline()
        while line:
            parts = line.split(" ")
            new_parts = []
            for part in parts:
                    cuvinte = part.split("_")
                    x = " ".join(cuvinte)
                    new_parts.append(x)
            try:
                c = Carte(name=new_parts[0],author=new_parts[1],location=new_parts[2],extra=new_parts[3])
                
            except IndexError:
                c = Carte(name=new_parts[0],author=new_parts[1],location=new_parts[2],extra=None)
            c.save()
            line = file.readline()
        file.close()
