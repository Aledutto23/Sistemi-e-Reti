def push_(pila, elemento):
    pila.append(elemento)

def pop_(pila):
    return pila.pop()    


def parentesi(input_str):
  stack = []
  for parentesi in input_str:
    if parentesi == '(':
      stack.append(parentesi)
    else:
      if parentesi == '[':
        stack.append(parentesi)
      else:
        if parentesi == '{':
          stack.append(parentesi)

      if not stack:
        print(input_str, "non valido")
        return
      else:
        top = stack[-1]
        if parentesi == ')':
          stack.pop()
        else:
          if parentesi == ']':
            stack.pop() 
          else:
            if parentesi == '}':
              stack.pop()  
  if not stack:
    print(input_str, "giusto")
  else:
    print(input_str, "sbagliato")




def main():
    stringa = input("inserire la stringa\n")
    parentesi(stringa)

    
if __name__ == "__main__":
    main()



