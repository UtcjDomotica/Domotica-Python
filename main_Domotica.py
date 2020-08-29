import sys
from time import sleep
import signal
from gpiozero import LED, Button
from threading import Thread
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

Relay_1 = LED(19)
Relay_2 = LED(13)
Relay_3 = LED(22)
Relay_4 = LED(27)
Relay_5 = LED(18)
Relay_6 = LED(23)
Relay_7 = LED(24)
Relay_8 = LED(25)
Alarma1 = Button(20)
Alarma2 = Button(21)

PAHT_CRED = '/home/pi/cred.json'
URL_DB = 'https://domotica-8864c.firebaseio.com/'
REF_HOME = 'Aparatos'
REF_Alarma = 'Alarmas'
Rele_1 = 'Rele_1'
Rele_2 = 'Rele_2'
Rele_3 = 'Rele_3'
Rele_4 = 'Rele_4'
Rele_5 = 'Rele_5'
Rele_6 = 'Rele_6'
Rele_7 = 'Rele_7'
Rele_8 = 'Rele_8'
Alarma_1 = "Alarma_1"
Alarma_2 = "Alarma_2"

class IOT():

    def __init__(self):
        cred = credentials.Certificate(PAHT_CRED)
        firebase_admin.initialize_app(cred, {
            'databaseURL': URL_DB
        })

        self.refHome = db.reference(REF_HOME)
        self.refAlarmas = db.reference(REF_Alarma)
        #self.estructuraInicialDB() # solo ejecutar la primera vez
        #self.estructuraAlarmas() # solo ejecutar la primera vez
        self.refRele_1 = self.refHome.child(Rele_1)
        self.refRele_2 = self.refHome.child(Rele_2)
        self.refRele_3 = self.refHome.child(Rele_3)
        self.refRele_4 = self.refHome.child(Rele_4)
        self.refRele_5 = self.refHome.child(Rele_5)
        self.refRele_6 = self.refHome.child(Rele_6)
        self.refRele_7 = self.refHome.child(Rele_7)
        self.refRele_8 = self.refHome.child(Rele_8)

        self.refAlarma_1 = self.refAlarmas.child(Alarma_1)
        self.refAlarma_2 = self.refAlarmas.child(Alarma_2)

    def estructuraInicialDB(self):
        self.refHome.set({
                'Rele_1':True,
                'Rele_2':True,
                'Rele_3':True,
                'Rele_4':True,
                'Rele_5':True,
                'Rele_6':True,
                'Rele_7':True,
                'Rele_8':True

        })


    def estructuraAlarmas(self):
        self.refAlarmas.set({
                'Alarma_1':False,
                'Alarma_2':False
        })


########################################### Relevadores ###################################


###############################################################
    def ledControlGPIO(self, estado):
        if estado:
            Relay_1.on()
            print('Rele_1 ON')
        else:
            Relay_1.off()
            print('Rele_2 OFF')

    def lucesStart(self):

        E, i = [], 0

        estado_anterior = self.refRele_1.get()
        self.ledControlGPIO(estado_anterior)

        E.append(estado_anterior)

        while True:
          estado_actual = self.refRele_1.get()
          E.append(estado_actual)

          if E[i] != E[-1]:
              self.ledControlGPIO(estado_actual)

          del E[0]
          i = i + i
          sleep(0.4)
###############################################################

    def ledControlGPIO2(self, estado):
        if estado:
            Relay_2.on()
            print('Rele_2 ON')
        else:
            Relay_2.off()
            print('Rele_2 OFF')

    def lucesStart2(self):

        E, i = [], 0

        estado_anterior = self.refRele_2.get()
        self.ledControlGPIO2(estado_anterior)

        E.append(estado_anterior)

        while True:
          estado_actual = self.refRele_2.get()
          E.append(estado_actual)

          if E[i] != E[-1]:
              self.ledControlGPIO2(estado_actual)

          del E[0]
          i = i + i
          sleep(0.4)

###############################################################

    def ledControlGPIO3(self, estado):
        if estado:
            Relay_3.on()
            print('Rele_3 ON')
        else:
            Relay_3.off()
            print('Rele_3 OFF')

    def lucesStart3(self):

        E, i = [], 0

        estado_anterior = self.refRele_3.get()
        self.ledControlGPIO3(estado_anterior)

        E.append(estado_anterior)

        while True:
          estado_actual = self.refRele_3.get()
          E.append(estado_actual)

          if E[i] != E[-1]:
              self.ledControlGPIO3(estado_actual)

          del E[0]
          i = i + i
          sleep(0.4)


###############################################################

    def ledControlGPIO4(self, estado):
        if estado:
            Relay_4.on()
            print('Rele_4 ON')
        else:
            Relay_4.off()
            print('Rele_4 OFF')

    def lucesStart4(self):

        E, i = [], 0

        estado_anterior = self.refRele_3.get()
        self.ledControlGPIO3(estado_anterior)

        E.append(estado_anterior)

        while True:
          estado_actual = self.refRele_3.get()
          E.append(estado_actual)

          if E[i] != E[-1]:
              self.ledControlGPIO3(estado_actual)

          del E[0]
          i = i + i
          sleep(0.4)

###############################################################

    def ledControlGPIO5(self, estado):
        if estado:
            Relay_5.on()
            print('Rele_5 ON')
        else:
            Relay_5.off()
            print('Rele_5 OFF')

    def lucesStart5(self):

        E, i = [], 0

        estado_anterior = self.refRele_5.get()
        self.ledControlGPIO5(estado_anterior)

        E.append(estado_anterior)

        while True:
          estado_actual = self.refRele_5.get()
          E.append(estado_actual)

          if E[i] != E[-1]:
              self.ledControlGPIO5(estado_actual)

          del E[0]
          i = i + i
          sleep(0.4)

###############################################################

    def ledControlGPIO6(self, estado):
        if estado:
            Relay_6.on()
            print('Rele_6 ON')
        else:
            Relay_6.off()
            print('Rele_6 OFF')

    def lucesStart6(self):

        E, i = [], 0

        estado_anterior = self.refRele_6.get()
        self.ledControlGPIO6(estado_anterior)

        E.append(estado_anterior)

        while True:
          estado_actual = self.refRele_6.get()
          E.append(estado_actual)

          if E[i] != E[-1]:
              self.ledControlGPIO6(estado_actual)

          del E[0]
          i = i + i
          sleep(0.4)



###############################################################

    def ledControlGPIO7(self, estado):
        if estado:
            Relay_7.on()
            print('Rele_7 ON')
        else:
            Relay_7.off()
            print('Rele_7 OFF')

    def lucesStart7(self):

        E, i = [], 0

        estado_anterior = self.refRele_7.get()
        self.ledControlGPIO7(estado_anterior)

        E.append(estado_anterior)

        while True:
          estado_actual = self.refRele_7.get()
          E.append(estado_actual)

          if E[i] != E[-1]:
              self.ledControlGPIO7(estado_actual)

          del E[0]
          i = i + i
          sleep(0.4)

###############################################################

    def ledControlGPIO8(self, estado):
        if estado:
            Relay_8.on()
            print('Rele_8 ON')
        else:
            Relay_8.off()
            print('Rele_8 OFF')

    def lucesStart8(self):

        E, i = [], 0

        estado_anterior = self.refRele_8.get()
        self.ledControlGPIO8(estado_anterior)

        E.append(estado_anterior)

        while True:
          estado_actual = self.refRele_8.get()
          E.append(estado_actual)

          if E[i] != E[-1]:
              self.ledControlGPIO8(estado_actual)

          del E[0]
          i = i + i
          sleep(0.4)


########################################### Alarmas ###################################

def pulsador_on1(self):
    print('Alarma_1 On')
    self.refAlarma_1.set(True)

def pulsador_off1(self):
    print('Alarma_1 Off')
    self.refAlarma_1.set(False)

def botonesStart1(self):
    print('Start Alarma_1 !')
    Alarma1.when_pressed = self.pulsador_on1
    Alarma1.when_released = self.pulsador_off1

################################################################

def pulsador_on2(self):
    print('Alarma_2 On')
    self.refAlarma_2.set(True)

def pulsador_off2(self):
    print('Alarma_2 Off')
    self.refAlarma_2.set(False)

def botonesStart2(self):
    print('Start Alarma_2 !')
    Alarma2.when_pressed = self.pulsador_on2
    Alarma2.when_released = self.pulsador_off2

###############################################################

print ('START !')
iot = IOT()

subproceso_Rele_1 = Thread(target=iot.lucesStart)
subproceso_Rele_1.daemon = True
subproceso_Rele_1.start()
subproceso_Rele_2 = Thread(target=iot.lucesStart2)
subproceso_Rele_2.daemon = True
subproceso_Rele_2.start()
subproceso_Rele_3 = Thread(target=iot.lucesStart3)
subproceso_Rele_3.daemon = True
subproceso_Rele_3.start()
subproceso_Rele_4 = Thread(target=iot.lucesStart4)
subproceso_Rele_4.daemon = True
subproceso_Rele_4.start()
subproceso_Rele_5 = Thread(target=iot.lucesStart5)
subproceso_Rele_5.daemon = True
subproceso_Rele_5.start()
subproceso_Rele_6 = Thread(target=iot.lucesStart6)
subproceso_Rele_6.daemon = True
subproceso_Rele_6.start()
subproceso_Rele_7 = Thread(target=iot.lucesStart7)
subproceso_Rele_7.daemon = True
subproceso_Rele_7.start()
subproceso_Rele_8 = Thread(target=iot.lucesStart8)
subproceso_Rele_8.daemon = True
subproceso_Rele_8.start()

subproceso_Alarma1 = Thread(target=iot.botonesStart1)
subproceso_Alarma1.daemon = True
subproceso_Alarma1.start()
subproceso_Alarma2 = Thread(target=iot.botonesStart2)
subproceso_Alarma2.daemon = True
subproceso_Alarma2.start()

signal.pause()
