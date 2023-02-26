import threading

import app.bot.flow_bot as bot

try:
    bot_thread = threading.Thread(target=bot.start, args=[])
    bot_thread.start()
except Exception as e:
    print(e)
