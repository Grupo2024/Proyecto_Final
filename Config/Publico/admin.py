# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.

from .models import *

#Si te fijas, la clase "Persona" no esta registrada en el admin, esto pasa xq es una clase abstracta
admin.site.register(Colegio)
admin.site.register(Delegado)
admin.site.register(Categoria)
admin.site.register(Equipo)
admin.site.register(Jugador)
admin.site.register(Estadisticas)
