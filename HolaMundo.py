import telepot, time

def principal(msj):

    tipoDeMensaje, tipoDeCHat, chatID= telepot.glance(msj)

    if(tipoDeMensaje == 'text'):
        comando = msj ['text']
        print('Comando Recibido: %s' % comando)

        if '/hola' in comando:

            bot.sendMessage(chatID, "Hola Mundo!")


bot = telepot.Bot('382778198:AAHuH71YnckzWia5AOlo8b7Rtp-YQTExsFE')
bot.message_loop(principal)

while 1:
    time.sleep(10)
