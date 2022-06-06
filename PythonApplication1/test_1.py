import unittest
from PythonApplication1 import *

class Test_Club_1(unittest.TestCase):
    def test_Clb(self):
        
        clbb=Club('Vera', 1950, 'Moskov', Test_Sponsor().test_Sponsor_1(), Test_Transport().test_Transport_1(), Test_Treiner().test_Treiner_1(), Test_Gum().test_Gum_1(), Test_Sportsmen().test_sport_1() )
          #clb=Club('nada', 1950, 'moskva', Test_Sponsor(spon), Test_Transport (cr), Test_Treiner(tr), Test_Gum(gm), Test_Sportsmen(sp))
        #assert('Vera', 1950, 'Moskov', Test_Sponsor(), Test_Transport, Test_Treiner, Test_Gum, Test_Sportsmen)==(clbb.nameClub, clbb.year_create, clbb.city, clbb.name_spon,clbb.type_car,clbb.treiner, clbb.gum, clbb.sportsmen)
        print("test Club1", clbb)
        return clbb
    def test_Clb2(self):
        cb=Club('Crvna Zvezda', 1970, 'Beograd', Test_Sponsor().test_Sponsor_2(), Test_Transport().test_Transport_2(), Test_Treiner().test_Treiner_2(), Test_Gum().test_Gum_2(), Test_Sportsmen().test_sprt_2())
        print("test Club1", cb)
        return cb

    def test_type_club(self):
        self.assertRaises(TypeError, Club, 333331, 'red', 12, 'viktor', 'bus', 'tarasov','vera','sportik', 'sportik2' )
        self.assertRaises(TypeError, Club, 'CSKA', 1.1, 'moskva',11,12,12,12,123,4,5,6,7,8,9,9,7,5,3,2)
class Test_Sportsmen(unittest.TestCase):
    def test_sport_1(self):
    #def Test_Sportsmen_1(self):
        spr=Sportsmen('Sakson', 'Olga', 'zashitnik', 1995, 190,50, 2022, 2)
        sp3=Sportsmen("Eva", "Katsuragi", "1 nomer", 1998, 189,75, 2020,1)
        #print("test Sportsmen 1")
        return spr, sp3
       # return sp3 
    def test_sprt_2(self):
        #assert ('nada', 1234)==(cr.type, cr.capacity_tr)
        spr1=Sportsmen("Vik", "Viktoria", "pervii nomer", 2000, 200,65, 2022, 10)
       # print("test sp1")
        sp2=Sportsmen("Ira", "Mir", "2 nomer", 1999, 196, 70, 2021, 4)
        sp4=Sportsmen("Lera", "Mir", "3 nomer", 1995, 196, 70, 2021, 3)
        return spr1, sp2, sp4
       # print("test Transport 2")
      #  assert ('nada', 1234)==(cr.type, cr.capacity_tr)
    def test_type_sport(self):
        self.assertRaises(TypeError, Sportsmen, 1,"Ivanova","1 nomer", 1998, 189,75, 2020,1)
        self.assertRaises(TypeError, Sportsmen, 'qw')
class Test_Gum(unittest.TestCase):
    def test_Gum_1(self):
        gm=Gum('Olimpic', 'Moskva', 1500, 7865457, 'pervaya')
       # print("test gum 1")
    #    assert ('nada', 1234)==(cr.type, cr.capacity_tr)
        return gm
    def test_Gum_2(self):
        gm2=Gum('Crvena', 'Beograd', 2000, 765311, 'vtoraya')
        #print("test gum 2")
        return gm2
    def test_type_gm(self):
        self.assertRaises(TypeError, Gum, 1,"Ivanova")
        self.assertRaises(TypeError, Gum, 'Olimpyc', 86.9,100,46)
    #    assert ('nada', 1234)==(cr.type, cr.capacity_tr)

   # def test_type_gum(self):
    #    self.assertRaises(TypeError, Gum, 'beograd',12, 'rgf',4566, 'eee')

class Test_Treiner(unittest.TestCase):
    def test_Treiner_1(self):
        tr=Treiner('Ivanov', 'Ivan', 1965, '1')
       # print("test Trainer 1")
      #  assert ('nada', 1234)==(cr.type, cr.capacity_tr)
        return tr
    def test_Treiner_2(self):
        tr2=Treiner( 'Petrov', 'Igor',1970, '4')
     #   print("test Trainer 2")
        return tr2
    def test_type_tre(self):
        self.assertRaises(TypeError, Treiner, 1,"Ivanova","1 nomer", 1998)
        self.assertRaises(TypeError, Treiner, 'qw')
      #  assert ('nada', 1234)==(cr.type, cr.capacity_tr)
class Test_Transport(unittest.TestCase):
    def test_Transport_1(self):
        cr=Transport( 'Bus', 144)
      #  print("test Transport 1")
        return cr
      #  assert ('nada', 1234)==(cr.type, cr.capacity_tr)
    def test_Transport_2(self):
        cr2=Transport( 'Mini', 40)
      #  print("test Transport 2")
        return cr2
    def test_type_tran(self):
        self.assertRaises(TypeError, Transport, 1,"Ivanova")
        self.assertRaises(TypeError, Transport, 1, 1)
      #  assert ('nada', 1234)==(cr.type, cr.capacity_tr)
class Test_Games(unittest.TestCase):
    lst_gm=[]
    def test_games_1(self):
        lst_gm=Games(Test_Club_1().test_Clb(), Test_Club_1().test_Clb2())
        #self.lst_gm.append(Test_Club_1().test_Clb())
        print ('test Games 1', lst_gm)
      #  print (lst_gm)
class Test_Sponsor(unittest.TestCase):
    def test_Sponsor_1(self):
        spon=Sponsor( 'Vera')
        print("test Sponsor 1")
        return spon
       # assert ('nada', 1234)==(cr.type, cr.capacity_tr)
    def test_Sponsor_2(self):
        spon2=Sponsor( 'Mini')
        print("test Sponsor 2")
        return spon2
       # assert ('nada', 1234)==(cr.type, cr.capacity_tr)
    def test_type_spon(self):
        self.assertRaises(TypeError, Sponsor, 1)
      #  self.assertRaises(TypeError, Sponsor, 'test spon')

if __name__ == '__main__':
    unittest.main()
