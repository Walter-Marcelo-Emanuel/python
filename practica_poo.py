#yo soy una clase ;)
class Cuerpo(): 
     altura=170
     peso=80
     piernas=2
     camina=False 
     #esto es un metodo
     def estado(self): 
     #esto es el comportamiento 
           self.camina=True 
          
     #otro metodo 
     def avanza(self): 
     #mis opciones son comportamiento 
           if (self.camina):
            return "voy caminando " 
           else: 
            return "espero el micro"

 #define el objeto miCuerpo y a que clase pertenece
miCuerpo=Cuerpo() 
 
print("mi altura es: ",miCuerpo.altura," cm") 
print("tengo:", miCuerpo.piernas , " piernas")
miCuerpo.estado() 
print(miCuerpo.avanza())