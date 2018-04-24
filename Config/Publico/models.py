# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Persona(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    edad = models.IntegerField()
    dni = models.AutoField(primary_key=True)
    #Datos estandares de persona, estos van a ser heredados x cualquier jugador y/o delegado

    def __str__(self):
        return 'Persona: {} {}| edad: {}| dni: {}| '.format(self.nombre,
         self.apellido, self.edad, self.dni)

    class Meta:
        abstract = True


class Colegio(models.Model):   
    nombre = models.CharField(max_length=40)

    def __str__(self):
        return 'Nombre: {}'.format(self.nombre)


class Delegado(Persona):
    colegio = models.ForeignKey(Colegio)

    def __str__(self):
        return 'Colegio: {}'.format(self.colegio.nombre)
    #El delegado, aparte de tener todos los datos de persona, pertenece a un colegio, 
    # a la vez que un colegio tiene un delegado, tira un error al crear un colegio ya
    # que no existe delegado al cual estar relacionado, y no existe delegado por que para
    # crear este, se tiene que seleccionar un colegio 


class Categoria(models.Model):
    nombre = models.CharField(max_length=40)
    colegio = models.ForeignKey(Colegio)

    def __str__(self):
        return 'Categoria: {} del {}'.format(self.nombre, self.colegio.nombre)
    #Un colegio puede tener muchas categorias, asi lo defini aca, pero falta buscar 
    # la forma de hacer que un colegio solo pueda tener HASTA 3 categorias


class Equipo(models.Model):
    nombre = models.CharField(max_length=40)
    cantidad = models.IntegerField()
    categoria = models.ForeignKey(Categoria)#Una categoria tiene muchos equipos que juegan entre si

    def __str__(self):
        return 'Equipo: {} con {} jugadores, de la categoria: '.format(self.nombre,
         self.cantidad, self.categoria.nombre)


class Jugador(Persona):
    equipo = models.ForeignKey(Equipo)#Un equipo tiene muchas personas que lo conforman

    def __str__(self):
        return 'Nombre: {}'.format(self.nombre)



class Estadisticas(models.Model):
    cant_goles = models.IntegerField()
    partidos_jugados = models.IntegerField()
    partidos_ganados = models.IntegerField()
    partidos_empatados = models.IntegerField()
    cant_amarillas = models.IntegerField()
    cant_rojas = models.IntegerField()
    jugador = models.OneToOneField(Jugador)#Cada jugador tiene sus propias estadisticas 

    def __str__(self):
        return 'Jugador: {}'.format(self.jugador.nombre)


#ERROR IMPORTANTE:
#resolver lo de que no se puede crear un colegio xq no existe delegado y visceversa