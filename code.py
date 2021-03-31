#wrapper
def enqueue(coda, elemento):
    coda.append(elemento)

def dequeue(coda):
    return coda.pop(0)

def main():
    queue = ["a","b","c","d"]
    enqueue(queue, "z")
    print(queue)
    x = dequeue(queue)
    print(x)
    print(queue)
    x = dequeue(queue)
    print(x)
    print(queue)

if __name__ == "__main__":
    main()    