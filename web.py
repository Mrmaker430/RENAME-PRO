from flask import Flask
from threading import Thread
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "ʙᴏᴛ ɪꜱ ʀᴜɴɴɪɴɢ. Mᴀᴅᴇ ᴡɪᴛʜ ♥️ ʙʏ ༄ᶦᶰᵈ᭄࿐𝘗𝘢𝘳𝘢𝘥𝟎𝘹 么"

def run():
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))

def keep_alive():
    t = Thread(target=run)
    t.start()
