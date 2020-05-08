#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
*** Script para gestionar las herramientas para el Hand Tracker ***

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.

Iván Rodríguez (irodrigu@ull.es) - 2020
'''

from datetime import datetime
from matplotlib import pyplot as plt

# Declaración de funciones

def log_msg(info_type,msg):
    ''' Función para mostrar los logs del sistema por pantalla '''
    now = datetime.now()
    dt_string = now.strftime("[%d/%m/%Y %H:%M:%S] ") # Creamos el mensaje que queremos guardar
    f_msg = dt_string+"["+info_type+"]"+" "+msg
    print(f_msg)

# Declaración de clases

class trackedObj:
  ''' Clase para registrar los datos del tracking realizado por el leap motion'''
  def __init__(self):
    self.frame_id = 0
    self.timestamp = 0
    self.hands_count = 0
    self.extended_fingers = 0
    self.hand_type = ["N","N"]
    self.first_hand_pos = [0,0,0]
    self.second_hand_pos = [0,0,0]

    self.data_plot = False
    self.figure = 0
    self.ax = 0
    self.line_x_y = 0

  def show_data(self):
    ''' Función para mostrar toda la información guardada en la clase '''
    print("Frame ID: {}, Timestamp: {}, Hands Count: {}, Extended Fingers: {}, Hand Type: {}, First Hand Pos: ({},{},{}), Hand Type: {}, Second Hand Pos: ({},{},{})".format(self.frame_id, self.timestamp, self.hands_count, self.extended_fingers, self.hand_type[0], self.first_hand_pos[0],self.first_hand_pos[1],self.first_hand_pos[2], self.hand_type[1], self.second_hand_pos[0],self.second_hand_pos[1],self.second_hand_pos[2]))

  def update_data(self, tracking_results):
    ''' Función para actualizar los datos del track '''
    parameters = tracking_results.split()

    if (len(parameters) == 4):
        # Caso para el cual no tenemos detección de ninguna mano
        self.frame_id = int(parameters[0])
        self.timestamp = int(parameters[1])
        self.hands_count = int(parameters[2])
        self.extended_fingers = int(parameters[3])
        self.hand_type = ["N","N"]
        self.first_hand_pos = [0,0,0]
        self.second_hand_pos = [0,0,0]

    elif (len(parameters) == 8):
        # Caso para el cual se detecta una mano
        self.frame_id = int(parameters[0])
        self.timestamp = int(parameters[1])
        self.hands_count = int(parameters[2])
        self.extended_fingers = int(parameters[3])
        self.hand_type = [str(parameters[4]),"N"]
        self.first_hand_pos = [float(parameters[5][1:-2]),float(parameters[6][:-2]),float(parameters[7][:-2])]
        self.second_hand_pos = [0,0,0]

    elif (len(parameters) == 12):
        # Caso para el cual se detectan dos manos
        # Caso para el cual se detecta una mano
        self.frame_id = int(parameters[0])
        self.timestamp = int(parameters[1])
        self.hands_count = int(parameters[2])
        self.extended_fingers = int(parameters[3])
        self.hand_type = [str(parameters[4]),str(parameters[8])]
        self.first_hand_pos = [float(parameters[5][1:-2]),float(parameters[6][:-2]),float(parameters[7][:-2])]
        self.second_hand_pos = [float(parameters[9][1:-2]),float(parameters[10][:-2]),float(parameters[11][:-2])]

  def plot(self):
   ''' Función para representar la localización espacial de la detección '''

   if (self.data_plot == False):
       # Creamos el gráfico la primera vez
       plt.ion()

       self.figure = plt.figure()
       self.ax = self.figure.add_subplot(111)

       self.ax.set_title("Localización XY")
       self.ax.set_xlim(-200,200)
       self.ax.set_ylim(-200,200)

       self.line_x_y, = self.ax.plot(self.first_hand_pos[0],self.first_hand_pos[1], 'ro')

       self.data_plot = True

   else:
       self.line_x_y.set_xdata(self.first_hand_pos[0])
       self.line_x_y.set_ydata(self.first_hand_pos[1])

       self.figure.canvas.draw()
       self.figure.canvas.flush_events()
