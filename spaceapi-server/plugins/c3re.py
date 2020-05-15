
from spaceapi_server import plugins
from shlex import quote
import os


host = os.environ.get("MQTT_HOST")
user = os.environ.get("MQTT_USER")
pw = os.environ.get("MQTT_PASSWORD")
topic_doorstatus = os.environ.get("MQTT_TOPIC_DOORSTATUS")
topic_clubraumtemp = os.environ.get("MQTT_TOPIC_CLUBRAUM")
topic_werkstatttemp = os.environ.get("MQTT_TOPIC_WERKSTATT")


@plugins.template_function
def c3re_get_doorstatus():
    stream = os.popen('mosquitto_sub -u ' + quote(user) + ' -P ' + quote(pw) + ' -h ' + quote(host) + ' -t ' + quote(topic_doorstatus) + ' -C 1')
    output = stream.read().replace('\n','')

    return output == "1"

@plugins.template_function
def c3re_get_clubraum_temp():
    stream = os.popen('mosquitto_sub -u ' + quote(user) + ' -P ' + quote(pw) + ' -h ' + quote(host) + ' -t ' + quote(topic_clubraumtemp) + ' -C 1')
    output = stream.read().replace('\n','')

    return float(output)

@plugins.template_function
def c3re_get_werkstatt_temp():
    stream = os.popen('mosquitto_sub -u ' + quote(user) + ' -P ' + quote(pw) + ' -h ' + quote(host) + ' -t ' + quote(topic_werkstatttemp) + ' -C 1')
    output = stream.read().replace('\n','')

    return float(output)
