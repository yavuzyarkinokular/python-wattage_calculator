import time


def hesaplama(deger):
    x = 13.69
    return x / deger


while True:
    deger_alma = float(input("Send OHM value:\n"))
    print("İdeal Watt Değeriniz {} 'dır.".format(hesaplama(deger_alma)))
    print("********************************************")
    time.sleep(3)
    break
