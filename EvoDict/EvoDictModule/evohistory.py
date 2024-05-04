import random
import string
import tkinter as tk
from tkinter import ttk

class EvoHistory:
  '''
  Classe représentant l'historique des dictionnaire évolué
  '''
  def __init__(self, object) :
    self.id = self.generer_id_random(4)
    self.liste_commit = {f"commit n°{self.generer_id_random(7)} - Dictionnaire n°{self.id}" : f"Création du {type(object).__name__}"}
    # Création de l'interface graphique
    self.root = tk.Tk()
    self.root.title(f"EvoHistory {self.id}")
    self.tree = ttk.Treeview(self.root)
    self.tree.pack(expand=True, fill=tk.BOTH)
    self.refresh_treeview()
       
  def generer_id_random(self, n):
    characters = string.ascii_uppercase + string.digits
    return ''.join(random.choices(characters, k=n))  
  
  def refresh_treeview(self):
        self.tree.delete(*self.tree.get_children())
        for commit, message in reversed(list(self.liste_commit.items())):
          self.tree.insert("", "end", text=commit[:16]+" : "+message)
        self.root.update()

  def commit(self, message):
        self.liste_commit[f"commit n°{self.generer_id_random(7)} - Dictionnaire n°{self.id}"] = message
        self.refresh_treeview()
    
  def __call__(self):
    self.root.mainloop()
  
  def __str__(self):
    i = 0
    for cle, value in reversed(list(self.liste_commit.items())):
      print(cle, "-->", value)
      print(i)
      i += 1
    return ""