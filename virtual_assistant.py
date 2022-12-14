import pyttsx3 
import speech_recognition as sr
import pywhatkit
import yfinance as yf
import pyjokes
import webbrowser
import datetime
import wikipedia
import flask
import subprocess

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

        # guardar en variable "audio" lo que se ecuche 
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
        # En caso de no devolver el pedido
        except sr.RequestError:
            #prueba de que no comprendió el audio
            print("Amo, no entiendo su orden")

            # devolver error
            return "Sigo esperando mi amo"

        #Error inesperado
        except:
             #Prueba de que no comprendió el audio
             print("Mi amo, lo siento. Algo ha salido mal...")

             # devolver error
             return "Amo sigo esperando, una disculpa por favor"


# Función para que el asistente pueda ser escuchado
def assistant_talking(msj):
    # Iniciar el motor de pyttsx3
    engine = pyttsx3.init()
    engine.setProperty('voice','id1')

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
    
    
def pedir_hora():
    #Crear variable con datos de la hora
    hora = datetime.datetime.now()
    hora = f'En este momento son las {hora.hour} horas con {hora.minute} minutos' # y {hora.second} segundos
    print(hora)

    #Decir la hora
    assistant_talking(hora)


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
        print("""
            Menús:
                - Hola
                - Abrir youtube
                - Reproducir + mi búsqueda en Youtube
                - Abrir Correo
                - Abrir Fatiga
                - Abrir navegador por favor
                - Buscar en Google + mi búsqueda en Google
                - Qué día es hoy?
                - Qué hora es?
                - Adiós
                - Catarinas
                - Terminar Sesión


            """)

        # add libreria = get_sapace
        pedido = transformar_audio_en_texto().lower()
        
        if 'abrir youtube' in pedido:
            assistant_talking('Con gusto, ahora mismo abro Youtube')
            webbrowser.open('https://www.youtube.com')
            continue
        elif 'reproducir' in pedido:
            pedido = pedido.replace('reproducir', '')
            assistant_talking(f'Claro, abriré en youtube {pedido}')
            webbrowser.open(f'https://www.youtube.com/search?q={pedido}')
            continue
        elif 'abrir correo' in pedido:
            assistant_talking(f'Claro, abriré correo')
            webbrowser.open(f'https://mail.google.com/mail/u/0/#inbox')
            continue    
        elif 'abrir fatiga' in pedido:
            pedido = pedido.replace('reproducir', '')
            assistant_talking(f'Claro, abriendo el sistema')
            webbrowser.open(f'http://localhost/fatiga/enviaFatiga.php?mov=1')
            continue
        elif 'abrir navegador por favor' in pedido:
            assistant_talking('Claro, estoy en ello')
            
            # Sitios cool: https://jcweb.es/7-web-con-animaciones-css-y-html-de-2021-para-inspirarte/
            webbrowser.open('https://umamiland.withgoogle.com/en')#http://www.airforce.com/intothestorm
            #webbrowser.open('http://www.airforce.com/intothestorm')
            #https://www.google.com/search?q=vida
            continue
        elif 'qué día es hoy' in pedido:
            pedir_dia()
            continue
        elif 'qué hora es' in pedido:
            pedir_hora()
            continue
        elif 'buscar en google' in pedido:
            try:
                pedido = pedido.replace('buscar en google', '')
                webbrowser.open(f'https://www.google.com/search?q={pedido}')
                wikipedia.set_lang('es')
                resultado = wikipedia.summary(pedido, sentences=1)
                assistant_talking('Wikidepdia dice lo siguiente: ')
                assistant_talking(resultado)
                continue
            except:
                assistant_talking('Algo ha salido fuera de lo esperado: ')
                print("Upsss, algo ha salido fuera de lo esperado")
        elif 'catarinas' in pedido:
            #pedir_dia()
            assistant_talking('Disculpe Amo. ¿Se refiere a su amigo, Dani. o a Luis Columna?')
            continue
        elif 'adiós' in pedido:
            #pedir_dia()
            assistant_talking('Disculpe Amo. ¿puedo decirlo?. Es un excelente Dev, pero... creo que no sabe comunicarse con las mujeres')
            continue
        elif 'hola' in pedido:
            #pedir_dia()
            assistant_talking('Hola en qué puedo ayudarle mi Amo')
            continue    
        elif 'terminar sesión' in pedido:
            assistant_talking("Adiós mi amo, me despido, deseando de corazón que siempre esté bien!")
            break

recibir_ordenes()

#pedir_hora()
#pedir_dia()


#transformar_audio_en_texto()

# Opciones de Idioma
id1 = 'HKEY_LOCAL_MACHINE/SOFTWARE/Microsoft/Speech/Voices/Tokens/TTS_MS_ES-MX_SABINA_11.0'
id2 = 'HKEY_LOCAL_MACHINE/SOFTWARE/Microsoft/Speech/Voices/Tokens/TTS_MS_ES-ES_HELENA_11.0'
id3 = 'HKEY_LOCAL_MACHINE/SOFTWARE/Microsoft/Speech/Voices/Tokens/TTS_MS_EN-US_ZIRA_11.0'
id4 = 'HKEY_LOCAL_MACHINE/SOFTWARE/Microsoft/Speech/Voices/Tokens/TTS_MS_EN-US_DAVID_11.0'



#assistant_talking('¡Hola Beto! De corazón Espero que tengas un gran día')
#assistant_talking('Hello everybody have a nice day!')