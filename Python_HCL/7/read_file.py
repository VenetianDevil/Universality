#!/usr/bin/python
# -*- coding: iso-8859-2 -*-

def read():
    path = input() #file path
    while not path == 'KONIEC':
        try:
            file = open(path, 'r')
        except FileNotFoundError:
            print('Plik o podanej nazwie nie istnieje')
        else:
            try:
                number = int(input()) # row number
            except ValueError:
                print ('nie mozna wczytac takiego numeru wiersza')
            else:
                for i in range(1, number+1):
                    line = file.readline()

                if number < 1 or line == '':
                    print ('Nie ma takiego wiersza')
                    # raise ValueError
                else:
                    print (line)
        path = input()

read()

#INPUT
# file path [enter]
# row number

# KONIEC [enter]