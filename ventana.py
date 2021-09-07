from tkinter import * 
from PIL import  Image,ImageTk
import  requests
from io import BytesIO
import  pokebase as pb


class root:
    def __init__(self):
        self.title="POKEDEX"
        self.size="600x700"
        self.resiable=False
        self.icon='icono.ico'


    def search(self):
        self.details.delete('1.0',END)
        #search a pokemon
        self.pokemon=pb.pokemon(self.poke_inp.get())
        try:
            #request
            self.response=requests.get(self.pokemon.sprites.front_default)
            self.image=ImageTk.PhotoImage(Image.open(BytesIO(self.response.content)))
            self.pokemon_image.config(image=self.image)
            self.pokemon_image.image=self.image
            self.abilities = ''
            self.types= ''
            for self.ability in self.pokemon.abilities:
                self.abilities += self.ability.ability.name + ', '

            for poketype in self.pokemon.types:
                self.types += poketype.type.name + ', '



            self.data=f"""{self.poke_inp.get().capitalize()}
            \nHeight:{self.pokemon.height}
            \nWeight:{self.pokemon.weight}
            \nAbilities:{self.abilities}
            \nType:{self.types}
         
         
            """
            self.details.insert(END,self.data)

                


        except  AttributeError:
            self.details.insert(END,"Not a valid pokemon try again")
            self.pokemon_image.config(image='')


    
    def cargar(self):
        self.ventana=Tk()
        self.ventana.title(self.title)
        self.ventana.iconbitmap(self.icon)
        
        self.ventana.geometry(self.size)
        self.ventana.resizable(0,0)
        self.logo="logo.png"
        self.img=ImageTk.PhotoImage(Image.open(self.logo))
        self.banner=Label(self.ventana,image=self.img)
        self.banner.image=self.img
        self.banner.pack()
        
        self.label2=Label(self.ventana,text="Enter the name of pokemon", fg="red",pady=20,font=("Ubuntu",18))
        self.label2.pack()

        self.poke_inp=Entry(self.ventana,font=('Ubuntu',18))
        self.poke_inp.pack(pady=20)

        self.but=Button(self.ventana,bd='4',text="Submit",fg="red",bg="yellow",command=self.search)
        self.but.pack()

        self.pokemon_image=Label(self.ventana)
        self.pokemon_image.pack(pady=30)

        self.details=Text(self.ventana,font=("Ubuntu",12),bg='light yellow')
        self.details.pack()


        self.ventana.mainloop()

    
    






