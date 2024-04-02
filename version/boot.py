# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
#import webrepl
#webrepl.start()

from machine import Pin

def ledYak(pin):
    pin = Pin(pin, Pin.OUT)
    pin.on()
    
def ledSondur(pin):
    pin = Pin(pin, Pin.OUT)
    pin.off()

def do_connect():
    import network
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('connecting to network...')
        wlan.connect('SUPERONLINE_WiFi_5207', 'PC9LNHM7XL7E')
        while not wlan.isconnected():
            pass
    print('network config:', wlan.ifconfig())
