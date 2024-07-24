# tg_sendmsg
Sending messages to Telegram via a bot (PyTelegramBotApi)

/opt/tg_sendmsg/venv/bin/python /opt/tg_sendmsg/main.py --caller_id Vasia


Asterisk extension config
```
;;;Отправка  номмера в ТГ
/opt/tg_sendmsg/venv/bin/python /opt/tg_sendmsg/main.py --caller_id ${CALLERID(num)} --audio_path ${AUDIO_PATH}
;;;
```