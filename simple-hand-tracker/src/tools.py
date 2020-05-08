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

def log_msg(info_type,msg):
    ''' Función para mostrar los logs del sistema por pantalla '''
    now = datetime.now()
    dt_string = now.strftime("[%d/%m/%Y %H:%M:%S] ") # Creamos el mensaje que queremos guardar
    f_msg = dt_string+"["+info_type+"]"+" "+msg
    print(f_msg)
