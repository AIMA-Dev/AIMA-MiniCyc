from .deviceLibs.visaDevices import get_visa_list
from .deviceLibs.picoDevices import get_pico_list
from .deviceLibs.serialDevices import get_serial_list

def list_all_devices():
    devices = []
    devices += get_visa_list()
    devices += get_pico_list()
    devices += get_serial_list()

    return devices
# Développé avec ❤️ par : www.noasecond.com.