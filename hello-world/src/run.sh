#!/bin/bash

echo "Iniciando el servicio leapd"
sudo leapd &
echo "Servicio iniciado"

echo "Iniciando el código Hello World"
./Sample
