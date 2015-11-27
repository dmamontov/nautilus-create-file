Nautilus create File
====================

Adds a context menu item Nautilus 'Create new file'

## Requirements
* python3-gi
* python-nautilus
* zenity

## Installation

#### Debian or Ubuntu
```bash
sudo apt-get install python3-gi python-nautilus zenity
mkdir -p ~/.local/share/nautilus-python/extensions
cd ~/.local/share/nautilus-python/extensions
wget https://raw.githubusercontent.com/dmamontov/nautilus-create-file/master/nautilus-create-file.py
nautilus -q
```
#### Fedora
```bash
sudo yum provides libcairo2 libgirepository1.0_1 libglib2.0_0 python3 python-gi-common python3-cairo girepository-GLib2.0
sudo yum install python3-3.3.0-1.fc18.i686 python3-cairo-1.10.0-4.fc18.i686 python3-3.3.0-1.fc18.i686 nautilus-python zenity
mkdir -p ~/.local/share/nautilus-python/extensions
cd ~/.local/share/nautilus-python/extensions
wget https://raw.githubusercontent.com/dmamontov/nautilus-create-file/master/nautilus-create-file.py
nautilus -q
```
