#!/bin/bash

echo "Iniciando el servicio leapd"
sudo leapd &
echo "Servicio iniciado"

echo "Iniciando el código Hello World"
python3 handTracker.py
