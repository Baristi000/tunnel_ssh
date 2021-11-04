from pyngrok import ngrok
import nest_asyncio
import time

ngrok.set_auth_token("20Sf4RN3rix4bKSTzYV3jWTDycF_2McMxfZyh8Ut3sbcMCFWz")
ngrok_tunnel = ngrok.connect(22, "tcp")
print('Public URL:', ngrok_tunnel.public_url)
nest_asyncio.apply()
ONE_MONTH_IN_SECONDS = 3600*24*30
while True:
    time.sleep(ONE_MONTH_IN_SECONDS)