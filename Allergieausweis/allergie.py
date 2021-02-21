# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 19:44:23 2021

@author: annag
"""

import csv
import random

import os

path = os.path.dirname(__file__)

# Name

vocals = 'aeiou'

cons = 'bcdfghjklmnpqrstvwxyz'


def fname():
    w1 = random.choice(cons)
    w2 = w1 + random.choice(vocals)
    w3 = w2 + random.choice(cons)
    w4 = w3 + random.choice(vocals)
    w5 = w4 + random.choice(cons)
    return w5


# Geburtstag

numbers = list(range(1, 29))
months = ['Januar', 'Februar', 'Marz', 'April', 'Mai', 'Juni',
          'Juli', 'August', 'September', 'Oktober', 'November', 'Dezember']


def fdate():
    geburi = str(random.choice(numbers)) + '. ' + random.choice(months)
    return geburi


# Medikamenteneinnahme

#ljn = [['ja'], ['nein']]

def fmedi():
    jn = random.choice([0, 1])
    return jn


# Blutgruppe

lbg = ['A', 'B', 'AB', '0']


def fblut():
    bg = random.choice(lbg)
    return bg

# list of allergies


def fallergien():
    with open("/".join([path, 'allergien.csv']), newline='') as g:
        reader1 = csv.reader(g)
        lallergies = list(reader1)
    nallergies = random.choice([1, 2, 2, 2, 3, 3])
    allergies = []
    for i in range(0, nallergies):
        allergies = allergies + random.choice(lallergies)
    return allergies

# Ausweisnummer


def fnummer():
    numb = random.randint(10000, 99999)
    return numb


# Ausstellungsland

def fland():
    with open("/".join([path, 'staaten.csv']), newline='') as f:
        reader = csv.reader(f)
        print(reader)
        lcountries = list(reader)
    aland = random.choice(lcountries)
    return aland


# Generiere Ausweise

# 4, 6 oder 8 Ausweise

nausw = 4
#nausw = 6
#nausw = 8

# XXX wie daten für ausweis speichern, wie allergien (versch. längen)?

# Fragen
"""
#Name, Geburi, Medi, BG, Allergien, Ausweisnr, Land
def ausweise(nausw):
    names = [fname(), fname(), fname(), fname()]
    geburis = [fdate(), fdate(), fdate(), fdate()]
    medis = [fmedi(), fmedi(), fmedi(), fmedi()]
    bluts = [fblut(), fblut(), fblut(), fblut()]
    nummers = [fnummer(), fnummer(), fnummer(), fnummer()]
    return names, geburis, medis, bluts, nummers
    
"""

# names, geburis, medis, bluts, nummers = ausweise(nausw)


def create_person():
    person = {'name': fname(), 'geburi': fdate(), 'medis': fmedi(),
              'bg': fblut(), 'nummer': fnummer(), 'allergien': fallergien(), 'land': fland()}
    return person


def create_uswiise(nausw):
    return [create_person() for i in range(nausw)]



# Eine Antwort richtig

# n1 = random.choice(nummers)
# print('In welchem Land wurde der Allergieausweis mit der Ausweisnummer ' +
#       str(n1)+' ausgestellt?')


# keine Antwort richtig

# rbg = random.choice(lbg)
# print('Welche Person nimmt Medikamente ein und hat zudem die Blutgruppe'+str(rbg)+'?')
