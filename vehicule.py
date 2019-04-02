class Vehicule:
  def __init__(self,speed,weight,km):
    self.speed=speed
    self.weight=weight
    self.km=km

  def speed_limit(self,limit):
    if self.speed<=limit+limit*0.05: #marge d erreur radar
      print ("C'est bon, ça passe")
    else :
      print ("WARNING : OVERSPEED")

  def new_travel(self,L):
    self.km+=L
    print(self.km, "kilometres au compteur de ce vehicule")

  def get_weight(self):
    print("ce vehicule pese",self.weight,"kg")




class Moto(Vehicule):
  def __init__(self,speed,weight,km,casque,n_cc):
    super().__init__(speed,weight,km)
    self.casque=casque
    self.n_cc=n_cc   #nombre de centimetre cube
  
  def check_casque(self):
    if self.casque:
      print ("C'est bon, ça passe")
    else :
      print ("WARNING : NO HELMET")
  
  def race_cat(self,cat_cc):
    if self.n_cc==cat_cc:
      print("Categorie verifiée")
      return True
    elif self.n_cc>cat_cc:
      print("trop grosse cylindrée")
      return False
    else:
      print("trop petite cylindrée")
      return False




class Car(Vehicule):
  def __init__(self,speed,weight,km,n_passenger,height):
    super().__init__(speed,weight,km)
    self.n_passenger=n_passenger
    self.height=height

  def passager_plus(self,n):
    if self.n_passenger+n>5 :
      print("trop de passagers")
    else :
      self.n_passenger+=n
      print("le nombre de passagers :" , self.n_passenger)

  def pass_barriere(self,H):
    if self.height<H :
      print ("C'est bon, ça passe")
      return True
    else :
      print ("WARNING : CRASH")
      return False

Camion=Car(52,1500,12000,2,3.2)
Voiture=Car(110,950,96200,3,1.5)
Moto_course=Moto(146,550,800,True,500)
Scooter=Moto(60,400,12000,False,50)

Camion.get_weight()
Camion.new_travel(650)
Camion.pass_barriere(3)

Voiture.passager_plus(3)
Voiture.passager_plus(2)
Voiture.speed_limit(100)

Moto_course.check_casque()
Scooter.check_casque()

CAT=250
while not Moto_course.race_cat(CAT):
  CAT+=250

Scooter.speed_limit(50)





    
