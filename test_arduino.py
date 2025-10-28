import pyvisa

rm = pyvisa.ResourceManager("@py")
ports = rm.list_resources()
print(ports)

device = rm.open_resource(
    "ASRL28::INSTR", 
    read_termination="\r\n", 
    write_termination="\n"
)
identification = device.query("*IDN?")
print(identification)