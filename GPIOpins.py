import time
import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306
import Adafruit_LSM303
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

RST = 26 #Pins
DC = 23
SPI_PORT = 0
SPI_DEVICE = 0

# LSM303, Library, Display
lsm303 = Adafruit_LSM303.LSM303()
disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST, i2c_address=0x3d)

disp.begin()
disp.clear()
disp.display()

width = disp.width
height = disp.height
image = Image.new('1', (width, height))
draw = ImageDraw.Draw(image)
font = ImageFont.load_default()

while True:
    # For black clear image
    draw.rectangle((0,0,width,height), outline=0, fill=0)
    # Read/Print X, Y, Z
    accel, mag = lsm303.read()
    # Grab the X, Y, Z components; read/print
    accel_x, accel_y, accel_z = accel
    mag_x, mag_y, mag_z = mag
    print('Accel X={0}, Accel Y={1}, Accel Z={2}, Mag X={3}, Mag Y={4}, Mag Z={5}'.format(
          accel_x, accel_y, accel_z, mag_x, mag_y, mag_z))
    draw.text((0, 0),     ("x: " + str(accel_x)),  font=font, fill=255)
    draw.text((0, 25),    ("y: " + str(accel_y)),  font=font, fill=255)
    draw.text((0, 50),    ("z: " + str(accel_z)),  font=font, fill=255)
    # 1/4 sec repeat
    disp.image(image)
    disp.display()
    time.sleep(0.25)
