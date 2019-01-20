#! /usr/bin/python

import unittest
import przyklad

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



if __name__ == '__main__':
    unnittest.main()
