producto = ["Coca Cola", "Asado 1kg", "Berenjena al Escaveche", "Galletas", "Alfajores"]
Efectivo = "Efectivo"
Transferencia = "Transferencia"
precio = [1500, 9000, 4600, 4000, 2000]
import time 
import streamlit as st


def buscar_posicion(lista, nombre):
    for i in range(len(lista)):
        if lista[i] == nombre:
            return i
    return -1

def aplicar_descuento(monto,forma_pago):
     if forma_pago == Efectivo:
          return round(monto - (monto * 10 / 100), 2)
     return monto

def calcular_iva(monto):
     return round(monto * 21 / 100, 2)