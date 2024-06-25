from .deviceLibs.visaDevices import get_visa_list
from .deviceLibs.picoDevices import get_pico_list
from .deviceLibs.serialDevices import get_serial_list


def list_all_devices():
    """
    Returns a list of all available devices.

    This function retrieves a list of devices by calling three different functions:
    - get_visa_list(): Retrieves a list of devices using VISA communication.
    - get_pico_list(): Retrieves a list of devices using Pico communication.
    - get_serial_list(): Retrieves a list of devices using serial communication.

    The devices from all three functions are combined into a single list and returned.

    Returns:
        devices (list): A list of all available devices.
    """
    devices = []
    devices += get_visa_list()
    devices += get_pico_list()
    devices += get_serial_list()

    return devices
# © AIMA DEVELOPPEMENT 2024