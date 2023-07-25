''' type hints untuk fungsi '''

# bentuk standar fungsi yang udah kita pelajar

'''
studi kasus
def fungsi(parameter):
    hasil = parameter**2
    print(hasil)

fungsi(1)
fungsi("agit")
fungsi(True)
'''

# penggunaan type hints

import string

def fungsi_dengan_hints(argument:int):
    ''' fungsi dengan hints '''
    output = 10**argument
    return

HASIL = fungsi_dengan_hints(20)
print(HASIL)

def display(argument:string):
    print(argument)

display("ucup")










