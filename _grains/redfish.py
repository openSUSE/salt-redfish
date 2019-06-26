'''
Prototype for Redfish grains for Salt
'''

import requests, json

GRAIN_MAP = {
    'AssetTag': 'AssetTag',
    'ChassisType': 'ChassisType',
    'Id':'Redfish_Id',
    'IndicatorLED': 'IndicatorLED',
    'Location': 'Redfish_Location',
    'Manufacturer': 'Manufacturer',
    'Model': 'Model',
    'Name': 'Redfish_Name',
    'PartNumber': 'PartNumber',
    'PowerState': 'PowerState',
    'SKU': 'SKU',
    'SerialNumber': 'Redfish_SerialNumber',
    'Status': 'Redfish_Health_Status',
    }

def grains():
    config = __opts__['redfish']
    data = requests.get('https://%s/redfish/v1/Chassis/System.Embedded.1' % config['host'], verify=False, auth=(config['user'], config['pwd'])).json()
    grain_dict = {}
    for grain in GRAIN_MAP.keys():
        if grain in data.keys():
            grain_dict[GRAIN_MAP[grain]] = data[grain]
    return grain_dict
