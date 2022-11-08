import turtle
import winsound
import datetime
from random import randint

class Game():
    player_speed = 20
    ball_speed = 450
    PLAYER_WIDTH = 1
    PLAYER_HEIGHT = 5

    #creating Player A
    player_a = turtle.Turtle()
    player_a.speed(0)
    player_a.shape("square")
    player_a.color("white")
    player_a.shapesize(stretch_wid=PLAYER_HEIGHT, stretch_len=PLAYER_WIDTH)
    player_a.penup()
    player_a.goto(-350,0)

    #creating Player B
    player_b = turtle.Turtle()
    player_b.speed(0)
    player_b.shape("square")
    player_b.color("white")
    player_b.shapesize(stretch_wid=PLAYER_HEIGHT, stretch_len=PLAYER_WIDTH)
    player_b.penup()
    player_b.goto(350,0)

    #creating ball
    ball = turtle.Turtle()
    ball.speed(0)
    ball.shape("square")
    ball.color("white")
    ball.penup()
    ball.goto(0,0)
    randomx = randint(0,1)
    randomy = randint(0,1)
    ball.dx = randomx if randomx == 1 else -1
    ball.dy = randomy if randomy == 1 else -1


    #creating punctuation text
    score_creating = turtle.Turtle()
    score_creating.speed(0)
    score_creating.color("white")
    score_creating.penup()
    score_creating.hideturtle()
    score_creating.goto(0,260)
    score_creating.write(f"Player A: 0  Player B: 0", align= "center", font=("Arial",24, "normal"))

    last_pa_render = datetime.datetime.now()
    last_pb_render = datetime.datetime.now()
    last_ball_render = datetime.datetime.now()
    ball_moving = True
    pa_has_ball = None

    def check_move_delay(self, last_render, speed):
        return datetime.datetime.now() > last_render + datetime.timedelta(milliseconds= 1000 / speed)

    def read_input(self, pressed_keys):

        def contains_key(key):
            return key in pressed_keys

        if contains_key("w"):
            self.player_a_up()
            
        elif contains_key("s"):
            self.player_a_down()

        if contains_key("Up"):
            self.player_b_up()

        elif contains_key("Down"):
            self.player_b_down()

        if self.ball_moving:
            return

        if self.pa_has_ball:
            self.ball.goto(self.player_a.xcor()+ 20,self.player_a.ycor() + (self.PLAYER_HEIGHT / 2))
        else:
            self.ball.goto(self.player_b.xcor()- 20,self.player_b.ycor() - (self.PLAYER_HEIGHT / 2))
        
        if not ((contains_key("d") and self.pa_has_ball) or (contains_key("Left") and not self.pa_has_ball)):
            return
        self.ball_moving = True
        if contains_key("s") or contains_key("Down"):
            self.ball.dy = -1
        elif contains_key("w") or contains_key("Up"):
            self.ball.dy = 1
                 

    def player_a_up(self):
        if not self.check_move_delay(self.last_pa_render, self.player_speed):
            return
        self.last_pa_render = datetime.datetime.now()    
        cord_y = self.player_a.ycor()
        cord_y +=20
        self.player_a.sety(cord_y)

    def player_a_down(self):
        if not self.check_move_delay(self.last_pa_render, self.player_speed):
            return
        self.last_pa_render = datetime.datetime.now()
        cord_y = self.player_a.ycor()
        cord_y -=20
        self.player_a.sety(cord_y)

    def player_b_up(self):
        if not self.check_move_delay(self.last_pb_render, self.player_speed):
            return
        self.last_pb_render = datetime.datetime.now()    
        cord_y = self.player_b.ycor()
        cord_y +=20
        self.player_b.sety(cord_y)

    def player_b_down(self):
        if not self.check_move_delay(self.last_pb_render, self.player_speed):
            return
        self.last_pb_render = datetime.datetime.now()  
        cord_y = self.player_b.ycor()
        cord_y -=20
        self.player_b.sety(cord_y)

    def movement_ball(self):
        if not self.check_move_delay(self.last_ball_render, self.ball_speed) or not self.ball_moving:
            return
        self.last_ball_render = datetime.datetime.now()  
        self.ball.setx(self.ball.xcor() + self.ball.dx)
        self.ball.sety(self.ball.ycor() + self.ball.dy)
        

    def sound(self):
        self.sound_collision = winsound.PlaySound("sound/bounce.wav", winsound.SND_ASYNC) 


    score_a = 0
    score_b = 0


    def ball_collision(self):

        if self.ball.ycor() > 290:
            self.ball.sety(290)
            self.ball.dy *= -1
            self.sound()

        if self.ball.ycor()<-290:
            self.ball.sety(-290)
            self.ball.dy *= -1
            self.sound()
        
        
        if (self.ball.xcor() < -340 and self.ball.xcor()> - 350) and (self.ball.ycor()< self.player_a.ycor()+50 and self.ball.ycor()> self.player_a.ycor()-50): 
            self.ball.setx(-340)
            self.ball.dx *=-1
            self.sound()

        if (self.ball.xcor() > 340 and self.ball.xcor()<350) and (self.ball.ycor()< self.player_b.ycor()+50 and self.ball.ycor()> self.player_b.ycor()-50): 
            self.ball.setx(340)
            self.ball.dx *=-1
            self.sound()
        
        if self.ball.xcor()>390:
            self.ball_moving = False
            self.pa_has_ball = False
            self.ball.dx *=-1
            self.score_a +=1
            self.score_creating.clear()
            self.score_creating.write(f"Player A: {self.score_a}  Player B: {self.score_b}", align= "center", font=("Arial",24, "normal"))
            self.sound()

        if self.ball.xcor()<-390:
            self.ball_moving = False
            self.pa_has_ball = True
            self.ball.dx *=-1
            self.score_b +=1
            self.score_creating.clear()
            self.score_creating.write(f"Player A: {self.score_a}  Player B: {self.score_b}", align= "center", font=("Arial",24, "normal"))
            self.sound()
        

    def players_collision(self):    
        if self.player_a.ycor()> 250:
            self.player_a.sety(250)

        if self.player_a.ycor()<-245:
            self.player_a.sety(-245)

        if self.player_b.ycor()> 250:
            self.player_b.sety(250)

        if self.player_b.ycor() <- 245:
            self.player_b.sety(-245)

