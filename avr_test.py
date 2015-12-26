import smbus, struct

bus = smbus.SMBus(1)
DEVICE_ADDRESS = 0x45

def read_uint16(bus, addr):
    bus.write_byte(DEVICE_ADDRESS, addr)
    low = bus.read_byte(DEVICE_ADDRESS)
    bus.write_byte(DEVICE_ADDRESS, addr+1)
    high = bus.read_byte(DEVICE_ADDRESS)
    return (high<<8)+low

bus.write_byte(DEVICE_ADDRESS, 0)
print "fan set speed:\t\t%d" % bus.read_byte(DEVICE_ADDRESS)
print "fan period:\t\t%d" % read_uint16(bus, 1)

print "adc0 value:\t\t%d" % read_uint16(bus, 3)
print "adc1 value:\t\t%d" % read_uint16(bus, 5)
print "adc2 value:\t\t%d" % read_uint16(bus, 7)
print "adc3 value:\t\t%d" % read_uint16(bus, 9)
