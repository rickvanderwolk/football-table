# football table

## Warning

***Please always shutdown the Pi gracefully to prevent the SD card from getting corrupted.***

`sudo shutdown -h now`

***Sounds are currently missing in this repository, I will add them later.***

## Index

- [Start game](#start-game)
- [Reset game](#reset-game)
- [Troubleshooting](#troubleshooting)
- [Setup a new Raspberry Pi](#setup-a-new-raspberry-pi)
- [Development](#development)

<a name="start-game"></a>
## Start game

1. Power on Pi (plug in extension cord)
2. Open the terminal with `ctrl` + `alt` + `t` or connect via ssh. For example: `ssh voetbaltafel@192.168.1.103`. Password is `voetbaltafel`.
3. Setup display port `export DISPLAY=:0`
4. Navigate to project `cd ~/Documents/voetbaltafel/`
5. Start script `python main.py`

<a name="reset-game"></a>
## Reset game

The game will be reset once one of the teams reaches a score of 10.

<a name="troubleshooting"></a>
## Troubleshooting

### No sound

Make sure sound is set to headphone jack output (not auto or HDMI)

`sudo raspi-config`

Navigate to `System Options` > `Audio` > select headphone output (probably 0).

### No UI

`export DISPLAY=:0`

<a name="setup-a-new-raspberry-pi"></a>
## Setup a new Raspbery Pi

### 1. install Raspberry Pi OS

Install Raspberry Pi OS on a micro SD card, https://www.raspberrypi.com/software/

### 2. Setup wizard

Place micro SD card in Pi and complete setup wizard

- Recommended: set language to `English` and keyboard to `US`
- Set both username and password as `voetbaltafel`
- Recommended: Connect to a Wi-Fi network for SSH connection later

### 3. Change defaults

3a. Recommended: Enable SSH

3b. Reboot

`sudo reboot`

3c. Change startup sequence 
  
`sudo nano /etc/xdg/lxsession/LXDE-pi/autostart`

Add the following:
```
@xset s noblank
@xset s off
@xset -dpms
```

3d.Recommended: Install additional fonts

`sudo apt-get install ttf-mscorefonts-installer`

3e. Reboot

`sudo reboot`

### 4. Deploy code to Pi

Deploy files to Pi with scp. For example:

`scp -r ./voetbaltafel voetbaltafel@192.168.1.103:~/Documents`

<a name="start-development"></a>
## Development

Currently aimed at development on macOS. 

Problems using Python on macOS?
See https://opensource.com/article/19/5/python-3-default-mac
I used Python 3.9.10

### 1. Install GPIO emulator

`pip install git+https://github.com/nosix/raspberry-gpio-emulator`

or

`pyenv exec pip install git+https://github.com/nosix/raspberry-gpio-emulator`

### 2. Install pygame

`pip install pygame`

or

`pyenv exec pip install pygame`
