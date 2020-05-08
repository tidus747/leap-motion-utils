#!/bin/bash

echo "Iniciando el servicio leapd"
sudo killall -9 leapd # Eliminamos todos los procesos anteriores relacionados con el servicio
sudo leapd & # Ejecutamos el servicio para que pueda funcionar el tracker
echo "Servicio iniciado"

echo "Iniciando el código del handTracker"
sleep 10 && python3 handTracker.py # Ejecutamos el tracker
