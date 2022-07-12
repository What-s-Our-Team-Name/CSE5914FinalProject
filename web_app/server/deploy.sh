#!/bin/bash
cp /root/CSE5914FinalProject/web_app/server/chatbot.service /etc/systemd/system/chatbot.service
sudo systemctl daemon-reload
pkill chatbot
sudo systemctl start chatbot