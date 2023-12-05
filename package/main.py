from ansic import *
import ansic

import pattern_command as ptc
import registro as rg
import basic_f


import platform
import argparse
import re
import os



def analisi(row):

    if re.match(ptc.commento, row) != None: # caso row commento
        return EXIT_SUCCESS

    elif re.match(ptc.void_line, row) != None: # caso row void
        return EXIT_SUCCESS

    elif re.fullmatch(ptc.assegnazione_var, row) != None: # ! assegnazione var !
        rg.assegna(row)
        return EXIT_SUCCESS

    elif re.fullmatch(ptc.stdout, row) != None: #caso sys-write in stdout
        basic_f.stdout(row)
        return EXIT_SUCCESS

    else:
        return EXIT_FAILURE


def main(argv:object):
    try:
        with open(argv.sorgente) as sorgente:
            counter = 0
            for row in sorgente:
                counter += 1
                if analisi(row) != EXIT_SUCCESS:
                    perror(f"errore! comando non riconosciuto a riga {counter} --> {row}")
                    return EXIT_FAILURE
        print(rg.var_register)
        return EXIT_SUCCESS

    except Exception as e:
        perror(e)
        return EXIT_FAILURE


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('sorgente', type = str)  # /sorgente.txt

    argv = parser.parse_args()
    result = main(argv)
    printf(f"uscita dal programma con valore: {result}")
    ansic._exit(result)
