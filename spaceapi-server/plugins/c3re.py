
from spaceapi_server import plugins
import os

@plugins.template_function
def example_function(name: str):
    """
    This function is registered as a Jinja2 function.  It can be used like this:
    {{ example_function('the Spanish Inquisition') }}
    """
    stream = os.popen('mosquitto_sub -u c3re -P ***REMOVED*** -h ***REMOVED*** -t "c3re/hhdst" -C 1')
    output = stream.read()
    """
    return f'Nobody expects {name}'
    """
    return output.replace('\n','')

@plugins.template_function
def c3re_get_doorstatus():
    stream = os.popen('mosquitto_sub -u c3re -P ***REMOVED*** -h ***REMOVED*** -t "c3re/hhdst" -C 1')
    output = stream.read().replace('\n','')

    return output == "1"

@plugins.template_function
def c3re_get_clubraumtemp():
    stream = os.popen('mosquitto_sub -u c3re -P ***REMOVED*** -h ***REMOVED*** -t "c3re/clubraumtemp" -C 1')
    output = stream.read().replace('\n','')

    return float(output)

@plugins.template_function
def c3re_get_werkstatt():
    stream = os.popen('mosquitto_sub -u c3re -P ***REMOVED*** -h ***REMOVED*** -t "c3re/werkstatttemp" -C 1')
    output = stream.read().replace('\n','')

    return float(output)

@plugins.template_function
def example_config_function():
    """
    This function demonstrates the use of configuration.
    {( example_config_function() }}
    """
    # Config lookup example.  A plugin's config should be below
    # `.plugins[plugin_name]` (JSONPath)

    # Get the .plugins.example dict
    conf = plugins.get_plugin_config('example')
    # Get the .test_value property from the plugin config, falling
    # back to a default value
    return conf.get('test_value', 'the Spanish Inquisition')
