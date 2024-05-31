import pyvisa

def list_connected_devices():
    rm = pyvisa.ResourceManager()
    devices = rm.list_resources()
    
    lan_devices = []
    for device in devices:
        if 'TCPIP' in device:
            lan_devices.append(device)
    
    return lan_devices

def get_device_info(device):
    rm = pyvisa.ResourceManager()
    dev = rm.open_resource(device)
    info = dev.query('*IDN?')
    dev.close()
    
    return info

def get_visa_list():    
    device_list = []
    for device in list_connected_devices():
        device_info = get_device_info(device)
        device_list.append(device_info + device)
    return device_list
# Développé avec ❤️ par : www.noasecond.com.