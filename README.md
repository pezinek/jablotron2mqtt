# py-jablotron6x
Library for interfacing with Jablotron 6x alarms by using the JA-80T serial cable
via MQTT.

Setup:

```
LC_ALL=C virtualenv venv
. ./venv/bin/activate
pip install -r requirements.txt
```

Run:

```
. ./venv/bin/activate
./main.py
```

once is the mqtt bridge running you may check mqtt for incomming messages:

```
$ mosquitto_sub -h mqtt -t 'alarm/#' -v 
alarm/online 1
alarm/mode disarmed
alarm/leds/power 1
alarm/leds/blinking_lock 0
alarm/leds/lock 0
alarm/display   
alarm/raw ba ff
alarm/raw e7 08 11 23 19 48 1b 4e ff
alarm/raw b4 ff
alarm/raw e0 40 01 59 7f 00 7f ff
...
```

or emulate key presses on the alarm control panel:

```
mosquitto_pub -h mqtt -t alarm/key/press -m "F1"
```


More details about the [ja-6x protocol](https://github.com/pezinek/py-jablotron6x/wiki/Protocol) is in the wiki.
