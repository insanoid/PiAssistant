Raspberry Pi + Google Assistant SDK With Sound & Always On
===============================================

Run `sudo apt-get install sox libsox-fmt-all` for Audio files.

## Run On Start

- Make a script called `startup.sh` with the following content.

```
#!/bin/bash

echo "Running Google Assistant…"
source env/bin/activate
python /home/pi/assistant/PiAssistant/assistant.py &

```
- Edit you `.bashrc` and add the following at the end of the file to set the volume and run the script on start.

```
amixer set Master 50%
zsh -e ~/startup.sh
```
Run `amixer` to get the name of the device and set a volume you want the Pi to start with.
Use the terminal client of your choosing.