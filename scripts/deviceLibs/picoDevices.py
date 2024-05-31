from pico_sdk import PicoDevice

def get_pico_list():
    device_list = []
    found = PicoDevice.enumerate()
    for device in found:
        device_list.append(
            "PicoScope " + device.variant + " with serial " + device.serial)
    return device_list
# Développé avec ❤️ par : www.noasecond.com.