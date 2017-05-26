Raspberry Pi + Google Assistant SDK
===============================================
### (With Sound & Automatic Turn On)

An extension of the basic Google Assistant + Raspberry Pi demo with instructions
for automatically turning it on with the Raspberry Pi and to provide audio
feedback when the user talks to the device.



**Step 0: Setup Assistant on Pi**
- Follow
https://developers.google.com/assistant/sdk/prototype/getting-started-pi-python/
- Clone this repo in the home directory.


**Step 1: Install audio library**

Run `sudo apt-get install sox libsox-fmt-all`

**Step 2: Startup script**

Make a script called `startup.sh` with the following content.


```bash
#!/bin/bash

echo "Running Google Assistant…"
source env/bin/activate
python /home/pi/PiAssistant/assistant.py &

```

**Step 3: Run the script on startup**
- To schedule a task on reboot we need a GUI for Corn, install it using `sudo apt-get install gnome-schedule`. Read more [here](https://www.raspberrypi.org/documentation/linux/usage/cron.md).
- Execute `crontab -e` and add the following two lines at the end of the file – one for setting the volume to a desirable level and another to start the assistant.

```bash
amixer set Master 80%
@reboot sleep 10 && /usr/bin/zsh -e "/home/pi/startup.sh"
```

- If you do not know the name of the device (Master in the example) run `amixer` to get the name of the device and set a volume you want the Pi to boot up with.
- Use the terminal client of your choosing, i prefer having zsh.
