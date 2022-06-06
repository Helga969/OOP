from datetime import datetime
from DB import *
import pickle
from abc import ABC, abstractmethod
from widget import *
_nxt=0
def _nxt_id():
    global _nxt
    _nxt+=1
    return _nxt
def print_decorator(decorator):
    def dec_pr(*arg):
        print("# # #    Получаем:  ",*arg,"    # # #")
        decorator(*arg)
    return dec_pr
def printInfo(inputObj):
    print('save to file')
    return inputObj.__editmode__()
when = datetime.today()
class Employ:
    '''Class Employ contains a description firstname, lastname, year of birth day'''

    def __init__(self, firstname, lastname, year_bday):
        self.__year_bday=year_bday
        self.__firstname=firstname
        if firstname.isalpha():
            self.__firstname=firstname
        else:
            raise ErrFirst(firstname)
        self.__lastname=lastname
        if lastname.isalpha():
            self.__lastname=lastname
        else:
            raise ErrLast
    def __str__(self):
        return 'Firstname : {0} | Lastname : {1} | Year of Birthday : {3} \n'.format(self.__firstname, self.__lastname, self.__year_bday)
    @property
    def lastname(self):
        return self.__lastname
    @lastname.setter
    def lastname(self, lastname):
        if type(lastname)!= str:
            raise TypeError("Type error. Only String")
        else:
            self.__lastname=lastname
    @property
    def fisrtname(self):
        return self.__firstname
    @fisrtname.setter
    def firstname(self, firstname):
        if type(firstname)!= str:
            raise TypeError("Type error. Only String")
        else:
            self.__firstname=firstname
    @property
    def year_bday(self):
        return self.__year_bday
    @year_bday.setter
    def year_bday(self, year_bday):
        if type(year_bday)!= int:
            raise ValueError("Type error. Only String")
        else:
            self.__yaer_bday=year_bday
    @year_bday.setter
    def year_bday2(self, year_bday):
        if year_bday>1900:
            return self.__year_bday
            #self.__year_bday=year_bday
        else:
            self.__year_bday=0
            print("unavailable")
class Trainer(Employ):
    '''Class Trainer contains a description firstname, lastname, year of birth day, rank'''

    def __init__(self, lastname, firstname, year_bday, rank):
        super(Trainer, self).__init__(lastname, firstname, year_bday)
        self.__rank=rank
        self.__id=_nxt_id()
    def __str__(self):
        return 'Trainer Lastname: {0}, Trainer Firstname: {1}, Trainer Year of birthday: {2}, Trainer Rank: {3}'.format(self._Employ__lastname, self._Employ__firstname, self._Employ__year_bday, self.__rank)
    @print_decorator
    def __call__(self, rank):
        self.__rank=rank
    @property
    def id(self):
        return self.__id
    @property
    def rank(self):
        return self.__rank
    @rank.setter
    def rank(self, rank):
        if type(rank)!= str:
            raise TypeError("Type error. Only String")
        else:
            self.__rank=rank
    def __del__(self):
        with open('transaction.txt', 'a') as f:
            f.write('when {0} : Lastname Trainer : {1} | Firstname Trainer : {2} | Trainer Year of birthday : {3} | Trainer Rank : {4} \n'.format(when, self._Employ__lastname, self._Employ__firstname, self._Employ__year_bday, self.__rank))
            f.closed
class Sportsmen(Employ):
    '''Class Sportsmen contains a description firstname, lastname, year of birth day, role, height, weight, number'''
    def __init__(self, lastname, firstname, role, year_bday, height, weight, date_hw, number):
        super(Sportsmen, self).__init__( lastname, firstname, year_bday)
        self.__role=role
        self.__height=height
       # self._HW__height=height
        self.__weight=weight
        self.__date_hw=date_hw
        self.__number=number
        self.__id=_nxt_id()
    @print_decorator
    def __call__(self, height, weight, date_hw):
  #      self.__height=height
        self.__weight=weight
        self.__date_hw=date_hw
  ##  def HW(self, height):
  #      self.__id=_nxt_id()
 #       self.__height=height
     #   self.__weight=weight
    @property
    def id(self):
        return self.__id
    @property
    def role(self):
        return self.__role
    @role.setter
    def role(self, role):
        if type(role)!= str:
            raise TypeError("Type error. Only String")
        else:
            self.__role=role
    @property
    def height(self):
        return self.__height
    @height.setter
    def height(self, height):
        if type(height)!= int:
            raise TypeError("Type error. Only String")
        else:
            self.__height=height
    @property
    def weight(self):
        return self.__weight
    @weight.setter
    def weight(self, weight):
        if type(weight)!= int:
            raise TypeError("Type error. Only String")
        else:
            self.__weight=weight        
    @property
    def date_hw(self):
        return self.__date_hw
    @date_hw.setter
    def date_hw(self, date_hw):
        if type(date_hw)!= str:
            raise TypeError("Type error. Only String")
        else:
            self.__date_hw=date_hw        
    @property
    def number(self):
        return self.__number
    @number.setter
    def number(self, number):
        if type(number)!= int:
            raise TypeError("Type error. Only String")
        else:
            self.__number=number   
    def __str__(self):
        return 'Sportsmen Lastname: {0}, Sportsmen Firstname: {1}, Sportsmen Role: {2}, Sportsmen Year of Birthday: {3}, Sportsmen Height: {4}, Sportsmen Weight: {5}, Sportsmen Date H/W: {6}, Sportsmen Number: {7}'.format(self._Employ__lastname, self._Employ__firstname, self.__role, self._Employ__year_bday, self.__height, self.__weight, self.__date_hw, self.__number)
    def __del__(self):
       with open('transaction.txt', 'a') as f:
            f.write('when {0} : Lastname sportsmen : {1} | Firstname sportsmen : {2} | Sportsmen Role: {3}, Sportsmen Year of Birthday: {4}, Sportsmen Height: {5}, Sportsmen Weight: {6}, Sportsmen Date H/W: {7}, Sportsmen Number: {8}\n'.format(when, self._Employ__lastname, self._Employ__firstname, self.__role, self._Employ__year_bday, self.__height, self.__weight, self.__date_hw, self.__number))
            f.closed
    def __editmode__(self):
        with open('HW_sport.txt', 'a') as f:
            f.write('when {0} : Lastname sportsmen : {1} |  Sportsmen Height: {2} | Sportsmen Weight: {3} | Sportsmen Date H/W: {4} | Sportsmen Number: {5}\n'.format(when, self._Employ__lastname, self.__height, self.__weight, self.__date_hw, self.__number))
            f.closed 
class Transport:
    '''Class Transport contains a description type transport and capacity'''
    def __init__(self, typ_tr, capacity_tr):
        self.__typ_tr=typ_tr
        self.__capacity_tr=capacity_tr
        self.__id=_nxt_id()
    @print_decorator
    def __call__(self, typ_tr, capacity_tr):
        self.__capacity_tr=capacity_tr
        self.__typ_tr=typ_tr
    def __str__(self):
        return 'Transport Type: {0}, Transport Capacity: {1}'.format(self.__typ_tr, self.__capacity_tr)
    def __del__(self):
        with open('transaction.txt', 'a') as f:
            f.write('when {0} : Transport : {1} | Capacity : {2}  \n'.format(when, self.__typ_tr, self.__capacity_tr))
            f.closed
    @property
    def id(self):
        return self.__id
    @property
    def typ_tr(self):
        return self.__typ_tr
    @typ_tr.setter
    def typ_tr(self, typ_tr):
        if type(typ_tr)!= str:
            raise TypeError("Type error. Only String")
        else:
            self.__typ_tr=typ_tr
    @property
    def capacity_tr(self):
        return self.__capacity_tr
    @capacity_tr.setter
    def capacity_tr(self, capacity_tr):
        if type(capacity_tr)!= int:
            raise TypeError("Type error. Only String")
        else:
            self.__capacity_tr=capacity_tr
class Gum:
    '''Class Gum contains a description name gym, adrress gym, capacity, phone number, category'''
    def __init__(self, name_gum, address, capacity, phone_number,category):
        self.__name_gum=name_gum
        self.__address=address
        self.__capacity=int(capacity)
        self.__phone_number=phone_number
        self.__category=category
        self.__id=_nxt_id()
    def __str__(self):
        return 'Gum Name: {0}, Gum Address: {1}, Gum Capacity: {2}, Gum Phone number: {3}, Gum Category: {4}'.format(self.__name_gum, self.__address, self.__capacity, self.__phone_number,self.__category)
    @print_decorator
    def __call__(self, capacity, phone_number):
        self.__capacity=capacity
        self.__phone_number=phone_number
    def __del__(self):
        with open('transaction.txt', 'a') as f:
            f.write('when {0} : Name gum : {1} |  Gum Capacity : {2} | Gum Phone number : {3} | Gum Category : {4} \n'.format(when, self.__name_gum, self.__capacity, self.__phone_number,self.__category))
            f.closed
    @property
    def id(self):
        return self.__id
    @property
    def name_gum(self):
        return self.__name_gum
    @name_gum.setter
    def name_gum(self, name_gum):
        if type(name_gum)!= str:
            raise TypeError("Type error. Only String")
        else:
            self.__name_gum=name_gum
    @property
    def address(self):
        return self.__address
    @address.setter
    def address(self, address):
        if type(address)!= str:
            raise TypeError("Type error. Only String")
        else:
            self.__address=address
    @property
    def capacity(self):
        return self.__capacity
    @capacity.setter
    def capacity(self, capacity):
        if type(capacity)!= int:
            raise TypeError("Type error. Only String")
        else:
            self.__capacity=capacity
    @property
    def phone_number(self):
        return self.__phone_number
    @phone_number.setter
    def phone_number(self, phone_number):
        if type(phone_number)!= int:
            raise TypeError("Type error. Only String")
        else:
            self.__phone_number=phone_number        
    @property
    def category(self):
        return self.__category
    @category.setter
    def category(self, category):
        if type(category)!= int:
            raise TypeError("Type error. Only int")
        else:
            self.__category=category 
class Sponsor:
    '''Class Sponsor contains a description name Sponsor'''

    def __init__(self, name_sponsor):
        self.__name_sponsor=name_sponsor
        self.__id=_nxt_id()
    def __str__(self):
        return 'Name sponsor: {0}'.format(self.__name_sponsor)
    def __del__(self):
        with open('transaction.txt', 'a') as f:
            f.write('when {0} : Sponsor : {1} :  \n'.format(when, self.__name_sponsor))
            f.closed       
    @property
    def id(self):
        return self.__id
    @property
    def name_sponsor(self):
        return self.__name_sponsor
    @name_sponsor.setter
    def name_sponsor(self, name_sponsor):
        if type(name_sponsor)!= str:
            raise TypeError("Type error. Only String")
        else:
            self.__name_sponsor=name_sponsor
class Club:
    '''Class Club contains a description name club, gym, year create, city, transport, trainer, sportsmens'''
    def __init__(self, nameClub, year_create, city, name_spon:Sponsor, type_car:Transport, trainer:Trainer, gum, *sportsmen):
        self.__nameClub=nameClub
        self.__gum=gum
        self.__year_create=year_create
        self.__city=city
        self.__name_spon=name_spon
        self.__type_car=type_car
        self.__trainer=trainer
        self.__sportsmen=sportsmen
        self.__id=_nxt_id()
    @property
    def nameClub(self):
        return self.__nameClub
    @nameClub.setter
    def nameClub(self, nameClub):
        if type(nameClub)!= str:
            raise TypeError("Type error. Only String")
        else:
            self.__nameClub=nameClub
    @property
    def id(self):
        return self.__id
    @property
    def city(self):
        return self.__city
    @city.setter
    def nameClub(self, city):
        if type(city)!= str:
            raise TypeError("Type error. Only String")
        else:
            self.__city=city
    @property
    def trainer(self):
        return self.__trainer
    @trainer.setter
    def trainer(self, trainer):
        if type(treiner)!=Trainer:
            raise TypeError("Type error. Only Class")
        else:
            self.__trainer=Trainer
    @property
    def sportsmen(self):
        return self.__sportsmen
    @sportsmen.setter
    def sportsmen(self, sportsmen):
        if type(sportsmen)!=Sportsmen:
            raise TypeError("Type error. Only Class")
        else:
            self.__sportsmen=Sportsmen
    @property
    def type_car(self):
        return self.__type_car
    @type_car.setter
    def type_car(self, type_car):
        if type(type_car)!=Transport:
            raise TypeError("Type error. Only Class")
        else:
            self.__type_car=Transport
    @property
    def name_spon(self):
        return self.__name_spon
    @name_spon.setter
    def name_spon(self, name_spon):
        if type(name_spon)!=Sponsor:
            raise TypeError("Type error. Only Class")
        else:
            self.__name_spon=Sponsor
    @property
    def gum(self):
        return self.__gum
    @gum.setter
    def gum(self, gum):
        if type(gum)!=Gum:
            raise TypeError("Type error. Only Class")
        else:
            self.__gum=Gum  
    @property
    def year_create(self):
        return self.__year_create
    @year_create.setter
    def year_create(self, year_create):
        if year_create>1900:
            self.__year_create=year_create
        else:
            self.__year_create=0
            print("unavailable")
    @year_create.setter
    def year_create2(self, year_create):
        if type(year_create)!= int:
            raise TypeError("Type error. Only INT")
        else:
            self.__year_create=year_create
    def __call__(self, treiner, gum, *sportsmen):
        self.__treiner=treiner
        self.__gum_tr=gum
        self.__sportsmen=sportsmen
    def __display_info__(self):
        print(f"year: {self.__year_create}")

    def __str__(self):

        return 'Name Club: {0}, Year Create: {1}, City: {2}, Name Sponsor: {3}, Type car: {4}, Trainer: {5} {6}, Gum: {7}, sportsmen: {8}'.format(self.__nameClub, self.__year_create, self.__city, self.__name_spon.name_sponsor,self.__type_car.typ_tr,  self.__trainer.lastname, self.__trainer.firstname, self.__gum.name_gum, self.__sportsmen)   
       # return ' : '.join(map(str, self.__nameClub,  self.__city))
    #, self.name_spon, self.type_car, self.treiner, self.gum, self.sportsmen))     
#self.__year_create,
#    def __del__(self):
#        with open('transaction.txt', 'a') as f:
#            f.write('when {0} : Club : {1} | Year Create : {2} | City : {3} | Name Sponsor : {4} | Type car : {5} | Trainer : {6} {7}| Gum : {8} | Sportsmen : {9}\n'.format(when, self.__nameClub, self.__year_create, self.__city, self.__name_spon.name_sponsor,self.__type_car.typ_tr,  self.__trainer.lastname, self.__trainer.firstname, self.__gum.name_gum, self.__sportsmen))
#            f.closed
    def __editmode__(self):
        with open('Clb_sport_trei.txt', 'a') as f:
            f.write('when {0} | Club name {1} | Lastname sportsmen : {2} \n'.format(when,self.__nameClub, self.__sportsmen))
            f.write('when {0} |Club name {1} | Lastname trainer : {2}  \n'.format(when, self.__nameClub, self.__trainer))
            f.closed 
class ErrLast(Exception):
    def __init__(self, lastname):
        self.lastname=lastname
    def __str__(self):
        return ("Input error. Value error. Only Alphabet")
class ErrFirst(Exception):
    def __init__(self, firstname):
        self.firstname=firstname
    def __str__(self):
        return ("Input error. Value error. Only Alphabet")
        print ("er")
class Serial:
    @staticmethod
    def serial1(club):
        with open ('club.pkl','wb') as f:
            pickle.dump(club, f)
        f.closed
    @staticmethod
    def deserial1():
        with open ('club.pkl','rb') as f:
            club=pickle.load(f)
        f.closed
        return club
    @staticmethod
    def serial2(transport):
        with open ('transport.pkl','wb') as f:
            pickle.dump(transport, f)
        f.closed
    @staticmethod
    def deserial2():
        with open ('transport.pkl','rb') as f:
            transport=pickle.load(f)
        f.closed
        return transport
    @staticmethod
    def serial4(sponsor):
        with open ('sponsor.pkl','wb') as f:
            pickle.dump(sponsor, f)
        f.closed
    @staticmethod
    def deserial4():
        with open ('sponsor.pkl','rb') as f:
            sponsor=pickle.load(f)
        f.closed
        return sponsor
    @staticmethod
    def serial5(treiner):
        with open ('treiner.pkl','wb') as f:
            pickle.dump(treiner, f)
        f.closed
    @staticmethod
    def deserial5():
        with open ('treiner.pkl','rb') as f:
            treiner=pickle.load(f)
        f.closed
        return treiner
    @staticmethod
    def serial6(gum):
        with open ('gum.pkl','wb') as f:
            pickle.dump(gum, f)
        f.closed
    @staticmethod
    def deserial6():
        with open ('gum.pkl','rb') as f:
            gum=pickle.load(f)
        f.closed
        return gum
    @staticmethod
    def serial7(sportsmen):
        with open ('sportsmen.pkl','wb') as f:
            pickle.dump(sportsmen, f)
        f.closed
    @staticmethod
    def deserial7():
        with open ('sportsmen.pkl','rb') as f:
            sportsmen=pickle.load(f)
        f.closed
        return sportsmen

class AbstractModel:
    def __init__(self):
        self.listeners=[]
    def addListener(self, listenerFunc):
        self.listeners.append(listenerFunc)
    def removeListener(self, listenerFunc):
        self.listeners.remove(listenerFunc)
  #  @abstract_method
    def update(self):
        for eachFunc in self.listeners:
            eachFunc(self)
    def abstract_method(self):
        raise NotImplementedError ('method is pure virtual')
class SportDB(AbstractModel):
    db={}
    filename='sportDB.pkl'
    index=0
    def __init__(self):
        super(SportDB, self).__init__()
        try:
            self.open_db()
        except:
            self.save_db()
    id=property(lambda self: self.db[self.index].id)
    lastname=property(lambda self: self.db[self.index].lastname)
    firstname=property(lambda self: self.db[self.index].firstname)
    role=property(lambda self: self.db[self.index].role)
    year_bday=property(lambda self: self.db[self.index].year_bday)
    height=property(lambda self: self.db[self.index].height)
    weight=property(lambda self: self.db[self.index].weight)
    date_hw=property(lambda self: self.db[self.index].date_hw)
    number =property(lambda self: self.db[self.index].number)
 #   @classmethod
    def __iter__(self):
        for item in self.db:
            yield self.db[item]
 #   @classmethod
    def next(self):
        if self.index==len(self.db):
            raise StopIteration
        self.index=self.index + 1
        self.update()
        return self.db[self.index]
 #   @classmethod
    def prev(self):
        if self.index <= 0:
            raise Exception("Больше записей нет!")
        else:
            try:
                self.index = self.index - 1
                while self.index >= 0 and self.index not in self.db.keys():
                    self.index = self.index - 1
                self.update()
                return self.db[self.index]
            except Exception:
                raise Exception("Больше записей нет!")
#    @classmethod
    def open_db(self):
        with open(self.filename, 'rb') as f:
            self.db=pickle.load(f)
        f.closed
#    @classmethod
    def save_db(self):
        with open(self.filename, 'wb') as f:
            pickle.dump(self.db, f)
        f.closed
 #   @classmethod
    def add_sp(self,lastname, firstname, role, year_bday, height, weight, date_hw, number):
        sport=Sportsmen(lastname, firstname, role, year_bday, height, weight, date_hw, number)
        if sport.id in self.db:
            sport.id=len(self.db.keys())[-1] + 1
        self.db[sport.id]=sport
        self.index=list(self.db.keys())[-1]
        self.update()
        self.save_db()
#    @classmethod
    def get_sp(self, id):
        if id not in self.db:
            return None
        return self.db[id]
  #  @classmethod
    def delete_sp(self, id):
        del self.db[id]
        self.save_db()
        self.index = list(self.db.keys())[0]

        self.update()
  #  @classmethod
    def change_sp(self, id, height, weight):
        sports = self.get_sp(id)
        if not sports:
            raise ValueError('value does not exist')
        sports.height = height
        sports.weight = weight
        self.update()
        self.save_db()
class TrainDB(AbstractModel):
    db={}
    filename='TrainDB.pkl'
    index=0

    def __init__(self):
        super(TrainDB, self).__init__()
        try:
            self.open_db()
        except:
            self.save_db()
    id=property(lambda self: self.db[self.index].id)
    lastname=property(lambda self: self.db[self.index].lastname)
    firstname=property(lambda self: self.db[self.index].firstname)
    year_bday=property(lambda self: self.db[self.index].year_bday)
    rank=property(lambda self: self.db[self.index].rank)

 #   @classmethod
    def __iter__(self):
        for item in self.db:
            yield self.db[item]
 #   @classmethod
    def next(self):
      #  if self.index==list(self.db.keys())[-1]:
        if self.index==len(self.db):
            raise StopIteration
        self.index=self.index + 1
        self.update()
        return self.db[self.index]
#    @classmethod
    def prev(self):
        if self.index <= 0:
            raise Exception("Больше записей нет!")
        else:
            try:
                self.index = self.index - 1
                while self.index >= 0 and self.index not in self.db.keys():
                    self.index = self.index - 1
                self.update()
                return self.db[self.index]
            except Exception:
                raise Exception("Больше записей нет!")

 #   @classmethod
    def open_db(self):
        with open(self.filename, 'rb') as f:
            self.db=pickle.load(f)
        f.closed
#    @classmethod
    def save_db(self):
        with open(self.filename, 'wb') as f:
            pickle.dump(self.db, f)
        f.closed
 #   @classmethod
    def add_train(self, lastname, firstname, year_bday, rank):
        train=Trainer(lastname, firstname, year_bday, rank)
        if train.id in self.db:
            train.id=list(self.db.keys())[-1] + 1
        self.db[train.id]=train
        self.index=list(self.db.keys())[-1]
        self.update()
        self.save_db()
 #   @classmethod
    def get_train(self, id):
        if id not in self.db:
            return None
        return self.db[id]
  #  @classmethod
    def delete_train(self, id):
        del self.db[id]
        self.save_db()
        self.index = list(self.db.keys())[0]

        self.update()
 #   @classmethod
    def change_train(self, id, rank):
        trains = self.get_train(id)
        if not trains:
            raise ValueError('value does not exist')
        trains.rank = rank
        self.update()
        self.save_db()
class TranspDB(AbstractModel):
    db={}
    filename='TranDB.pkl'
    index=0
    def __init__(self):
        super(TranspDB, self).__init__()
        try:
            self.open_db()
        except:
            self.save_db()
    id=property(lambda self: self.db[self.index].id)
    typ_tr=property(lambda self: self.db[self.index].typ_tr)
    capacity_tr=property(lambda self: self.db[self.index].capacity_tr)

#    @classmethod
    def __iter__(self):
        for item in self.db:
            yield self.db[item]
  #  @classmethod
    def next(self):
        if self.index==len(self.db):
            raise StopIteration
        self.index=self.index + 1
        self.update()
        return self.db[self.index]
#    @classmethod
    def prev(self):
        if self.index <= 0:
            raise Exception("Больше записей нет!")
        else:
            try:
                self.index = self.index - 1
                while self.index >= 0 and self.index not in self.db.keys():
                    self.index = self.index - 1
                self.update()
                return self.db[self.index]
            except Exception:
                raise Exception("Больше записей нет!")
#    @classmethod
    def open_db(self):
        with open(self.filename, 'rb') as f:
            self.db=pickle.load(f)
        f.closed
#    @classmethod
    def save_db(self):
        with open(self.filename, 'wb') as f:
            pickle.dump(self.db, f)
        f.closed
 #   @classmethod
    def add_trans(self, typ_tr, capacity_tr):
        tran=Transport(typ_tr, capacity_tr)
        if tran.id in self.db:
            tran.id=list(self.db.keys())[-1] + 1
         
        self.db[tran.id]=tran
        self.index=list(self.db.keys())[-1]
        self.update()
        self.save_db()
 #   @classmethod
    def get_trans(self, id):
        if id not in self.db:
            return None
        return self.db[id]
 #   @classmethod
    def delete_trans(self, id):
        del self.db[id]
        self.save_db()
        self.index = list(self.db.keys())[0]

        self.update()
 #   @classmethod
    def change_trans(self, id, typ_tr, capacity_tr):
        trans = self.get_trans(id)
        if not trans:
            raise ValueError('value does not exist')
        trans.typ_tr = typ_tr
        trans.capacity_tr=capacity_tr
        self.update()
        self.save_db()
class GumDB(AbstractModel):
    db={}
    filename='GumDB.pkl'
    index=0
    def __init__(self):
        super(GumDB, self).__init__()
        try:
            self.open_db()
        except:
            self.save_db()
    id=property(lambda self: self.db[self.index].id)
    name_gum=property(lambda self: self.db[self.index].name_gum)
    address=property(lambda self: self.db[self.index].address)
    capacity=property(lambda self: self.db[self.index].capacity)
    phone_number=property(lambda self: self.db[self.index].phone_number)
    category=property(lambda self: self.db[self.index].category)

#    @classmethod
    def __iter__(self):
        for item in self.db:
            yield self.db[item]
 #   @classmethod
    def next(self):
        if self.index==len(self.db):
            raise StopIteration
        self.index=self.index + 1
        self.update()
        return self.db[self.index]
 #   @classmethod
    def prev(self):
        if self.index <= 0:
            raise Exception("Больше записей нет!")
        else:
            try:
                self.index = self.index - 1
                while self.index >= 0 and self.index not in self.db.keys():
                    self.index = self.index - 1
                self.update()
                return self.db[self.index]
            except Exception:
                raise Exception("Больше записей нет!")
 #   @classmethod
    def open_db(self):
        with open(self.filename, 'rb') as f:
            self.db=pickle.load(f)
        f.closed
 #   @classmethod
    def save_db(self):
        with open(self.filename, 'wb') as f:
            pickle.dump(self.db, f)
        f.closed
 #   @classmethod
    def add_gum(self, name_gum, address, capacity, phone_number,category):
        gum=Gum( name_gum, address, capacity, phone_number,category)
        if gum.id in self.db:
            gum.id=list(self.db.keys())[-1] + 1
        
        self.db[gum.id]=gum
        self.index=list(self.db.keys())[-1]
        self.update()
        self.save_db()
  #  @classmethod
    def get_gum(self, id):
        if id not in self.db:
            return None
        return self.db[id]
  #  @classmethod
    def delete_gum(self, id):
        del self.db[id]
        self.save_db()
        self.index = list(self.db.keys())[0]

        self.update()
        
 #   @classmethod
    def change_gum(self, id,  name_gum, address, capacity, phone_number,category):
        gums = self.get_gum(id)
        if not gums:
            raise ValueError('value does not exist')
        gums.name_gum = name_gum
        gums.address = address
        gums.capacity=capacity
        gums.phone_number=phone_number
        gums.category=category
        self.update()
        self.save_db()
class SponDB(AbstractModel):
    db={}
    filename='SponDB.pkl'
    index=0
    def __init__(self):
        super(SponDB, self).__init__()
        try:
            self.open_db()
        except:
            self.save_db()
    id=property(lambda self: self.db[self.index].id)
    name_sponsor=property(lambda self: self.db[self.index].name_sponsor)

 #   @classmethod
    def __iter__(self):
        for item in self.db:
            yield self.db[item]
 #   @classmethod
    def next(self):
        if self.index==len(self.db):
            raise StopIteration
        self.index=self.index + 1
        self.update()
        return self.db[self.index]
 #   @classmethod
    def prev(self):
        if self.index <= 0:
            raise Exception("Больше записей нет!")
        else:
            try:
                self.index = self.index - 1
                while self.index >= 0 and self.index not in self.db.keys():
                    self.index = self.index - 1
                self.update()
                return self.db[self.index]
            except Exception:
                raise Exception("Больше записей нет!")
#    @classmethod
    def open_db(self):
        with open(self.filename, 'rb') as f:
            self.db=pickle.load(f)
        f.closed
#    @classmethod
    def save_db(self):
        with open(self.filename, 'wb') as f:
            pickle.dump(self.db, f)
        f.closed
  #  @classmethod
    def add_spon(self, name_sponsor):
        spon=Sponsor(name_sponsor)
        if spon.id in self.db:
            spon.id=list(self.db.keys())[-1] + 1
        
        self.db[spon.id]=spon
        self.index=list(self.db.keys())[-1]
        self.update()
        self.save_db()
 #   @classmethod
    def get_spon(self, id):
        if id not in self.db:
            return None
        return self.db[id]
 #   @classmethod
    def delete_spon(self, id):
        del self.db[id]
        self.save_db()
        self.index = list(self.db.keys())[0]

        self.update()
 #   @classmethod
    def change_spon(self,id,  name_sponsor):
        spons = self.get_spon(id)
        if not spons:
            raise ValueError('value does not exist')
        spons.name_sponsor = name_sponsor
        self.update()
        self.save_db()
class ClubDB(AbstractModel):
    db={}
    filename='ClubDB.pkl'
    index=0
    def __init__(self):
        super(ClubDB, self).__init__()
        try:
            self.open_db()
        except:
            self.save_db()
    id=property(lambda self: self.db[self.index].id)
    nameClub=property(lambda self: self.db[self.index].nameClub)
    year_create=property(lambda self: self.db[self.index].year_create)
    city=property(lambda self: self.db[self.index].city)
    type_car=property(lambda self: self.db[self.index].type_car)
    name_spon=property(lambda self: self.db[self.index].name_spon)
    trainer=property(lambda self: self.db[self.index].trainer)
    gum=property(lambda self: self.db[self.index].gum)
    sportsmen=property(lambda self: self.db[self.index].sportsmen)

#    @classmethod
    def __iter__(self):
        for item in self.db:
            yield self.db[item]
#    @classmethod
    def next(self):
        if self.index==len(self.db):
            raise StopIteration
        self.index=self.index + 1
        self.update()
        return self.db[self.index]
 #   @classmethod
    def prev(self):
        if self.index <= 0:
            raise Exception("Больше записей нет!")
        else:
            try:
                self.index = self.index - 1
                while self.index >= 0 and self.index not in self.db.keys():
                    self.index = self.index - 1
                self.update()
                return self.db[self.index]
            except Exception:
                raise Exception("Больше записей нет!")
 #   @classmethod
    def open_db(self):
        with open(self.filename, 'rb') as f:
            self.db=pickle.load(f)
        f.closed
 #   @classmethod
    def save_db(self):
        with open(self.filename, 'wb') as f:
            pickle.dump(self.db, f)
        f.closed
 #   @classmethod
    def add_club(self, nameClub, year_create, city, name_spon, type_car, trainer, gum, *sportsmen):
        club=Club(nameClub, year_create, city, name_spon, type_car, trainer, gum, *sportsmen)
        if club.id in self.db:
            club.id=list(self.db.keys())[-1] + 1
         
        self.db[club.id]=club
        self.index=list(self.db.keys())[-1]
        self.update()
        self.save_db()
  #  @classmethod
    def get_club(self, id):
        if id not in self.db:
            return None
        return self.db[id]
 #   @classmethod
    def delete_club(self, id):
        del self.db[id]
        self.save_db()
        self.index = list(self.db.keys())[0]

        self.update()
 #   @classmethod
    def change_club(self, nameClub, year_create, city, name_spon, type_car, trainer, gum, *sportsmen):
        clubs = self.get_club(id)
        if not clubs:
            raise ValueError('value does not exist')
        clubs.nameClub = nameClub
        clubs.year_create = year_create
        clubs.city=city
        clubs.name_spon=name_spon
        clubs.type_car=type_car
        clubs.trainer=trainer
        clubs.gum=gum
        clubs.sportsmen=sportsmen
        self.update()
        self.save_db()





if __name__=='__main__':
    print('Декоратор')
    
    epm=Trainer('Ivanov', 'Ivan', 1984, '1')
    epm2=Trainer('Tarasov', 'Alexander',1979,'2')
 #   print(epm('34'))
    epm3=Sportsmen("Eva", "Katsuragi", "1 nomer", 1998, 189,75, 2020,1)
    car1=Transport("bus", 200)
    car2=Transport("miniven", 20)
    sp=Sponsor("Travilini")
    sp2=Sponsor("CSKA")
    sprt=Sportsmen("Vik", "Viktoria", "pervii nomer", 2000, 200,65, 2022, 10)
    sprt2=Sportsmen("Ira", "Mir", "2 nomer", 1999, 196, 70, 2021, 4)
    sprt4=Sportsmen("Lera", "Mir", "3 nomer", 1995, 196, 70, 2021, 3)
    sprt3=Sportsmen("Eva", "Katsuragi", "1 nomer", 1998, 189,75, 2020,1)
    gm=Gum("Vera", "pervomaiskaya", 1000, 87665433, "1")
    gm2=Gum("Novi sad", "Pasterova", 600, 882349, "2")    
    c1=Club("Nadezda", 0, "Moskva", sp, car1, epm,  gm, epm3, sprt2, sprt3)
    c2=Club('CrvnZvezda', 0, "Beograd", sp2, car2, epm2, gm2, sprt4)
  #  mtc=Games(c1, c2)


  #  mtc.__repr__
    clb3=Club('Partizan', 1970,'Beograd', sp2, car2, epm2, gm2, sprt4)
    print("_____")
  #  clb1.year_create=2000
 #   clb2.year_create=1000
  #  clb3.year_create=1975
 #   sprt2.year_bday=10
 #   sprt3.year_bday=2000
    #clb1.display_info()
   # clb2.display_info()
   # clb3.display_info()
 #   print(Club.__doc__)
 #  print("####")
    #epm3.HW(1999, 333)
    print(epm)
    
#    print(Sportsmen.__doc__)
 #   print('##########')
  #  sprt2(210,70,2010)
  # print(sprt2)
  #  print('##########')
  #  gm(2000, 23945697)
  #  print (gm)
  #  print('##########')
  #  print(clb3)
  #  print('##########')
  #  clb3(epm, gm, sprt, sprt2,sprt3)
  #  print(clb3)
 #   print('##########')

  #  help(mtc)

 #   print("_____")
 #   print("###")
  #  printInfo(sprt2)
    sprt2=Sportsmen("Ira", "Mir", "2 nomer", 1999, 198, 72, 2022, 4)
  #  printInfo(sprt2)
  #  printInfo(clb1)
    clb1=Club("Nadezda", 1992, "Moskva", sp, car1, epm2,  gm, epm3, sprt, sprt4)
#    printInfo(clb1)
 #   print('###')
    
  #  print(isinstance(sp, Games))
 #   print(str(clb1))
 #   print(str(clb2))
   # print(sp.id)
    #print(epm3.HW().id)
    print("~~~~~~~~~~DB~~~~~~~~~")
    #SpDB.add_sp()
#    SportDB.add_sp("Eva", "Katsuragi", "1 nomer", 1998, 189, 75, 2020,2)
  #  SpDB.change_sp()
#    SpDB.change_sp(7,32,13)
#    SportDB.add_sp("Ira", "Mir", "2 nomer", 1999, 196, 70, 2021, 4)
 #   SportDB.add_sp("Ira", "Mir", "2 nomer", 1999, 196, 70, 2021, 4)
#    print(SpDB.get_sp(20))
  #  TranspDB.add_trans('Bus 1', 150)
  #  TranspDB.add_trans('Bus 2', 200)
  #  SponDB.add_spon('gazprom')
  #  TrainDB.add_train('Ivanov', 'Ivan', 1984, '1')
  #  TrainDB.add_train('Tarasov', 'Alexander',1979,'2')
  #  GumDB.add_gum("Vera", "pervomaiskaya", 1000, 87665433, "1")
  #  GumDB.add_gum("Novi sad", "Pasterova", 600, 882349, "2")
#    ClubDB.add_club('Real', 1920,'Madrid','Emirates Fly', 'Bus 1', 'Ivanov', 'Novi sad', 'Eva', 'Ira')
  #  ClubDB.add_club('Novisad', 1930,'Beograd', 'RIO', car1, epm, gm,sprt2,sprt3)
  #  ClubDB.add_club('Part', 1970,'Mosk', sp2, car2, epm2, gm2, sprt4,sprt)
  #  ClubDB.add_club('ssss', 1999,'arh', sp2, car2, epm2, gm2, sprt4,sprt)
  #  TranspDB.add_trans('bus', 123)
  #  TranspDB.add_trans('mini', 150)
#    print(DB_Term.printDBsport())
    print("+++++++")
 #   print(SpDB.get_train(24))
   # print (SportDB.db)
 #   print(TrainDB.db)
 #   print(TranspDB.db)
 #   print(SponDB.db)
 #   print(GumDB.db)
 #   print(ClubDB.db)
  #   print ("-----", DB_Term.printDBgame())
#    DB_Term().run()

 #   print('-----------------------------------')
 #   Serial.serial1(clb1)
 #   print('deserialize       -->>   ',Serial.deserial1())
 #   print('-----------------------------------')
 #   Serial.serial2(car1)
 #   print('deserialize       -->>   ',Serial.deserial2())
 #   print('-----------------------------------')
 #   Serial.serial3(mtc)
 #   print('deserialize       -->>   ',Serial.deserial3())
 #   print('-----------------------------------')
 #   Serial.serial4(sp)
 #   print('deserialize       -->>   ',Serial.deserial4())
 #   print('-----------------------------------')
 #   Serial.serial5(epm)
 #   print('deserialize       -->>   ',Serial.deserial5())
 #   print('-----------------------------------')
 #   Serial.serial6(gm)
 #   print('deserialize       -->>   ',Serial.deserial6())
 #   print('-----------------------------------')
 #   Serial.serial7(epm3)
 #   print('deserialize       -->>   ',Serial.deserial7())
 #   print('-----------------------------------')
    print("___")