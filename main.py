import turtle
import random

#setup game screen

game = turtle.Screen()
game.setup(800,600)
game.tracer(0)
game.bgcolor(.1,.1,.1)
game.title("Ping Pong By Mohammed Ahmad Raafat")

#setup center line
line = turtle.Turtle()
line.color("white")
line.shape("square")
line.penup()
line.goto(0,0)
line.shapesize(0.1,30)

#setup ball
ball = turtle.Turtle()
ball.speed(0)
ball.color("red")
ball.shape("circle")
ball.shapesize(1,1)
ball.penup()
ball.goto(0,0)

#setup player 1
p1 = turtle.Turtle()
p1.speed(0)
p1.color("white")
p1.shape("square")
p1.shapesize(1,8)
p1.penup()
p1.goto(0,230)

#setup player 2
p2 = turtle.Turtle()
p2.speed(0)
p2.color("white")
p2.shape("square")
p2.shapesize(1,8)
p2.penup()
p2.goto(0,-260)

#setup score 1
score1 = turtle.Turtle()
score1.penup()
score1.goto(-320,270)
score1.color("white")
score1.write("Player score : 0", align="center", font=("Arial",14,"normal"))
score1.hideturtle()

#setup score 2
score2 = turtle.Turtle()
score2.penup()
score2.goto(-320,-290)
score2.color("white")
score2.write("Player score : 0", align="center", font=("Arial",14,"normal"))
score2.hideturtle()

#Movements
player_speed = 80

def p1_left():
  p1.setx(p1.xcor() - player_speed )

def p1_right():
  p1.setx(p1.xcor() + player_speed )

def p2_left():
  p2.setx(p2.xcor() - player_speed )

def p2_right():
  p2.setx(p2.xcor() + player_speed )


game.listen()
game.onkeypress(p1_left, "a")
game.onkeypress(p1_right, "d")
game.onkeypress(p2_left, "Left")
game.onkeypress(p2_right, "Right")

xr = 1
xl = 1

p1score , p2score = 0,0 

colors = ["red" ,"blue" ,"green", "yellow", "white", "pink"]

while 1 == 1:
    game.update()
    
    ball.sety(ball.ycor()+xl)
    ball.setx(ball.xcor()+xr)
    
    if ball.xcor() == 380:
      xr *= -1
    elif ball.xcor() == -380:
      xr *= -1
    elif ball.ycor() > 210 and ball.ycor() < 240 and ball.xcor() < p1.xcor()+80 and ball.xcor() > p1.xcor()-80:
      xl *= -1
      ball.color(random.choice(colors))
    elif ball.ycor() < -250 and ball.ycor() > -280 and ball.xcor() < p2.xcor()+80 and ball.xcor() > p2.xcor()-80:
      xl *= -1
      ball.color(random.choice(colors))
    elif ball.ycor() > 380:
      ball.goto(0,0)
      xl*=-1
      xr*=random.choice([1,-1])
      p2score+=1
      score2.clear()
      score2.write(f"Player score : {p2score}", align="center", font=("Arial",14,"normal"))
    elif ball.ycor() < -380:
      ball.goto(0,0)
      xl*=-1
      xr*=random.choice([1,-1])
      p1score+=1
      score1.clear()
      score1.write(f"Player score : {p1score}", align="center", font=("Arial",14,"normal"))

