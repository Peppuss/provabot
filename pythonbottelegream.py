from apscheduler.schedulers.background import BackgroundScheduler
from pyrogram import Client, filters
from pyrogram.types import ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup
import time 


admins = [444719991]
api_id = 16635563
api_hash = "c86ecebcb03126fcc4c27cadcd069abf"
app = Client("dsadsada", api_id=16635563, api_hash="c86ecebcb03126fcc4c27cadcd069abf")

activated = True
groups = [-1001690459076, -1001369710960, -1001205217457, -1001165007380, -1001145116956, -1001162943678, -1001452117544, -1001245251138, -1001230649113]
def job():
    for id in groups:
        app.send_message(id, "💲<b>PI NETWORK</b>\n\nPI Network <u>è una rivoluzionaria cripto</u> (un po' come i Bitcoin) che puoi minare tramite <b>un'app installata sul proprio smartphone</b>. Il tutto senza consumare <b>batteria</b> o <b>traffico dati</b> oltre il normale utilizzo del telefono quindi una cosa super. è proprio davvero un <b>CLOUD MINING</b>\n\n<b>❓COME FUNZIONA?</b>\n\n1. Installa l'app PI da questo link https://minepi.com/Peppusss in modo che tu abbia 1PiGreco\n2. In caso ti chiede di mettere un username di invito inserisci : <i>Peppusss</i> in modo da ricevere la tua prima moneta\n3. Dopo che hai fatto il primo tutorial, clicca a destra, dove c'è la quarta <i>sezione</i>, dove c'è  il fulmine, in modo che farmerai in <b>AUTOMATICO</b>. <u>Ogni 24 ore devi riattivare il pulsante</u>")

scheduler = BackgroundScheduler()
scheduler.add_job(job, "interval", seconds=7)

scheduler.start()
app.run()