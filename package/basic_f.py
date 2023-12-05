from ansic import *
import ansic


import pattern_command as ptc
import registro as rg
import calc


import nltk
import platform
import argparse
import re
import os



def stdout(stri:str) -> int:
    tokens = nltk.word_tokenize(stri)
    x = 0 # contatore parentesi, serve per capire quante parentesi ci sono all'interno della funzione print
    for element in tokens:
        if element != "print":
            
            if x > 0 and element != ")" and element != ",":
                if element in rg.var_register: 
                    print(rg.var_register[element])

                if re.fullmatch(ptc.CASE_EXPRESSION_ONLY_NUMBER, element):
                    print(calc.main(element))
                    

            if element == '(':
                x += 1

            if element == ')' and x != 0:
                x =- 1
                if x == 0:
                    break
    return EXIT_SUCCESS
