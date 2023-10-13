import paho.mqtt.client as mqtt
import RPi.GPIO as gpio
import requests
import re as r
from datetime import datetime as d
import math
import os
import random

sound_list = ["./rain1.wav", "./rain2.wav", "./rain3.wav", "./rain4.wav"]

msg_topic = str()
msg_msg = str()

pir = 21

gpio.setmode(gpio.BCM)
gpio.setup(pir, gpio.IN)

mqtt_sub = ["distance"]
ip_address = "192.168.110.202"

mqttc = mqtt.Client()

NX = 149            # X축 격자점 수
NY = 253            # Y축 격자점 수

Re = 6371.00877     #  지도반경
grid = 5.0          #  격자간격 (km)
slat1 = 30.0        #  표준위도 1
slat2 = 60.0        #  표준위도 2
olon = 126.0        #  기준점 경도
olat = 38.0         #  기준점 위도
xo = 210 / grid     #  기준점 X좌표
yo = 675 / grid     #  기준점 Y좌표
first = 0

if first == 0 :
    PI = math.asin(1.0) * 2.0
    DEGRAD = PI/ 180.0
    RADDEG = 180.0 / PI

    re = Re / grid
    slat1 = slat1 * DEGRAD
    slat2 = slat2 * DEGRAD
    olon = olon * DEGRAD
    olat = olat * DEGRAD

    sn = math.tan(PI * 0.25 + slat2 * 0.5) / math.tan(PI * 0.25 + slat1 * 0.5)
    sn = math.log(math.cos(slat1) / math.cos(slat2)) / math.log(sn)
    sf = math.tan(PI * 0.25 + slat1 * 0.5)
    sf = math.pow(sf, sn) * math.cos(slat1) / sn
    ro = math.tan(PI * 0.25 + olat * 0.5)
    ro = re * sf / math.pow(ro, sn)
    first = 1

def mapToGrid(lat, lon, code = 0 ):
    ra = math.tan(PI * 0.25 + lat * DEGRAD * 0.5)
    ra = re * sf / pow(ra, sn)
    theta = lon * DEGRAD - olon
    if theta > PI :
        theta -= 2.0 * PI
    if theta < -PI :
        theta += 2.0 * PI
    theta *= sn
    x = (ra * math.sin(theta)) + xo
    y = (ro - ra * math.cos(theta)) + yo
    x = int(x + 1.5)
    y = int(y + 1.5)
    return x, y

def getWeather():

        retV = []

        find_V = ["POP", "PTY", "SKY"]
        append_V = [" 강수확률(POP): ", " 강수형태(PTY): ", " 하늘상태(SKY): "]
        last_V = ["%", "", ""]

        my_PTY = {"0":"없음", "1":"비", "2":"비/눈", "3":"눈", "4":"소나기"}
        my_SKY = {"1" : "맑음", "3" : "구름많음", "4" : "흐림"}

        time = d.now()
        now_h = str()
        if (time.hour > 0 and time.hour <= 2) or (time.hour <= 24 and time.hour > 23): now_h = "2300"
        elif time.hour > 2 and time.hour <= 5: now_h = "0200"
        elif time.hour > 5 and time.hour <= 8: now_h = "0500"
        elif time.hour > 8 and time.hour <= 11: now_h = "0800"
        elif time.hour > 11 and time.hour <= 14: now_h = "1100"
        elif time.hour > 14 and time.hour <= 17: now_h = "1400"
        elif time.hour > 17 and time.hour <= 20: now_h = "1700"
        elif time.hour > 20 and time.hour <= 23: now_h = "2000"

        realtime = str(time.hour) + "00"
        retV.append(realtime)

        now_d = str(time.date())
        now_d = ''.join([x for x in list(now_d) if x != '-'])


        x_n = 36.766615
        y_n = 127.282466

        nx, ny = mapToGrid(x_n, y_n)

        url = 'http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getVilageFcst'
        params = {'serviceKey' : 'JYVAfDor8zrqtfnqsihAVqSRYDQFh382sboRRIHQOFlvI5Beo/r6/0SWlywHrH3lSnGlJq64vn8LNpYVBGnDFg==', 'numOfRows' : '50', 'pageNo' : '1', 'dataType' : 'XML', 'base_date' : now_d, 'base_time' : now_h, 'nx' : str(nx), 'ny' : str(ny) }

        response = requests.get(url, params=params)
        response_str = response.content.decode('utf-8')

        cnt = 0

        # 강수 확률 추출
        for x in list(response_str.split('<items>')):
                if cnt >= 1:

                        for yp in x.split("</item>"):
                                for i in range(3):
                                        buf = []
                                        if len(r.findall(find_V[i], yp)) != 0:
                                                findall_result = r.findall(r'<fcstValue>[0-9]{2}</fcstValue>', yp) + r.findall(r'<fcstValue>[0-9]{3}</fcstValue>', yp) + r.findall(r'<fcstValue>[0-9]{1}</fcstValue>', yp)
                                                findall_time = r.sub(r'[^0-9]', '', (r.findall(r'<fcstTime>[0-9]{4}</fcstTime>', yp))[0])
                                                result_num = r.sub(r'[^0-9]', '', findall_result[0])
                                                if find_V[i] == "PTY": val = my_PTY[result_num]
                                                elif find_V[i] == "SKY": val = my_SKY[result_num]
                                                else: val = str(result_num)
                                                buf.append((val, str(findall_time) + append_V[i] + val + last_V[i]))
                                                retV.append(buf)
                cnt += 1

        return retV

def pir_state():
    if gpio.input(pir) == True:
        return "detected"
    else:
        return "nothing"

def on_connect(client, userdata, flags, rc):
        print("Connected with result code" + str(rc))
        mqttc.subscribe("distance")

def on_publish(client, userdata, mid):
        msg_id = mid

def on_message(client, userdata, msg):
        global msg_topic
        global msg_msg
        msg_topic = msg.topic
        msg_msg = list(str(msg.payload))
        msg_msg = [x for x in msg_msg if x.isdigit() or x == "."]
        msg_msg = ''.join(x for x in list(msg_msg))
        msg_msg = float(msg_msg)
        print("Topic:", msg_topic, " Message:", msg_msg)


mqttc.on_connect = on_connect
mqttc.on_publish = on_publish
mqttc.on_message = on_message

mqttc.connect(ip_address, 1883, 60)

try:
    while True:
        max_val = 0
        mqttc.loop()
        if msg_topic == "distance" and msg_msg <= 5.0:
                if pir_state() == "detected":
                        result = getWeather()
                        for i in result:
                                if i[0][0].isdigit():
                                        max_val = max(max_val, int(i[0][0]))
                        if max_val >= 0:
                                os.system("aplay " + sound_list[random.randrange(0, 3)])
                        print("yes")
                        msg_topic = None
                        msg_msg = None
        else:
                print("no")


except KeyboardInterrupt:
    mqttc.disconnect()
    print("finished")