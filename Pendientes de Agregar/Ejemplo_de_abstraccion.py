#!/usr/bin/env python
# -*- coding: utf-8 -*-
# A continuación se te presenta un ejemplo de como aplicar el término de abstracción 
# al crear la clase Vehículo.
#  
#  
class Vehículo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self._velocidad = 0  # Este es un atributo "privado" que no debería modificarse directamente

    def acelerar(self, incremento):
        self._velocidad += incremento
        print(f"La aceleración es de: la velocidad actual es {self._velocidad} km/h")

    def frenar(self, decremento):
        self._velocidad -= decremento
        print(f"El dato para frenar: la velocidad actual es {self._velocidad} km/h")

# Uso de la clase Vehículo
mi_vehículo = Vehículo("Toyota", "Corolla")
mi_vehículo.acelerar(70)
mi_vehículo.frenar(5)

