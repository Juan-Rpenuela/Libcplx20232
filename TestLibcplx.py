import unittest
import libreria_numeros_complejos as lc
class Testliberia_numeros_complejosfunc(unittest.TestCase):
    def test_suma(self):
        # (3.5+5.7i) + (2.8 + 4.76i) = 6.3 + 10.46i
        c1= (3.5, 5.7)
        c2= (2.8, 4.76)
        suma = lc.suma(c1,c2)
        self.assertAlmostEqual(suma[0], 6.3)
        self.assertAlmostEqual(suma[1], 10.46)
    def test2_suma(self):
        # (3+5i) + (-2.6 + 6.8i) = 0.4 + 11.8i
        c1= (3, 5)
        c2= (-2.6, 6.8)
        suma = lc.suma(c1,c2)
        self.assertAlmostEqual(suma[0], 0.4)
        self.assertAlmostEqual(suma[1], 11.8)   

    def test_resta(self):
        # (3.5+5.7i) - (2.8 + 4.76i) = 0.7000000000000002 + 0.9400000000000004i
        c1= (3.5, 5.7)
        c2= (2.8, 4.76)
        resta = lc.resta(c1,c2)
        self.assertAlmostEqual(resta[0],0.7000000000000002 )
        self.assertAlmostEqual(resta[1],0.9400000000000004)
    def test2_suma(self):
        # (3+5i) - (-2.6 + 6.8i) = 5.6 + -1.7999999999999998i
        c1= (3,5)
        c2= (-2.6, 6.8)
        resta = lc.resta(c1,c2)
        self.assertAlmostEqual(resta[0], 5.6)
        self.assertAlmostEqual(resta[1], -1.7999999999999998)

    def test_multip(self):
        # (3.5+5.7i) * (2.8 + 4.76i) = 0.7000000000000002 + 0.9400000000000004i
        c1= (3.5, 5.7)
        c2= (2.8, 4.76)
        mult = lc.multip(c1,c2)
        self.assertAlmostEqual(mult[0],-17.332 )
        self.assertAlmostEqual(mult[1],32.62)
    def test2_multip(self):
        # (3+5i) * (-2.6 + 6.8i) = -41.8 + 7.399999999999999i
        c1= (3,5)
        c2= (-2.6, 6.8)
        mult = lc.multip(c1,c2)
        self.assertAlmostEqual(mult[0], -41.8)
        self.assertAlmostEqual(mult[1], 7.399999999999999)

    def test_division(self):
        # (3+5i) / (-2.6 + 6.8i) = 0.4943396226415095 - 0.6301886792452831i
        c1= (3,5)
        c2= (-2.6, 6.8)
        div = lc.division(c1,c2)
        self.assertAlmostEqual(div[0],0.4943396226415095)
        self.assertAlmostEqual(div[1], -0.6301886792452831)

    def test2_division(self):
        # (3.5+5.7i) / (2.8 + 4.76i) = 1.2109805361733381 - 0.022952625780389313i
        c1= (3.5,5.7)
        c2= (2.8,4.76)
        div = lc.division(c1,c2)
        self.assertAlmostEqual(div[0], 1.2109805361733381)
        self.assertAlmostEqual(div[1], -0.022952625780389313)
    
    def test_conjugado(self):
        # (3+5i) = 3 - 5i
        c1= (3,5)
        conjug = lc.conjugado(c1)
        self.assertAlmostEqual(conjug[0],3)
        self.assertAlmostEqual(conjug[1], -5)
    
    def test2_conjugado(self):
        # (-2.8-4.76i) = -2.8+4,76i
        c1= (-2.8,-4.76)
        conjug = lc.conjugado(c1)
        self.assertAlmostEqual(conjug[0],-2.8)
        self.assertAlmostEqual(conjug[1],4.76)

    def test_modulo(self):
        # (3+4i) = 5
        c1= (3,4)
        mod = lc.modulo(c1)
        self.assertAlmostEqual(mod,5)

    
    def test2_modulo(self):
        # (-2.8-4.76i) = 5.522463218528485
        c1= (-2.8,-4.76)
        mod = lc.modulo(c1)
        self.assertAlmostEqual(mod,5.522463218528485)
    
    def test_fase(self):
        # (3**0.5+i) = 0.5235987755982989
        c1= (3**0.5,1)
        fas = lc.fase(c1)
        self.assertAlmostEqual(fas,0.5235987755982989)

    def test2_fase(self):
        # (2+3) = 0.982793723247329
        c1= (2,3)
        fas = lc.fase(c1)
        self.assertAlmostEqual(fas,0.982793723247329)

    def test_carte_polar(self):
        # (4+8) = (8.94427190999916,1.1071487177940904)
        c1= (4,8)
        cart = lc.carte_polar(c1)
        self.assertAlmostEqual(cart[0],8.94427190999916)
        self.assertAlmostEqual(cart[1],1.1071487177940904)
    
    def test2_carte_polar(self):
        # (5+7.5) = (9.013878188659973, 0.982793723247329)
        c1= (5,7.5)
        cart = lc.carte_polar(c1)
        self.assertAlmostEqual(cart[0],9.013878188659973)
        self.assertAlmostEqual(cart[1],0.98279372324732)

if __name__ == '__main__':
    unittest.main()

