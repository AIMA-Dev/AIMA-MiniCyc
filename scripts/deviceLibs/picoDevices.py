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
# Développé avec ❤️ par : www.noasecond.com.
