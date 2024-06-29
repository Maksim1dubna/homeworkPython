import requests as rq
import logging

logger200 = logging.getLogger('RequestsLogger')
loggerNo200 = logging.getLogger('RequestsLoggerError')
loggerNoResp = logging.getLogger('RequestsLoggerResponse')

sites = ['https://www.youtube.com/', 'https://instagram.com', 'https://wikipedia.org', 'https://yahoo.com',
         'https://yandex.ru', 'https://whatsapp.com', 'https://twitter.com', 'https://amazon.com', 'https://tiktok.com',
         'https://www.ozon.ru']
logger200.setLevel(logging.INFO)
loggerNo200.setLevel(logging.ERROR)
loggerNoResp.setLevel(logging.WARNING)

logger200hand = logging.FileHandler("success_responses.log", mode='w')
logger200form = logging.Formatter("%(name)s %(asctime)s %(levelname)s %(message)s")
logger200hand.setFormatter(logger200form)
logger200.addHandler(logger200hand)

loggerNo200hand = logging.FileHandler("bad_responses.log", mode='w')
loggerNo200form = logging.Formatter("%(name)s %(asctime)s %(levelname)s %(message)s")
loggerNo200hand.setFormatter(loggerNo200form)
loggerNo200.addHandler(loggerNo200hand)

loggerNoResphand = logging.FileHandler("blocked_responses.log", mode='w')
loggerNoRespform = logging.Formatter("%(name)s %(asctime)s %(levelname)s %(message)s")
loggerNoResphand.setFormatter(loggerNoRespform)
loggerNoResp.addHandler(loggerNoResphand)

for site in sites:
    try:
        response = rq.get(site, timeout=3)
        if response.status_code == 200:
            logger200.info(response)
    except Exception:
        if rq.exceptions.ReadTimeout:
           print("Time out")
           loggerNoResp.warning(response)
           pass
        loggerNo200.error(response)
        pass
    print(response)