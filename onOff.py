import telepot, time, serial

from telepot.namedtuple import ReplyKeyboardMarkup
ser = serial.Serial ('COM3', 9600)

def comandosTexto(msj):
    tipoDeMensaje, tipoDeChat, chatID = telepot.glance(msj)
    markup = ReplyKeyboardMarkup (keyboard=[
        ['Encendido'],
        ['Apagado']
    ])
    bot.sendMessage(chatID, '.', reply_markup = markup)

    if msj ['text'] == "Encendido":
        bot.sendMessage(chatID, "Encendido")
        ser.write(b'Y')


    if msj ['text'] == "Apagado":
        bot.sendMessage(chatID, "Apagado")
        ser.write(b'N')

def principal(msj):
    tipoDeMensaje, tipoDeChat, chatID = telepot.glance(msj)
    informacionEmisor = msj ['From']
    emisor = informacionEmisor ['First_name']

    if (tipoDeMensaje == 'text'):
        comandosTexto(msj)
    if (tipoDeMensaje == 'voice'):
        bot.sendMessage(chatID,"Lo sentimos pedro" + emisor +
                        "aun no implemento los msjs de voz")

bot = telepot.Bot('382778198:AAHuH71YnckzWia5AOlo8b7Rtp-YQTExsFE')
bot.message_loop(principal)
