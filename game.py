import tkinter as tk
import time
import random

canvas_width = 500
canvas_height = 700

#bullets/meteors
meteoroids = 10
bullet_width = 8
bullet_height = 15
uy = 90
ay = 30
hitbox_posx = [0,0]
#flag for level up purpose
flag = 0
damage = 0
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
            global damage
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
                global flag,hitbox_posx,uy
                global damage
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
                xc = x1 + bullet_width/2
                #needs a revisit
                if y1>canvas_height-200-0.2 and y1<canvas_height-180+0.2:
                    if xc >= hitbox_posx[0]-bullet_width/2 and x1<= hitbox_posx[1] +bullet_width/2 :
                        print("Damage ",end="")
                        C.delete(self.bullet)
                        time.sleep(0.05)
                        self.label.config(text=f"Score: {damage}")
                        #C.itemconfig(self.bullet,fill = "blue")
                        damage += 1
                        print("dealt")
                if y1 <= canvas_height:
                    root.after(20,self.flow)

                else:
                    flag += 1
                    if level <= MAX_LEVEL and flag == meteoroids:
                        print(f"level {level} completed!")
                        flag = 0
                        roundx(level+1)
            def rain(self):
                self.bullet_initial_position()
                self.flow()

            def survive(event):
                #x = event.x + 20
                #C.coords(ship,x,canvas_height-200,x+60,canvas_height-180)
                #hitbox_posx[0] = x
                #hitbox_posx[1] = x+60
                pass

            def goleft(event):
                x = C.coords(ship)[0] - 20
                y = C.coords(ship)[1] 
                C.coords(ship,x,y,x+60,y+20)
                hitbox_posx[0] = x
                hitbox_posx[1] = x+60

            def goright(event):
                x = C.coords(ship)[0] + 20
                y = C.coords(ship)[1] 
                C.coords(ship,x,y,x+60,y+20)
                hitbox_posx[0] = x
                hitbox_posx[1] = x+60

            def hi():
                x = C.coords(ship)[0] - 20
                y = C.coords(ship)[1] 
                C.coords(ship,x,y,x+60,y+20)
                hitbox_posx[0] = x
                hitbox_posx[1] = x+60
            def hello():
                x = C.coords(ship)[0] + 20
                y = C.coords(ship)[1] 
                C.coords(ship,x,y,x+60,y+20)
                hitbox_posx[0] = x
                hitbox_posx[1] = x+60
                
            root.bind("<Left>", goleft) 
            root.bind("<Right>", goright) 
            left_button=tk.Button(root, width = 10,text = "<=",command =hi )
            right_button=tk.Button(root, width = 10,text = "=>",command =hello)
            label = tk.Label(root,text = f"Score: {damage}")

            label.pack()
            
    def roundx(level):
        for i in range(meteoroids):
            obj = bullets(level)
            obj.rain()
        print(damage)
    roundx(0)


    bullets.left_button.pack(padx= 10, pady = 15,side = 'left')
    bullets.right_button.pack(padx= 10, pady = 15,side = 'right')
    root.mainloop()
if __name__ == "__main__":
    main()
