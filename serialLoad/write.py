import serial
ser = serial.Serial(
         port='/dev/ttyS0',
         baudrate =62500 ,
         parity=serial.PARITY_NONE,
         stopbits=serial.STOPBITS_ONE,
         bytesize=serial.EIGHTBITS,
         timeout=1
)
#counter=0
for counter in range(0,10):
    data="A59977744F".encode('utf-8')
    ser.write(data[counter])
    #time.sleep(1)
    #counter += 1
