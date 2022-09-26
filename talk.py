import pyttsx3 
import speech_recognition as sr
import pywhatkit
import yfinance as yf
import pyjokes
import webbrowser
import datetime
import wikipedia
import flask

# Escuchar nuestro microfono y devolver el audio como texto

def transformar_audio_en_texto():
    # almacenar a recognizer en una variable r
    r = sr.Recognizer()
    # configurar el microfono
    with sr.Microphone() as source:
        # tiempo de espera pause_threshold
        r.pause_threshold = 0.8
        #informar que inició la grabación
        #name = input("""
        #    Escriba su nombre: """)
        #print(f"\nYa puede hablar {name}: ")
        print(f"\nYa puede hablar mi amo")

        # guardar en variable "audio" todo lo que se ecuche 
        audio = r.listen(source)

        #Manejo de errores
        try:
            #Buscar en google
            pedido = r.recognize_google(audio, language="es")

            #prueba de ingres
            print(f"""\nUsted ha dicho: 
            {pedido}""")

            # devolver pedido
            return pedido

        # En caso de no entender el pedido
        except sr.UnknownValueError:
            #Prueba de que no comprendio el audio
            print("Señor no entiendo su orden")

            # Devolver error
            return "Sigo esperando mi amo"
        

# Función para que el asistente pueda ser escuchado
def assistant_talking(msj):
    # Iniciar el motor de pyttsx3
    engine = pyttsx3.init()
    engine.setProperty('voice','id2')

    # Pronunciar mensaje
    engine.say(msj)
    engine.runAndWait()


# Informar día de la semana
def pedir_dia():
    # Crear varia con datos de hoy
    fecha = datetime.date.today()
    print(fecha)


    #Crear variable para el día de la semana
    dia_semana = fecha.weekday()
     
    # Crear diccionario
    calendario = {0: 'Lunes',1: 'Martes',2: 'Miércoles',3: 'Jueves',4: 'Viernes', 5: 'Sábado',6: 'Domingo'}
    
    # Decir día de la semana
    assistant_talking(f'Hoy es {calendario[dia_semana]}')
    
 

# Función saludo inicial
def saludo_inicial():
    # Crear variable con datos de hora
    hora = datetime.datetime.now()
    if hora.hour < 6 or hora.hour > 20:
        momento = 'Buenas noches'
    elif 6 <= hora.hour < 13:
        momento = 'Buen día'
    else:
        momento = 'Buenas tardes'


    # Decir saludo
    assistant_talking(f'Hola, {momento} mi Amo. Soy Helena, su asistente personal')
    assistant_talking('Por favor dígame en qué le puedo servir!')

def recibir_ordenes():
    #Activar saludo inicial
    saludo_inicial()

    # Variable de corte
    comenzar = True

    #loop central
    while comenzar:
        # Activar micro y guardar el pedido en un string
        pedido = transformar_audio_en_texto().lower()

        if 'que dia es hoy' in pedido:
            assistant_talking('Con gusto, ahora mismo abro Youtube')
            pedir_dia()
            continue
 
        elif 'terminar sesión' in pedido:
            assistant_talking("Adiós mi amo, me despido, deseando de corazón que siempre esté bien!")
            break

recibir_ordenes()

#pedir_hora()
#pedir_dia()


#transformar_audio_en_texto()

# Opciones de Idioma
id1 = 'HKEY_LOCAL_MACHINE/SOFTWARE/Microsoft/Speech/Voices\Tokens/TTS_MS_ES-MX_SABINA_11.0'
id2 = 'HKEY_LOCAL_MACHINE/SOFTWARE/Microsoft/Speech/Voices/Tokens/TTS_MS_ES-ES_HELENA_11.0'
id3 = 'HKEY_LOCAL_MACHINE/SOFTWARE/Microsoft/Speech/Voices/Tokens/TTS_MS_EN-US_ZIRA_11.0'
id4 = 'HKEY_LOCAL_MACHINE/SOFTWARE/Microsoft/Speech/Voices/Tokens/TTS_MS_EN-US_DAVID_11.0'



#assistant_talking('¡Hola Beto! De corazón Espero que tengas un gran día')
#assistant_talking('Hello everybody have a nice day!')