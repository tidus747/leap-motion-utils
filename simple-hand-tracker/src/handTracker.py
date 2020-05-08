#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
*** Script para analizar los datos del tracking realizado por el programa en C++ ***

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

import keyboard, os, sys
import tools as t
from subprocess import Popen, PIPE

CPP_COMPILED_PATH = './handTracker' # Nombre que tiene el código fuente compilado

# Abrimos el tracker escrito en C++ una vez compilado
if (os.path.exists(CPP_COMPILED_PATH)):
    t.log_msg("INFO","Fichero ejecutable encontrado!")
    MyPopen = Popen([CPP_COMPILED_PATH], shell=True, stdout=PIPE, stdin=PIPE)
    # Creamos el objeto para los datos del tracking
    track = t.trackedObj()
else:
    t.log_msg("ERROR","Fichero ejecutable ("+CPP_COMPILED_PATH+") no encontrado!")
    sys.exit()

while(True):
  tracking_results = MyPopen.stdout.readline().strip()

  track.update_data(tracking_results.decode('ascii'))
  track.show_data()
  #track.plot()

  if (keyboard.is_pressed("ENTER")):
      # Si se pulsa ENTER se saldrá del programa
      t.log_msg("INFO","Saliendo del programa...")
      break
