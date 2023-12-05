from ansic import *
import ansic

import pattern_command as ptc
import calc

import re


'''
    modulo per la gestione dell'assegnazione delle variabili. Tutte le variabili sono contenute all'interno del dizionario
    variabili (a sinistra il dizionario contiene il nome della variabile e adestra il suo valore)
'''


var_register = {

}


def dividi(row:str) -> list:
    try:
        index = 0
        name_var = ""
        content_var = ""
        flag_ricordo = 0

        while row[index] != '=':
            if row[index] != " " and row[index] != "\t" and row[index] != "\n":
                name_var += row[index]
            index += 1
        
        index += 1

        while index < strlen(row):

            if row[index] == "\"" and flag_ricordo == 1:
                flag_ricordo = 0
                break

            if row[index] == "\"" and flag_ricordo == 0: #['b', '"ciaone"\n']
                flag_ricordo = 1

            if flag_ricordo == 1:
                content_var += row[index] 
            else:
                if row[index] != " " and row[index] != "\t" and row[index] != "\n":
                    content_var += row[index]
            index += 1

        return [str(name_var), str(content_var)]

    except Exception as e:
        perror(e)


def assegna(row:str) -> int:
        variabile_divisa:list = dividi(row)

        if re.fullmatch(ptc.CASE_EXPRESSION, variabile_divisa[1]):
            for element in var_register: # mi permette di identificare possibili variabili all'interno dell'esepressione matematica
                if element in variabile_divisa[1]: # se ci sono sostituisco il nome della variabile con il valore che rappresenta
                    variabile_divisa[1] = variabile_divisa[1].replace(element, str(var_register[element]))

            variabile_divisa[1] = calc.main(variabile_divisa[1]) # calcolo il risultato

        var_register[variabile_divisa[0]] = variabile_divisa[1]
        return EXIT_SUCCESS
