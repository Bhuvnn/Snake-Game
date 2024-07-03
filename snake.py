from turtle import Turtle
starting=[(0,0),(-20,0),(-40,0)]
class Snake:
    
    
    def __init__ (self):
        self.turtles=[]
        self.create_snake()
        self.head=self.turtles[0]
        
        
    def create_snake(self):
        
        for i in starting:
           self.add_square(i) 
    
    def add_square(self,position):
        turtle=Turtle()
        turtle.shape("square")
        turtle.penup()
        turtle.color("white")
        turtle.goto(position)
        self.turtles.append(turtle)
    

    def move(self):
        for post in range(len(self.turtles)-1,0,-1):
            new_x=self.turtles[post-1].xcor() 
            new_y=self.turtles[post-1].ycor()
            self.turtles[post].goto(new_x,new_y)
        self.turtles[0].forward(20)
    
    def reset(self):
        for i in self.turtles:
            i.goto(1000,1000)
        self.turtles.clear()
        self.create_snake()
        self.head=self.turtles[0]
    
    

    def extend(self):
        self.add_square(self.turtles[-1].position())


    def up(self):
        self.turtles[0].setheading(90)
        
    def down(self):
        self.turtles[0].setheading(270)
        
    def left(self):
        self.turtles[0].setheading(180)
        
    def right(self):
        self.turtles[0].setheading(0)
    
        

