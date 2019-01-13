# jablotron2mqtt
Library for interfacing with Jablotron 6x alarms by using the JA-80T serial cable
via MQTT.

### Setup:


```
LC_ALL=C virtualenv venv
. ./venv/bin/activate
pip install -r requirements.txt
```

### Run:

```
. ./venv/bin/activate
jablotron2mqtt/main.py --serial-port /dev/ttyUSB0  --host mqtt
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

### Home Assistant:

eventually if you plan to controll your jablotron from [Home Assistant](https://home-assistant.io/) your configuration may look like this:

```
alarm_control_panel:
  - platform: mqtt
    name: jablotron
    state_topic: "alarm/mode"
    command_topic: "alarm/key/press"
    payload_disarm: !secret alarm_code
    payload_arm_home: "F1"
    payload_arm_away: !secret alarm_code
    availability_topic: "alarm/online"
    payload_available: "1"
    payload_not_available: "0"
```

More details about the [ja-6x protocol](https://github.com/pezinek/py-jablotron6x/wiki/Protocol) is in the wiki.
