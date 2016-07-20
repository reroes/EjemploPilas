#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2016 René Elizalde - @reroes <reroes799[AT]utpl[DOT]edu.ec>
#
# Distributed under terms of the GPLv3+ license.

"""

"""

import pilasengine

pilas = pilasengine.iniciar()

sonido1 = pilas.sonidos.cargar('chimes.wav')
sonido2 = pilas.sonidos.cargar('camera.wav')
sonido3 = pilas.sonidos.cargar('applause.wav')

sonido1.reproducir()
sonido2.reproducir()
sonido3.reproducir()

