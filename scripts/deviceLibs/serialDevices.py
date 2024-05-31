import serial
import serial.tools.list_ports

def get_serial_list():
    ports = serial.tools.list_ports.comports()
    available_ports = []
    for port in ports:
        available_ports.append(port.device)
    return available_ports
# Développé avec ❤️ par : www.noasecond.com.