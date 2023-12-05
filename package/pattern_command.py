import re


'''  VOID LINE  '''
void_line    = r'([\s]+)|\n'


'''  COMMENTI SORGENTE  '''
commento     = r"(\s*\/\/.*)(\n|$)"


''' TYPE STR, NUM '''
CASE_STR  = r'(\s*"[^"]*")\s*'   # (\s*"[^"]*")
CASE_NUM  = r'\s*(\d+)\s*'       # (\d+)
CASE_VAR  = r'([A-Za-z_][\w_]*)' # variabile
CASE_END  = r'(\n*)'             # (\n*)
OR        = r'|'                 # |


case_num_var = f'({CASE_NUM}{OR}{CASE_VAR})'

''' ESPRESSIONI MATEMATICHE '''
CASE_EXPRESSION_ONLY_NUMBER = r'\s*\d+\s*([\-\+\*\%\/]\s*\d+\s*)*'
CASE_EXPRESSION = r'\s*' + case_num_var + '+\s*([\-\+\*\%\/]\s*' + case_num_var + '+\s*)*'

three_case      = f'(({CASE_STR})|({CASE_EXPRESSION})|({CASE_VAR}))'


'''  ASSEGNAZIONE VARIABILI  '''
prima_parte      = r"([A-Za-z_][\w\_]*)"
seconda_parte    = r"(\s*=\s*)"
terza_parte      = r'' + three_case

assegnazione_var = prima_parte + seconda_parte + terza_parte


'''  PRINT STDOUT  '''

stdout = r'\s*print\(\s*' + f'{three_case}+\s*(\,\s*{three_case}+)*' + '\s*\)' + f'({commento})*\s*\n*' 


if __name__ == "__main__": # usato per test regex
    if re.fullmatch(stdout, 'print(ciao,ciao, 12, 12+18) + 14 //coao // c8a9a9'):
        print("valid syntax")
    else:
        print("syntax not valid")
