
from spaceapi_server import plugins
from shlex import quote
import os


host = os.environ.get("MQTT_HOST")
user = os.environ.get("MQTT_USER")
pw = os.environ.get("MQTT_PASSWORD")

@plugins.template_function
def c3re_get_doorstatus():
    stream = os.popen('mosquitto_sub -u ' + quote(user) + ' -P ' + quote(pw) + ' -h ' + quote(host) + ' -t "c3re/hhdst" -C 1')
    output = stream.read().replace('\n','')

    return output == "1"

@plugins.template_function
def c3re_get_clubraum_temp():
    stream = os.popen('mosquitto_sub -u ' + quote(user) + ' -P ' + quote(pw) + ' -h ' + quote(host) + ' -t "c3re/clubraumtemp" -C 1')
    output = stream.read().replace('\n','')

    return float(output)

@plugins.template_function
def c3re_get_werkstatt_temp():
    stream = os.popen('mosquitto_sub -u ' + quote(user) + ' -P ' + quote(pw) + ' -h ' + quote(host) + ' -t "c3re/werkstatttemp" -C 1')
    output = stream.read().replace('\n','')

    return float(output)
