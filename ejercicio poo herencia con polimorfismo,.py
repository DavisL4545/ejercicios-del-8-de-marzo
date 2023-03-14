'''
class Ventana:
    def __init__(self, titulo):
        self.titulo=titulo

    def obtenerTitulo(self):
        print(self.titulo)

class VentanaPrincipal(Ventana):
    def __init__(self, x,y,titulo):
        super(VentanaPrincipal,self).__init__(titulo)
        self.x=x
        self.y=y
    
    def obtenerTitulo(self):
        print('el titulo es =', self.titulo)

v1=Ventana('Ventana')
v2=VentanaPrincipal(20,40,'Principal')

listaVentanas=[v1,v2]

for v in listaVentanas:
    v.obtenerTitulo()


'''
'''
class Calendario:
    def __init__(self, fecha):
        self.fecha=fecha

    def obtenerFecha(self):
        return self.fecha
    
class Reloj:
    
    def __init__(self,hora):
        self.hora=hora
    
    def obtenerHora(self):
        return self.hora

class HorarioClase(Calendario,Reloj):
    
    def __init__(self, fecha,hora,aula):
        Calendario.__init__(self,fecha)
        Reloj.__init__(self,hora)
        self.aula=aula
    
    def obtenerAula(self):
        return self.aula

h1=HorarioClase('lunes y miercoles','10:40am a 12:20', 'cuidad universitaria UNIVO')
print(h1.fecha,h1.hora,h1.aula)
'''