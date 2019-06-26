'''
Prototype for a Redfish module for Salt
'''

import requests, json

__virtualname__ = 'redfish'


def __virtual__():
    return True

def system_details():
    data = requests.get('https://%s/redfish/v1/Chassis/System.Embedded.1' % __opts__['redfish']['host'], verify=False, auth=(__opts__['redfish']['user'], __opts__['redfish']['pwd'])).json()
    return data

def system_property(property):
    data = system_details()
    if property in data.keys():
        return data[property]
    else:
        return False

def set_property(property, value):
    '''
    This is currently only known to work for setting the IndicatorLED like this:
    
    .. code-block:: bash
    
        salt-call redfish.set_property IndicatorLED "Blinking"
        salt-call redfish.set_property IndicatorLED "'Off'"

    The double quotes are required for the "Off" property because otherwise it will be interpreted as a Python "False"!
    '''
    
    payload = {property: value}
    headers = {'content-type': 'application/json'}
    response = requests.patch(
        'https://%s/redfish/v1/Chassis/System.Embedded.1' % __opts__['redfish']['host'],
        data=json.dumps(payload),
        headers=headers,
        verify=False,
        auth=(__opts__['redfish']['user'], __opts__['redfish']['pwd']))
    return response.__dict__
 

