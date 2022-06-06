from datetime import datetime
from PythonApplication1 import *

class DB_Term:
    def __init__(self):
        self.db1=SportDB()
        self.db2=TrainDB()
        self.db3=TranspDB()
        self.db4=GumDB()
        self.db5=SponDB()
        self.db6=ClubDB()
    def printDBsport(self):
        for sports in self.db1:
            #return sports
            print( 'ID {0} Sportsmen Lastname: {1}, Sportsmen Firstname: {2}, Sportsmen Role: {3}, Sportsmen Year of Birthday: {4}, Sportsmen Height: {5}, Sportsmen Weight: {6}, Sportsmen Date H/W: {7}, Sportsmen Number: {8} '.format(sports.id, sports._Employ__lastname, sports._Employ__firstname, sports.role, sports.year_bday, sports.height, sports.weight, sports._Sportsmen__date_hw, sports.number ))
    def printDBtrain(self):
        for trains in self.db2:
            print('ID {0} Trainer Lastname: {1}, Trainer Firstname: {2},  Trainer Year of Birthday: {3}, Trainer rank: {4}'.format(trains.id, trains._Employ__lastname, trains._Employ__firstname, trains.year_bday, trains.rank))
    def printDBtrans(self):
        for trans in self.db3:
            print ('ID {0} Transport Type: {1}, Tranaspor capasity: {2}'.format(trans.id, trans.typ_tr, trans.capacity_tr))
    def printDBclub(self):
        for clubs in self.db6:
            print ( 'ID {0} Club Name: {1}, Year creatr: {2},  city: {3}, sponsor: {4} , transport: {5} , gum {6} , trainer {7} ,sportsmen {8}'.format(clubs.id, clubs.nameClub,  clubs.year_create, clubs.city, clubs.name_spon, clubs.type_car, clubs.gum, clubs.trainer, clubs.sportsmen))
    def printDBspon(self):
        for spons in self.db5:
            print  ('ID {0} Sponsor: {1}'.format(spons.id, spons.name_sponsor))
    def printDBgum(self):
        for gums in self.db4:
            print ('ID {0} Name: {1}, Address: {2},  Capacity: {3}, Category: {4}'.format(gums.id, gums.name_gum, gums.address, gums.capacity, gums.category))
    def run(self):
        choice=0
        while (choice!=8):
            print()
            print('1. Sportsmen')
            print('2. Trainer')
            print('3. Transport')
            print('4. Club')
            print('5. Sponsor')
            print('6. Gum')
            print('7. Games')

            print('8. EXIT')
            print('choose:')
            choice = int(input())
            if choice==1:
                self.menu_sport()
            elif choice==2:
                self.menu_trainer()
            elif choice==3:
                self.menu_transport()
            elif choice==4:
                self.menu_club()
            elif choice==5:
                self.menu_spons()
            elif choice==6:
                self.menu_gum()
            elif choice==7:
                self.menu_games()
        return choice
    def menu_sport(self):
        choice=0
        while (choice!=5):
            print()
            print('1. print DB')
            print('2. ADD sportsmen')
            print('3. DEL sportsmen')
            print('4. CHAN Sportsmen')
            print('5. EXIT')
            print('choose:')
            choice = int(input())
            if choice==1:
                self.printDBsport()
            elif choice==2:
                self.db1.add_sp( str(input(\
               'name  ')),str(input('name  ')),str(input('role  ')),int(input( 'bday   ')),int(input( 'enter height  ')),int(input( 'enter weight  ')),int(input( 'enter date hw  ')),int(input( 'enter number  ')))
            elif choice==3:
                self.db1.delete_sp(int(input(\
                "enter num")))
            elif choice==4:
                self.db1.change_sp(int(input(\
                'enter id')),int(input( 'enter height')),int(input( 'enter weight')))
        return choice
    def menu_trainer(self):
        choice=0
        while (choice!=5):
            print()
            print('1. print DB')
            print('2. ADD trainer')
            print('3. DEL trainer')
            print('4. CHAN trainer')
            print('5. EXIT')
            print('choose:')
            choice = int(input())
            if choice==1:
                self.printDBtrain()
            elif choice==2:
                self.db2.add_train( str(input(\
               'name  ')),str(input('name  ')),int(input( 'bday   ')),str(input( 'enter rank  '))),
            elif choice==3: 
                self.db2.delete_train(int(input(\
                "enter num")))
            elif choice==4:
                self.db2.change_train(int(input(\
                'enter id')),str(input( 'enter rank')))

        return choice
    def menu_transport(self):
        choice=0
        while (choice!=5):
            print()
            print('1. print DB')
            print('2. ADD transport')
            print('3. DEL transport')
            print('4. CHAN transport')
            print('5. EXIT')
            print('choose:')
            choice = int(input())
            if choice==1:
                self.printDBtrans()
            elif choice==2:
                self.db3.add_trans( str(input(\
               'Type  ')),int(input( 'capacity   ')))
            elif choice==3:
                self.db3.delete_trans(int(input(\
                "enter num")))
            elif choice==4:
                self.db3.change_trans(int(input(\
                'enter id  ')),str(input( 'enter type  ')),int(input(\
                'enter capacity  ')))
        return choice
    def menu_club(self):
        choice=0
        while (choice!=5):
            print()
            print('1. print DB Club')
            print('2. ADD Club')
            print('3. DEL Club')
            print('4. CHAN Club')
            print('5. EXIT')
            print('choose:')
            choice = int(input())
            if choice==1:
                self.printDBclub()
            elif choice==2:
                self.db6.add_club( str(input('name Club  ')),int(input('Year create  ')),str(input('city  ')),str(input( 'sponsor   ')),str(input( 'transport  ')),str(input( 'trainer  ')),str(input( 'gum  ')),str(input( 'sportsmen  ')))
            elif choice==3:
                self.db6.delete_club(int(input(\
                "enter num")))
            elif choice==4:
                self.db6.change_club( int(input('enter id')),str(input( 'gum  ')),str(input( 'sportsmen  ')))
             #   nameClub, year_create, city, name_spon, type_car, trainer, gum, *sportsmen
        return choice
    def menu_spons(self):
        choice=0
        while (choice!=5):
            print()
            print('1. print DB Sponsor')
            print('2. ADD sponsor')
            print('3. DEL sponsor')
            print('4. CHAN Sponsor')
            print('5. EXIT')
            print('choose:')
            choice = int(input())
            if choice==1:
                self.printDBspon()
            elif choice==2:
                self.db5.add_spon( str(input(\
               'name  ')))
            elif choice==3:
                self.db5.delete_spon(int(input(\
                "enter num   ")))
            elif choice==4:
                self.db5.change_spon(int(input(\
                'enter id   ')),str(input( 'name   ')))
        return choice
    def menu_gum(self):
        choice=0
        while (choice!=5):
            print()
            print('1. print DB Gum')
            print('2. ADD Gum')
            print('3. DEL Gum')
            print('4. CHAN Gum')
            print('5. EXIT')
            print('choose:')
            choice = int(input())
            if choice==1:
                self.printDBgum()
            elif choice==2:
                self.db4.add_gum( str(input(\
               'name  ')),str(input('address  ')),int(input( 'capacity   ')),int(input( 'phone number  ')),int(input( 'category  ')))
            elif choice==3:
                self.db4.delete_gum(int(input(\
                "enter num")))
            elif choice==4:
                self.db4.change_gum(int(input(\
                'enter id')),str(input('name gum  ')),str(input('address  ')),int(input( 'capacity   ')),int(input( 'phone number  ')),int(input( 'category  ')))
        return choice
if __name__ == '__main__':
    DB_Term().run()