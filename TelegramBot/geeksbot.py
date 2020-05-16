from telegram.ext import Updater, CommandHandler

def main():
    #Instatanciamos el updater
    updater = Updater(token=open("./bot_token").read(), use_context=True)

    #Añadimos un manejador al comando /start
    updater.dispatcher.add_handler(CommandHandler("start", start))

    #Añadimos un manejador al comando /start
    updater.dispatcher.add_handler(CommandHandler("repite", repite))

    
    #Añadimos un manejador al comando /start
    updater.dispatcher.add_handler(CommandHandler("suma", suma))
    
    #Empezamos a pedir notificaciones a telegram
    updater.start_polling()

    #Capturamos señale de parada
    updater.idle()

def start(update, context):
    update.message.reply_text('Hola soy un bot echo por TheOredor')
    pass

def repite(update, context):
    update.message.reply_text(update.message.text)

def suma(update, context):
    # args = [ 2, 2]
    resultado = int(context.args[0]) + int(context.args[1])
    resultado = str(resultado)
    update.message.reply_text('El resultado de ' + context.args[0] + ' + ' + context.args[1] + ' es: ' + resultado)

main()