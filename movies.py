import random
import operator
peliculas={}
class Movie:
    def __init__(self, name):
        self.name=name
        self.rank=random.randrange(10)
        
    def like(self):
        if self.rank < 10:
            self.rank += 1
            print("diste like, calificacion actualizada:",self.rank)
        else:
            self.rank = self.rank
        

    def dislike(self):
        if self.rank > 0:
            self.rank -= 1
            print("diste un dislike, lo sentimos calificacion actualiza :",self.rank)
        else:
            self.rank = self.rank
        
        
    def display(self):
        print("PELICULA:",self.name,"CALIFICACION:",self.rank)
    def guardan(self):
        
        return self.name
    def guardar(self):
        return self.rank
        
tiburon=Movie("tiburon")
tiburon.display()
peliculas[tiburon.guardan()]=tiburon.guardar()

aceventura=Movie("aceventura")
aceventura.display()
peliculas[aceventura.guardan()]=aceventura.guardar()


capitanam=Movie("Capitana Marvel")
capitanam.dislike()
capitanam.display()
peliculas[capitanam.guardan()]=capitanam.guardar()

shrek=Movie("shrek")
shrek.like()
shrek.display()
peliculas[shrek.guardan()]=shrek.guardar()

capitan_a=Movie("Capitan America")
capitan_a.display()
peliculas[capitan_a.guardan()]=capitan_a.guardar()

hulk=Movie("hulk")
hulk.display()
peliculas[hulk.guardan()]=hulk.guardar()



ironman=Movie("ironman")
ironman.display()

vengadores=Movie("vengadores")
vengadores.display()

batman=Movie("batman")
batman.display()

pokemon=Movie("pokemon")
pokemon.display()

pelis = sorted(peliculas.items(), key=operator.itemgetter(1))
print(pelis)