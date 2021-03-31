class Node:
    def __init__(self,data): #inizializzo il costruttore
        self.left = None
        self.right = None
        self.data = data
        
#stampa albero
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data)
        if self.right:
            self.right.PrintTree() 

    def insert(self,data):
#confronto il valore da aggiungere con il nodo corrente
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node (data)
                else:
                    self.left.insert (data)    
            elif data > self.data:
                if self.right is None:
                    self.right = Node (data)
                else:
                        self.right.insert(data)
        else:  
            self.data = data

           
#metodo di inserimento per aggiungere i nodi
root=Node(12)
root.insert(6)
root.insert(14)
root.insert(3)
root.PrintTree()