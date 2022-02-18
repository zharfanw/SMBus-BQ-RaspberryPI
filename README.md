# SMBus-BQ-RaspberryPI
## Using For Raspberry PI with custom GPIO I2C
With GPIO8 as SDA, and GPIO7 as SCL you can add in `/boot/config.txt` with text below
```
dtoverlay=i2c-gpio,bus=3,i2c_gpio_delay_us=1,i2c_gpio_sda=17,i2c_gpio_scl=27
```
