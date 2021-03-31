def push_(pila, elemento):
    pila.append(elemento)

def pop_(pila):
    return pila.pop()

def main():
    stack=[]
    parentesi = input("Inserire un insieme di parentesi: ")

    for elemento in parentesi:
        if elemento == '(' or elemento == '[' or elemento == '{':
         push_(stack, elemento)
        else:
            pos = stack[-1]
            if  (elemento == ')' and pos == '(' or elemento == ']' and pos == '[' or elemento == '}' and pos == '{'):
                    pop = pop_(stack)
                   
    if not stack:
        print("insieme giusta")
    else:
        print("insieme sbagliato")

if __name__ == "__main__":
    main()