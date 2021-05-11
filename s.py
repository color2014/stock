import requests
import time
import json
url = "https://www.okex.com/api/v5/market/ticker?instId=SHIB-USDT"
proxies = {
    'https': 'http://127.0.0.1:10809',
}
headers = { 'Connection': 'close',}
requests.packages.urllib3.disable_warnings()
requests.adapters.DEFAULT_RETRIES = 1
if __name__ == "__main__":
    while True:
        try:
            #time.sleep(0.1) # 0.1秒查一次
            time.sleep(0.3)    # 每1秒更新一次
            response = requests.get(url, proxies=proxies,headers=headers,verify=False,timeout=5)
            json_data=json.loads(response.text)
            response.close()
            del(response)
            price = json_data.get("data",{"last":"check your internet"})[0].get("last",0)
            if price=="check your internet":
                print("check your internet")
            else:
                print("{:0<4d}".format(int(price.replace(".",""))),end="\r")
        except Exception as e:
            time.sleep(2)


