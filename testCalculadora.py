import unittest
from parameterized import parameterized

from calculadora import suma

class testCalculadora(unittest.TestCase):
      #Fase Arrange (Organizar/inicializar)
      @parameterized.expand([[1, 2, 3], [-5, 1, -4], [-1, -3, -4]]) #datos que se van a usar en el test de suma para comprobar (resultados planificados)


    #metodo para test de la suma
      def testSuma (self, num1, num2, resultadoPlanificado):
          #Fase Act (actuar)
          resultadoObtenido = suma (num1, num2) #llama al metodo para probar con los parametros
          
          #Fase Assert (confirmar/comprobar)
          self.assertEqual(resultadoObtenido, resultadoPlanificado) #comprueba que metodo se comporta como estaba previsto (devuelve el resultado que se esperaba)
          
          
if __name__ == "__main__":
    unittest.main()
        
        
        
        
        