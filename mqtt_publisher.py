import paho.mqtt.client as paho
import time

def on_publish(client, userdata, mid):
    print("mid: "+str(mid))
 

client = paho.Client(client_id="Publisher", clean_session=True, userdata=None, protocol=paho.MQTTv31)
client.on_publish = on_publish
client.connect(host="localhost", port=1883)
client.loop_start()

data = 0

while True:
    data += 1
    (rc, mid) = client.publish("topic_1", str(data), qos=1)
    time.sleep(5)