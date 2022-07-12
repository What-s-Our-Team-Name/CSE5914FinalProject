#!/bin/bash
sudo apt update
sudo apt install python3-pip python3-dev build-essential libssl-dev libffi-dev python3-setuptools
sudo apt install python3-venv

python3 -m venv /root/CSE5914FinalProject/venv
. /root/CSE5914FinalProject/venv/bin/activate

pip install -r /root/CSE5914FinalProject/requirements.txt