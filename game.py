import tkinter as tk
import time
import random
import os

canvas_width = 500
canvas_height = 700

#bullets/meteors
meteoroids = 2

bullet_width = 8
bullet_height = 15
uy = 90
ay = 30
#wtf is 'a'?
a = 0
hitbox_posx = [0,0]
damage = 0
lives = 5
#flag for level up purpose
flag = 0
MAX_LEVEL = 10
def main():
    root = tk.Tk()
    root.title("Meteoroid Game")
    root.geometry('500x800')
    C = tk.Canvas(root,width = canvas_width,height = canvas_height,bg = "black")
    C.pack()
    #elements
               
    ship = C.create_rectangle(0,canvas_height-200,60,canvas_height-180,fill = "red")
    print("Total lives: 5") 
    class bullets:
            def __init__(self,level):
                self.starting_time = time.time()
                self.level = level
                
            def time_passed(self):
                self.t = time.time() - self.starting_time
                return self.t
            def bullet_initial_position(self):
                level = self.level
                self.xy0 = [random.randrange(1,canvas_width),-1 * random.randint(0,500)
]
                x1,y1 = self.xy0
                x2,y2 = x1 + bullet_width, y1 + bullet_height
                color = ["red","yellow","green","blue"]
                self.bullet = C.create_rectangle(x1,y1,x2,y2,fill="yellow")
                #print(self.xy0)
            def flow(self):
                global flag,hitbox_posx
                level = self.level
                x1 = self.xy0[0]
                #
                t = self.time_passed()
                y = self.xy0[1]
                y1 = y + uy*t + 0.5*(self.level+1)*ay*(t**2) #extra fun
                #y1 = y + uy*t + 0.5*ay*(t**2)
                #
                x2,y2 = x1 + bullet_width, y1 + bullet_height
                C.coords(self.bullet,x1,y1,x2,y2+level*3)
                if y1>=canvas_height-200 and y1<canvas_height-180:
                    if ( x1 >= hitbox_posx[0] and x1<= hitbox_posx[1] ) or ( x2 >= hitbox_posx[0] and x2<= hitbox_posx[1] ):
                        print("Damage ",end="")
                        C.delete(self.bullet)
                        print("dealt")

                if y1 <= canvas_height:

                    root.after(20,self.flow)

                else:
                    flag += 1
                    #print(flag)
                    if level <= MAX_LEVEL and flag == meteoroids:
                        print(f"level {level} completed!")
                        flag = 0
                        roundx(level+1)
            def rain(self):
                self.bullet_initial_position()
                self.flow()


            def survive(event):
                x = event.x
                C.coords(ship,x,canvas_height-200,x+60,canvas_height-180)
                hitbox_posx[0] = x
                hitbox_posx[1] = x+60
                
            root.bind("<Motion>", survive) 
    def roundx(level):
        for i in range(meteoroids):
            obj = bullets(level)
            obj.rain()
    roundx(0)
    root.mainloop()

#    print("Points:",points) 
if __name__ == "__main__":
    main()
