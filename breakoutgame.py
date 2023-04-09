import turtle
import time
import random

# Set up the screen
screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Breakout Game")
screen.tracer(0)

# Create the paddle
paddle = turtle.Turtle()
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_wid=1, stretch_len=5)
paddle.penup()
paddle.goto(0, -250)

# Create the ball
ball = turtle.Turtle()
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 3
ball.dy = 3

# Create the bricks
bricks = []
for i in range(-200, 200, 50):
    for j in range(150, 250, 25):
        brick = turtle.Turtle()
        brick.shape("square")
        brick.color(random.choice(["red", "orange", "yellow", "green", "blue", "purple"]))
        brick.shapesize(stretch_wid=1, stretch_len=4)
        brick.penup()
        brick.goto(i, j)
        bricks.append(brick)

# Create the score
score = 0
score_text = turtle.Turtle()
score_text.hideturtle()
score_text.penup()
score_text.goto(-280, 260)
score_text.write(f"Score: {score}", align="left", font=("Courier", 14, "normal"))

# Create the game over text
game_over_text = turtle.Turtle()
game_over_text.hideturtle()
game_over_text.penup()
game_over_text.goto(0, 0)
game_over_text.write("GAME OVER", align="center", font=("Courier", 24, "normal"))
game_over_text.color("red")
game_over_text.hideturtle()

# Move the paddle left
def move_left():
    x = paddle.xcor()
    if x > -250:
        paddle.setx(x - 20)

# Move the paddle right
def move_right():
    x = paddle.xcor()
    if x < 250:
        paddle.setx(x + 20)

# Keyboard bindings
screen.listen()
screen.onkeypress(move_left, "Left")
screen.onkeypress(move_right, "Right")

# Main game loop
while True:
    screen.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Check for wall collisions
    if ball.xcor() > 290 or ball.xcor() < -290:
        ball.dx *= -1

    if ball.ycor() > 290:
        ball.dy *= -1

    if ball.ycor() < -290:
        game_over_text.showturtle()
        time.sleep(2)
        game_over_text.hideturtle()
        score = 0
        score_text.clear()
        score_text.write(f"Score: {score}", align="left", font=("Courier", 14, "normal"))

    # Check for paddle collision
    if ball.ycor() < -240 and (paddle.xcor() - 50 < ball.xcor() < paddle.xcor() + 50):
        ball.dy *= -1

    # Check for brick collisions
    for brick in bricks:
        if ball.distance(brick) < 40:
            ball.dy *= -1
            brick.goto(1000, 1000)
            bricks.remove(brick)
            score += 10
            score_text.clear()
            score_text.write(f"Score: {score}", align="left", font=("Courier", 14, "normal"))

    # Check for game over
    if len(bricks) == 0:
        game_over_text.write("YOU WIN!", align="center", font=("Courier", 24, "normal"))
        game_over_text.showturtle()
        time.sleep(2)
        game_over_text.hideturtle()
        score = 0
        score_text.clear()
        score_text.write(f"Score: {score}", align="left", font=("Courier", 14, "normal"))
        ball.goto(0, 0)
        ball.dx = 3
        ball.dy = 3
        for i in range(-200, 200, 50):
            for j in range(150, 250, 25):
                brick = turtle.Turtle()
                brick.shape("square")
                brick.color(random.choice(["red", "orange", "yellow", "green", "blue", "purple"]))
                brick.shapesize(stretch_wid=1, stretch_len=4)
                brick.penup()
                brick.goto(i, j)
                bricks.append(brick)

