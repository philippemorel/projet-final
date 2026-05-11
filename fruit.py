

class Fruit() :
    
    def __init__(self, nom_fruit :str, fruit_type :str):
        self.nom_fruit = nom_fruit
        self.fruit_type = fruit_type

    def __str__(self):
        return f"Nom: {self.nom_fruit}, Type: {self.fruit_type}"
    
    def to_dict(self): 
        return {
            "nom_fruit" : self.nom_fruit,
            "fruit_type" : self.fruit_type
        }
    

    