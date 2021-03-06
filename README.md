# rigstarter
Manager program for your mining rig. Manual reboot through the use of  a gui with buttons and messages about the status of your gpus. Auto quick reboot in case of crash of the system. No root access needed.

The rigstarter is a program i made while trying to fix my seldom pc crash while mining. While still i am not sure exactly what is happening, auto reboot is surely the method to restart your rig work as soon as possible.

Whats new in version 0.1
In the first release there is a minimal gui which gives the actual status of your system (2 gpus support at the moment) and in case one gpu crash the system will auto reboot without waiting the miner (LOLminer, Redteamniner, Phoenixminer, etcetera) to give the reboot signal to the os.

HOW TO USE (For Manjaro only at the moment but should work with other distros as well)

-Install TK:
pacman -S tk

-Put the main.py script into the folder of your miner (or whatever directory)

-Launch the console with right click, then terminal. Once inside simply input: python main.py

-In order to make this auto-bootable open the menu 'Session and startup', add in Application Autostart tab a new application with name 'rigstarter' and command 'python /pathofscript/'.

