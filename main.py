from parser import analyze
from scanner import scan
from generate_scanner import create
from parsed_productions import analyze_productions
import os, sys, subprocess

def open_file(filename):
    if sys.platform == "win32":
        os.startfile(filename)
    else:
        opener = "open" if sys.platform == "darwin" else "xdg-open"
        subprocess.call([opener, filename])

def main():
    archivo = input("Ingrese el nombre del archivo a provar --> ")
    
    input_file = open("./input/" + archivo)

    data = input_file.read()
    input_file.close()

    name, characters, keywords, tokens, productions = scan(data)
    code = analyze_productions(productions, tokens, keywords)

    final_dfa, dfas = analyze(name, characters, keywords, tokens)

    create(final_dfa, dfas, name, code)
    
if __name__ == "__main__":
    main()