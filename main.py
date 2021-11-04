from pyngrok import ngrok
import nest_asyncio
import time

ngrok.set_auth_token("20SfHPyEmnzSBKU6ooXYgRl9qCp_5JFDCSxLdRRZMpaZwCJqc")
ngrok_tunnel = ngrok.connect(22, "tcp")
print('Public URL:', ngrok_tunnel.public_url)
nest_asyncio.apply()
ONE_MONTH_IN_SECONDS = 3600*24*30
while True:
    time.sleep(ONE_MONTH_IN_SECONDS)