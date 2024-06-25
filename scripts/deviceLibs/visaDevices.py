import pyvisa


def list_connected_devices():
    """
    Returns a list of connected LAN devices using the pyvisa library.

    Returns:
        list: A list of LAN devices connected to the system.
    """
    rm = pyvisa.ResourceManager()
    devices = rm.list_resources()

    lan_devices = []
    for device in devices:
        if 'TCPIP' in device:
            lan_devices.append(device)

    return lan_devices


def get_device_info(device):
    """
    Retrieves the identification information of a given device.

    Parameters:
    device (str): The address or name of the device.

    Returns:
    str: The identification information of the device.

    """
    rm = pyvisa.ResourceManager()
    dev = rm.open_resource(device)
    info = dev.query('*IDN?')
    dev.close()

    return info


def get_visa_list():
    """
    Retrieves a list of connected VISA devices.

    Returns:
        device_list (list): A list of device information for each connected VISA device.
    """
    device_list = []
    for device in list_connected_devices():
        device_info = get_device_info(device)
        device_list.append(device_info + device)
    return device_list


def Connect(self, rsrcMgr, rsrcString, timeout, doIdQuery, doReset, doClear):
    """
    Connects to a resource using the given resource manager and resource string.

    Args:
        rsrcMgr (ResourceManager): The resource manager object.
        rsrcString (str): The resource string specifying the resource to connect to.
        timeout (float): The timeout value in seconds.
        doIdQuery (int): Flag indicating whether to perform an ID query.
        doReset (int): Flag indicating whether to perform a reset.
        doClear (int): Flag indicating whether to clear the instrument.

    Returns:
        None
    """
    self.myInstr = rsrcMgr.open_resource(rsrcString)
    if doIdQuery == 1:
        print(self.QueryCmd("*IDN?"))
    if doReset == 1:
        self.SendCmd("reset()")
    if doClear == 1:
        self.myInstr.clear()

    self.myInstr.timeout = timeout
    return


def Disconnect(self):
    """
    Disconnects the instrument by closing the connection.

    Returns:
        None
    """
    self.myInstr.close()
    return


def SendCmd(self, cmd):
    """
    Sends a command to the instrument.

    Args:
        cmd (str): The command to send.

    Returns:
        None
    """
    if self.echoCmd == 1:
        print(cmd)
    self.myInstr.write(cmd)
    return


def QueryCmd(self, cmd):
    """
    Sends a query command to the instrument and returns the response.

    Args:
        cmd (str): The command to send to the instrument.

    Returns:
        str: The response from the instrument.

    """
    if self.echoCmd == 1:
        print(cmd)
    return self.myInstr.query(cmd)