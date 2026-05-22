import tkinter as tk
import time
import random
import os

canvas_width = 500
canvas_height = 700

meteoroids = 10
a = 0
pos = [0,0]
damage = 0
lives = 5
starting_time = time.time()
def main():
    root = tk.Tk()
    root.title("Meteoroid Game")
    root.geometry('500x800')
    C = tk.Canvas(root,width = canvas_width,height = canvas_height,bg = "black")
    C.pack()
    #elements
               
    ship = C.create_rectangle(0,canvas_height-200,20,canvas_height-180,fill = "red")
    
    #action    print(2)
    def shower(lim):
        beams = []
        meteo = []
        def beam(x,y):

            col = ["red","yellow","blue","white","green"]
            return C.create_rectangle(x,y,x+2,y+10,fill = col[1],outline = "gold")
        
        class barage:
            def __init__(self,index):
                self.index = index
            def rain(self):
                global damage
                damage_0 = damage
                C.move(beams[self.index],0,1)
                root.after(5,self.rain)
                if len(C.coords(beams[self.index]))==4:
                    x1,y1,x2,y2 = C.coords(beams[self.index])
                else:
                    x1,y1,x2,y2 = 0,0,0,0
                #print(x1,y1,x2,y2)
                
                #print(C.coords(beams[self.index]))
                x = pos[0]
                y = pos[1]

                if y == y1 or y == y2:
                    if x1 >= x and x1<= x+20:

                        #print("case 1a")
                        damage += 1
                        os.system("echo 1a >> stat")
                        self.boom(beams[self.index])
                    elif x2 >= x and x2<= x+20:

                        #print("case 1b")
                        damage += 1
                        os.system("echo 1b >> stat")
                        self.boom(beams[self.index])
                    else: 
                        pass
                if x == x1 or x == x2 :
                    if y1 >= y and y1 <= y+20:
                        #print("case 2a")
                        damage += 1
                        os.system("echo 2a >> stat")
                        self.boom(beams[self.index])


                    elif y2 >= y and y2 <= y+20:
                        #print("case 2b")
                        damage += 1
                        os.system("echo 2b >> stat")
                        self.boom(beams[self.index])
                    else:
                        pass
                increament = damage - damage_0 
                #if increament > 0:
                    ##print(damage,increament,damage_0)
                    #damage_0 =damage

            def boom(self,a):
                global points
                global lives
                lives -= 1
                #C.coords(a,0,0,0,0)
                C.delete(a)
                print(f"Lives remaining:",lives)
                if lives == 0:
                    ending_time = time.time()
                    points = round((ending_time - starting_time)*250)

                    C.delete('all')
                    
                    C.create_text(canvas_width/2, canvas_height/2,text = f"Points: {points}",font=("Arial",24),fill = "yellow")        
                    os.system(f"echo {points} >> points_record")
                    
            def mouse(event):
                global pos
                x = event.x
                y = event.y
                stage_y = canvas_height - 200
                pos[0] = x
                pos[1] = stage_y
                C.coords(ship,x,stage_y,x+20,stage_y+20)
                 
            root.bind("<Motion>", mouse)                
                 
                
        for i in range(meteoroids):
                x = random.randint(1,canvas_width)
                y = -1 * random.randint(lim*500,(lim+1)*500)
                #print(x,y)
                beams.append(beam(x,y))
        #beams[i]=beam(x,y)
        for i in range(10):
                meteo.append(barage(i))
                meteo[i].rain()

    for i in range(10):
        shower(i)
    root.mainloop()

#    print("Points:",points) 
if __name__ == "__main__":
    main()
