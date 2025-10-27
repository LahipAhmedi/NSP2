import pyvisa


rm = pyvisa.ResourceManager("@py")
ports = rm.list_resources()
print(ports)


