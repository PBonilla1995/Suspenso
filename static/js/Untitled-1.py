import time
from datetime import datetime
import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO

#######pulsador y led 1
Push1=40
LED_1=38
######pulsador y led 2
Push2=37
LED_2=35

mqttc=mqtt.Client()
#establecimiento del modo de los pines de la tarjeta
GPIO.setmode(GPIO.BOARD)

def main():
    global mqttc
    mqttc=mqtt.Client()
    mqttc.on_message=on_message
    mqttc.username_pw_set("patriciabonilla1995@gmail.com","1726646654")
    mqttc.connect("maqiatto.com",1883)
    mqttc.subscribe("patriciabonilla1995@gmail.com/test1",0)
    GPIO.setup(Push1,GPIO.IN)
    GPIO.setup(LED_1,GPIO.OUT)
    GPIO.setup(Push2,GPIO.IN)
    GPIO.setup(LED_2,GPIO.OUT)
    #creacion del archivo
    File=open("Prueba.txt","w")
    File.write("Datos recolectados de los led\n")
    DatosIni=" "
    Fecha_Hora=0
    
    i=0
    while(1):
       
        mqttc.loop()
        File=open("Prueba.txt","a")
        Fecha_Hora=datetime.now()
        DatosIni=str(Fecha_Hora).split(".")[0].replace("-","/")

        if(GPIO.input(Push1)==0):
            i=i+1
            File.write(str(i)+"._ Fecha&Hora: "+DatosIni+"\n    Accion: Se ha encendido el LED_1\n")
            GPIO.output(LED_1,1)
            mqttc.publish("patriciabonilla1995@gmail.com/test","Led-Encendido-Apagado")
            time.sleep(1)
            mqttc.publish("patriciabonilla1995@gmail.com/test","Led-Apagado-Apagado")
            GPIO.output(LED_1,0)
            File.close()

        if(GPIO.input(Push2)==0):
            i=i+1
            File.write(str(i)+"._ Fecha&Hora: "+DatosIni+"\n    Accion: Se ha encendido el LED_2\n")
            GPIO.output(LED_2,1)
            mqttc.publish("patriciabonilla1995@gmail.com/test","Led-Apagado-Encendido")
            time.sleep(1)
            mqttc.publish("patriciabonilla1995@gmail.com/test","Led-Apagado-Apagado")
            GPIO.output(LED_2,0)
            File.close()
      

def on_message(client,obj,msg):
    print(msg.topic+" "+str(msg.qos)+" "+msg.payload.decode('utf-8'))
    if(msg.payload.decode('utf-8')=="0"):
        Leer_Datos()

def Leer_Datos():
    global mqttc
    File=open("Prueba.txt", "r")
    file_send=str(File.read())
    print(file_send)
    mqttc.publish("patriciabonilla1995@gmail.com/test","Datos-"+file_send)

            