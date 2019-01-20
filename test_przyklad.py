#! /usr/bin/python

import unittest
import przyklad
import random


class klasa_testowa (unittest.TestCase):
            def test_test(self):
                self.assertTrue(True)

            def test_f1_1(self):
                w=przyklad.f1(0)
                self.assertEqual(w,0)

            def test_f1_2(self):
                w=przyklad.f1(1)
                self.assertEqual(w,1)

            def test_f1_3(self):
                w=przyklad.f1(2)
                self.assertEqual(w,4)

            def test_f1_4(self):
                w=przyklad.f1(2,1)
                self.assertEqual(w,5)

            def test_f1_5(self):
                w=przyklad.f1(2,3)
                self.assertEqual(w,7)

            def test_f2_1(self):
                w=przyklad.f2('ala')
                self.assertEqual(w,'a')

            def test_f2_2(self):
                w=przyklad.f2([1,2,3])
                self.assertEqual(w,1)

            def test_f2_3(self):
                w=przyklad.f2([])
                self.assertEqual(w,"BUUUM")

            def test_f3_1(self):
                w=przyklad.f3(1)
                self.assertEqual(w,"jeden")

            def test_f3_2(self):
                w=przyklad.f3(2)
                self.assertEqual(w,"dwa")

            def test_f3_3(self):
                w=przyklad.f3(3)
                self.assertEqual(w,"trzy")

            def test_f3_4(self):
                w=przyklad.f3(random.choice(range(4,1000)))
                self.assertEqual(w,"other")

            def test_4_1(self):
                w=przyklad.f4("ala")
                self.assertEqual(w,"ala ma kota")

            def test_4_2(self):
                w=przyklad.f4("kot")
                self.assertEqual(w,"kot ma kota")

            def test_4_3(self):
                w=przyklad.f4("kot","psa")
                self.assertEqual(w,"kot ma kota i psa")

            def test_4_4(self):
                w=przyklad.f4("kot","mysz")
                self.assertEqual(w,"kot ma kota i mysz")

            def test_f5_1(self):
                w=przyklad.f5(0)
                self.assertEqual(w,[])

            def test_f5_2(self):
                w=przyklad.f5(1)
                self.assertEqual(w,[0])

            def test_f5_3(self):
                w=przyklad.f5(2)
                self.assertEqual(w,[0,1])

            def test_f5_4(self):
                w=przyklad.f5(7)
                self.assertEqual(w,[0,1,2,3,4,5,6])

            def test_f5_5(self):
                w=przyklad.f5(7,2)
                self.assertEqual(w,[0,2,4,6])

            def test_f5_6(self):
                w=przyklad.f5(17,2)
                self.assertEqual(w,[0,2,4,6,8,10,12,14,16])

            def test_f5_7(self):
                w=przyklad.f5(17,5)
                self.assertEqual(w,[0,5,10,15])

            def test_f6_1(self):
                w=przyklad.f6(1)
                self.assertEqual(w,"*")

            def test_f6_2(self):
                w=przyklad.f6(7)
                self.assertEqual(w,"*******")

            def test_f7_1(self):
                w=przyklad.f7("ala")
                self.assertEqual(w,"slowo")

            def test_f7_2(self):
                w=przyklad.f7(1)
                self.assertEqual(w,"cyfra")

            def test_f7_2(self):
                w=przyklad.f7(11111)
                self.assertEqual(w,"liczba")

            def test_f7_3(self):
                w=przyklad.f7(-11111)
                self.assertEqual(w,"liczba ze znakiem")

            def test_f7_4(self):
                w=przyklad.f7("Ala ma kota")
                self.assertEqual(w,"zdanie")

            def test_f7_5(self):
                w=przyklad.f7("<taaag>")
                self.assertEqual(w,"tag poczatkowy")

            def test_f7_6(self):
                w=przyklad.f7("</taaag>")
                self.assertEqual(w,"tag koncowy")

            def test_f8_1(self):
                w=przyklad.f8("kot", "ala ma kota")
                self.assertEqual(w,True)
            def test_f8_2(self):
                w=przyklad.f8("pies", "ala ma kota")
                self.assertEqual(w,False)

            def test_f9_1(self):
                w=przyklad.f9(1,2)
                self.assertEqual(w,"dodatnie")

            def test_f9_2(self):
                w=przyklad.f9(-1,-2)
                self.assertEqual(w,"ujemne")

            def test_f9_4(self):
                w=przyklad.f9(-1,1)
                self.assertEqual(w,"roznych znakow")

            def test_f9_5(self):
                w=przyklad.f9(-1,0)
                self.assertEqual(w,"zero")

    
            def test_f10_1(self):
                w=przyklad.f10(1,1)
                self.assertEqual(w,"rowne")

            def test_f10_2(self):
                w=przyklad.f10(1,2)
                self.assertEqual(w,"rozne")

















if __name__ == '__main__':
    unnittest.main()
