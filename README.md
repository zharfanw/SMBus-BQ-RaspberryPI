# SMBus-BQ-RaspberryPI
## Using For Raspberry PI with custom GPIO I2C
With GPIO8 as SDA, and GPIO7 as SCL you can add in `/boot/config.txt` with text below
```
dtoverlay=i2c-gpio,bus=3,i2c_gpio_delay_us=10,i2c_gpio_sda=17,i2c_gpio_scl=27
```
using `i2c_gpio_delay_us=10` to slow down clock required maximum Smart Battery SMBUS 
and for check i2c address, can try `i2cdetect -y 3`. using Bus 3 because have define above
