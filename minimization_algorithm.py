def minimize_dfa(n, alphabet, finals, transitions):
    # Se crea una tabla (matriz) para almacenar si el par (i, j) (con i < j)
    # ha sido marcado como distinguible.
    mark = [[False for _ in range(n)] for _ in range(n)]
    # Paso 1: Marcar como distinguibles a aquellos pares en los que uno es final y el otro no.
    for i in range(n):
        for j in range(i+1, n):
            if ((i in finals and j not in finals) or (i not in finals and j in finals)):
                mark[i][j] = True

def main():
    if int(input("Ingrese el formato de la entrada (1 para archivo, 2 para consola): ")) == 1:
        input_file = "predeterminated_input.txt" # Se lee la entrada desde el archivo "predeterminated_input.txt"
        with open(input_file, 'r') as f:
        # Se ignoran líneas en blanco
           lines = [line.strip() for line in f if line.strip()]
        index = 0
    
        # Número de casos
        cases = int(lines[index])
        index += 1
        for _ in range(cases):
            # Número de estados
            n = int(lines[index])
            index += 1
            # Alfabeto (lista de símbolos)
            alphabet = lines[index].split()
            index += 1
            # Estados finales (convertir a enteros)
            finals = list(map(int, lines[index].split()))
            index += 1
            # Se leen las n líneas de la tabla de transición.
            transitions = []
            for _ in range(n):
                row = list(map(int, lines[index].split()))
                index += 1
                transitions.append(row)
            # Se calcula la minimización y se obtienen los pares equivalentes.
            eq_pairs = minimize_dfa(n, alphabet, finals, transitions)
            # Se formatea la salida: cada par se muestra como "i,j"
            output = " ".join(f"({i},{j})" for (i, j) in eq_pairs)
            print(output)
    else:
        cases = int(input("Ingrese el número de casos: "))
        for _ in range(cases):
           n = int(input("Ingrese el número de estados: "))
           alphabet = input("Ingrese el alfabeto: ").split()
           finals = list(map(int, input("Ingrese los estados finales: ").split()))
           transitions = []
           for i in range(n):
               while True:
                row = list(map(int, input(f"Transición {i} (Empiece con {i}): ").split()))
                if len(row) != len(alphabet) + 1:
                    print("Error: la fila de transición excede el número de posibles transiciones de acuerdo al alfabeto. Inténtelo de nuevo.")
                else:
                    transitions.append(row)
                    break
           eq_pairs = minimize_dfa(n, alphabet, finals, transitions)
           output = " ".join(f"({i},{j})" for (i, j) in eq_pairs)
           print(output)

if _name_ == "_main_":
    main()
