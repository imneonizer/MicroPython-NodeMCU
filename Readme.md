## MicroPython - NodeMCU

This repository contains my initial exploration on running MicroPython with NodeMCU. Read through and follow along all the steps to setup your own development environment and prototype quickly.

**Requirements**

- [NodeMCU ESP82261](https://www.amazon.in/gp/product/B07262H53W/ref=ppx_yo_dt_b_asin_title_o01_s00?ie=UTF8&psc=1)
- Ubuntu 18.04 or Later
- Python 3.7+

**Installing MicroPython**

In order to run python code, we need to install [MicroPython](https://docs.micropython.org/en/latest/) firmware first.

- Download firmware from [micropython.org](https://micropython.org/download/all/)

  ````
  wget "https://micropython.org/resources/firmware/esp8266-1m-20200902-v1.13.bin" -O esp8266-micropython.bin
  ````

- Install [esptool.py](https://pypi.org/project/esptool/) for flashing NodeMCU with latest firmware.

  ````
  pip install esptool
  ````

- Connect the device using Micro USB cable to your linux system and loot for `ttyUSB*` devices.

  ````
  ls /dev/ttyUSB*
  ````

  For me because I have only connected one board, it's `ttyUSB0`.

- Erase older firmware `esptool.py` should be already added to `$PATH` when you installed it using pip.

  ````
  esptool.py --port /dev/ttyUSB0 erase_flash
  ````

- Flash your NodeMCU

  ````
  esptool.py --port /dev/ttyUSB0 --baud 460800 write_flash --flash_size=detect 0 esp8266-micropython.bin
  ````

**Development Environment**

For developing and testing out ideas quickly we need to install few more tools.

1. [ampy](https://github.com/scientifichackers/ampy) is used for managing NodeMCU from host machine.

   ````
   pip install adafruit-ampy
   ````

2. [picocom](https://github.com/npat-efault/picocom) is used for accessing python terminal over USB serial port.

   ````
   sudo apt-get install picocom -y
   ````

3. Open up a terminal, and run below command for hassle free access.

   ````
   export AMPY_PORT=/dev/ttyUSB0
   export AMPY_BAUD=115200
   alias mcu="picocom -b $AMPY_BAUD $AMPY_PORT"
   ````

   You can also write these line in `~/.bashrc` file so that these alias can be accessible from any terminal.

**Basics of MicroPython**

1. The NodeMCU file system is very simple, it contains a `/boot.py` file which runs automatically to setup system configuration during boot. (you should not modify or delete this file)
2. The file of our interest is `main.py` which gets executed automatically when ever the MCU boots or reset, this is the entry point of our application. Initially this might not be already present.

**Basics of ampy**

Ampy is a command line tool which helps to interact with MicroPython running MCUs.

1. `ampy ls` to list all the files on NodeMCU file system.
2. `ampy get boot.py` to print contents of `boot.py` on MCU.
3. `ampy put main.py` to copy `main.py` from host system to MCU file system.
4. `ampy reset` to reset MCU board.

**Basics of Picocom**

Picocom is yet another helpful tool to connect to the NodeMCU MicroPython terminal directly.

````
picocom -b 115200 /dev/ttyUSB0
````

With this our setup and basic understanding of tool is complete, we can move forward to deploy our first hello world program.

**Hello World Program**

We will trigger the on board led on and off to confirm that our setup is working and we can deploy our code.

````python
# main.py

from machine import Pin
from time import sleep

led = Pin(2, Pin.OUT)

while True:
  print("led:", "on" if led.value() else "off")
  led.value(not led.value())
  sleep(0.5)
````

1. save this as `main.py` and copy the file to MCU using command `ampy put main.py` and press the `reset` button on board.

2. The led should start blinking on and of continuously.

3. Open another terminal and connect to the MCU terminal by executing below command

   ````
   picocom -b 115200 /dev/ttyUSB0
   ````

   Expected output:

   ````
   led: off
   led: on
   led: off
   .
   .
   .
   ````

   You can interrupt the current execution by pressing `ctrl+c` and you will enter into python shell, to restart the `main.py` file from same shell again you can press `ctrl+d`.

**Resources**

https://docs.micropython.org/en/latest/esp8266/tutorial/intro.html

https://randomnerdtutorials.com/getting-started-micropython-esp32-esp8266/