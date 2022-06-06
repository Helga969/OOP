import unittest
from PythonApplication1 import *

class Test_Club_1(unittest.TestCase):
    def test_Clb(self):
        clbb=Club('Vera', 1950, 'Moskov', Test_Sponsor, Test_Transport, Test_Treiner, Test_Gum, Test_Sportsmen)
          #clb=Club('nada', 1950, 'moskva', Test_Sponsor(spon), Test_Transport (cr), Test_Treiner(tr), Test_Gum(gm), Test_Sportsmen(sp))
        #assert('Vera', 1950, 'Moskov', Test_Sponsor(), Test_Transport, Test_Treiner, Test_Gum, Test_Sportsmen)==(clbb.nameClub, clbb.year_create, clbb.city, clbb.name_spon,clbb.type_car,clbb.treiner, clbb.gum, clbb.sportsmen)
        print("test Club1", clbb)
        cb=Club('Crvna Zvezda', 1970, 'Beograd', Test_Sponsor, Test_Transport, Test_Treiner, Test_Gum, Test_Sportsmen().test_sprt_2())
        print("test Club1", cb)
        
class Test_Sportsmen(unittest.TestCase):
    def test_sport_1(self):
    #def Test_Sportsmen_1(self):
        spr=Sportsmen('Sakson', 'Olga', 'zashitnik', 1995, 190,50, 2022, "2")
        sp3=Sportsmen("Eva", "Katsuragi", "1 nomer", 1998, 189,75, 2020,"1")
        print("test Sportsmen 1")
        return spr
        return sp3
    def test_sprt_2(self):
        #assert ('nada', 1234)==(cr.type, cr.capacity_tr)
        spr1=Sportsmen("Vik", "Viktoria", "pervii nomer", 2000, 200,65, 2022, "10")
        print("test sp1")
        sp2=Sportsmen("Ira", "Mir", "2 nomer", 1999, 196, 70, 2021, "4")
        sp4=Sportsmen("Lera", "Mir", "3 nomer", 1995, 196, 70, 2021, "3")
        
        print("test Transport 2")
      #  assert ('nada', 1234)==(cr.type, cr.capacity_tr)
    
class Test_Gum(unittest.TestCase):
    def test_Gum_1(self):
        gm=Gum('Olimpic', 'Moskva', 1500, 7865457, 'pervaya')
        print("test gum 1")
    #    assert ('nada', 1234)==(cr.type, cr.capacity_tr)

        gm2=Gum('Crvena', 'Beograd', 2000, 765311, 'vtoraya')
        print("test gum 2")
    #    assert ('nada', 1234)==(cr.type, cr.capacity_tr)
class Test_Treiner(unittest.TestCase):
    def test_Treiner_1(self):
        tr=Treiner('Ivanov', 'Ivan', 1965, 1)
        print("test Trainer 1")
      #  assert ('nada', 1234)==(cr.type, cr.capacity_tr)
        tr2=Treiner( 'Petrov', 'Igor',1970, 4)
        print("test Trainer 2")
      #  assert ('nada', 1234)==(cr.type, cr.capacity_tr)
class Test_Transport(unittest.TestCase):
    def test_Transport_1(self):
        cr=Transport( 'Bus', 144)
        print("test Transport 1")
      #  assert ('nada', 1234)==(cr.type, cr.capacity_tr)
        cr2=Transport( 'Mini', 40)
        print("test Transport 2")
      #  assert ('nada', 1234)==(cr.type, cr.capacity_tr)
class Test_Games(unittest.TestCase):
    
    def test_games_1(self):
        lst_gm=[]
        lst_gm.append(Test_Club_1().test_Clb())
        print ('test Games 1')
class Test_Sponsor(unittest.TestCase):
    def test_Sponsor_1(self):
        spon=Sponsor( 'Vera')
        print("test Sponsor 1")
       # assert ('nada', 1234)==(cr.type, cr.capacity_tr)
        spon2=Sponsor( 'Mini')
        print("test Sponsor 2")
       # assert ('nada', 1234)==(cr.type, cr.capacity_tr)


if __name__ == '__main__':
    unittest.main()
