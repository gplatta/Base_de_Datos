# Código 11.8: puntajes_pickle.py: Módulo para guardar y recuperar puntajes en un archivo que usa pickle

#! /usr/bin/env python
# encoding: utf8

import pickle

def guardar_puntajes(nombre_archivo, puntajes):
        """ Guarda la lista de puntajes en el archivo.
        Pre: nombre_archivo corresponde a un archivo válido,
            puntajes corresponde a los valores a guardar
        Post: se guardaron los valores en el archivo en formato pickle.
        """

        archivo = open(nombre_archivo, "wb")
        pickle.dump(puntajes, archivo)
        archivo.close()

def recuperar_puntajes(nombre_archivo):
        """ Recupera los puntajes a partir del archivo provisto.
            Devuelve una lista con los valores de los puntajes.
        Pre: el archivo contiene los puntajes en formato pickle
        Post: la lista devuelta contiene los puntajes en el
            mismo formato que se los almacenó.
        """

        archivo = open(nombre_archivo, "rb")
        puntajes = pickle.load(archivo)
        archivo.close()
        return puntajes


valores = [("Pepe", 108, "4:16"), ("Juana", 2315, "8:42")]
guardar_puntajes("puntajes.dat", valores)
recuperado = recuperar_puntajes("puntajes.dat")
print (recuperado)