## Steps:
- Install RASPBIAN STRETCH LITE
    + https://www.raspberrypi.org/downloads/raspbian/
- first time that you log in typpe this user name and password.
    + raspberrypi login: pi
    + Password: raspberry
- Install python:
    + $ apt-get update
    + $ sudo apt-get install python3-picamera
- Install PIP:
    + $ sudo apt-get install python-pip
- Install python control librery.
    + With python packages manager:
        * sudo pip install RPi.GPIO
            - Link: https://raspberrypi.stackexchange.com/questions/8220/how-to-correctly-install-the-python-rpi-gpio-library
- Install git in debein:
        *  sudo apt-get install git-core
           - Link: https://www.digitalocean.com/community/tutorials/how-to-install-git-on-debian-8
- Set up wifi
    + Change the file in "/etc/network/interfaces.d" with.
            '''
            auto lo
 
            iface lo inet loopback
            iface eth0 inet manual
    
            allow-hotplug wlan0
            auto wlan0
 
 
            iface wlan0 inet manual
                wpa-ssid "DC"
                wpa-psk "5124223639"

            '''    
- Conect remotly to raspberry pi with IP addres.
    + This option if you only have terminal
        * Install putty:
            - Link: https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html
        * Enable SSH inside of the raspberry pi:
            - sudo '''raspi-config'''
            - Select '''Interfacing Options'''
            - Navigate to and select '''SSH'''
            - Choose '''Yes'''
            - Select '''Ok'''
        * Get rasberry IP address
        * place this IP addres inside of putty and then press yes.
        * You need to introduce password and Username 

    + This option if you have a GUI install.
        * Get the IP address of the raspberry pi
        * Install VNC
            - Link: https://www.realvnc.com/en/connect/download/viewer/
        * Then run
            - sudo apt-get update
            - sudo apt-get install realvnc-vnc-server realvnc-vnc-viewer
            - sudo raspi-config
                + enable VNC Server by doing the following:
                    * Navigate to Interfacing Options.
                    * Scroll down and select VNC > Yes.
    + If you only want to control the 

## Importan commands and information:
- Shoutdown rasberrypi:
    + sudo shutdown -h now
- Reboot rasberrypi:
    + sudo reboot -h now
- Git IP address:
    + hostname -I
- IP addres:
    + 10.0.0.116
- change rasberry pi configurationsL
    + sudo raspi-config


## Investigate
- How do I acces rasberry pi with IP address?
- How do I set an IP addres?
    + /etc/hostname
        * link: https://www.raspberrypi.org/documentation/remote-access/ip-address.md
## Important link:
- Interesting tutorial: https://learn.sparkfun.com/tutorials/raspberry-gpio
- Setting rasbery py with ubuntu: https://developer.ubuntu.com/core/get-started/installation-medias
    + Note: after unpackages change ".img" for ".iso"
        * Note: in windows unable "file name extentions" to be able to see the extentions.

- Loging and pasword:
    + UserName: deepcast || pi  
    + Passwor: ai

