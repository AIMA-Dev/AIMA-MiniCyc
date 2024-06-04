from pico_sdk import PicoDevice


def get_pico_list():
    """
    Retrieves a list of PicoScope devices connected to the system.

    Returns:
        list: A list of strings representing the PicoScope devices, each string
        contains the device variant and serial number.
    """
    device_list = []
    found = PicoDevice.enumerate()
    for device in found:
        device_list.append(
            "PicoScope " + device.variant + " with serial " + device.serial)
    return device_list

def get_pico_values():
    found = PicoDevice.enumerate()
    if len(found) == 0:
        return "No PicoScope devices found."
    
    device_id = found[0].device_id
    device = PicoDevice(device_id)
    device.open()
    device.set_channel("C1")
    device.set_samples(10)
    device.run()
    values = device.get_values()
    device.close()
    return values