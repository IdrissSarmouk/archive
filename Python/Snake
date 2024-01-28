#Pink Snake Game!
import turtle
import random

width = 750
height = 750
foodS = 20
delay = 101

offsets = {
    "up": (0, 20),
    "down": (0,-20),
    "left": (-20,0),
    "right": (20, 0),
}

def reset():
    global snake, snakeDir, foodP, pen
    snake = [[0, 0], [0, 20], [0, 40], [0, 60], [0, 80]]
    snakeDir = "up"
    foodP = get_random_foodP()
    food.goto(foodP)
    move_snake()

    
def move_snake():
    global snake_dir
    new_head = snake[-1].copy()
    new_head[0] = snake[-1][0] + offsets[snakeDir][0]
    new_head[1] = snake[-1][1] + offsets[snakeDir][1]

    if new_head in snake[:-1]:
        reset()
    else:
        snake.append(new_head)

        if not food_collision():
            snake.pop(0)

        if snake[-1][0] > width/2:
            snake[-1][0]-= width 
        elif  snake[-1][0] < - width/2:  
            snake[-1][0] += width
        elif snake[-1][1] > height / 2:
            snake[-1][1] -= height
        elif snake[-1][1] < - height / 2:
            snake[-1][1]+= height

        pen.clearstamps()

        for segment in snake:
            pen.goto(segment[0], segment[1])
            pen.stamp()

        screen.update()

        turtle.ontimer(move_snake, delay)
def food_collision():
    global foodP   
    if get_distance(snake[-1], foodP) <20:
        foodP = get_random_foodP()
        food.goto(foodP)
        return True
    return False

def get_random_foodP():
    x = random.randint(- width/2 + foodS, width/2 - foodS) 
    y = random.randint(- height/2 + foodS, height/2 - foodS)
    return (x, y)

def get_distance(pos1, pos2):
    x1, y1 = pos1
    x2, y2 = pos2
    distance = ((y2 - y1)**2 + (x2 - x1)**2) ** 0.5
    return distance

def go_up():
    global snakeDir
    if snakeDir != "down":
        snakeDir = "up"

def go_right():
    global snakeDir 
    if snakeDir != "left": 
        snakeDir = "right"

def go_left():
    global snakeDir 
    if snakeDir != "right":
        snakeDir = "left"

def go_down():
    global snakeDir 
    if snakeDir != "up":
        snakeDir= "down"

screen = turtle.Screen()
screen.setup(width, height)
screen.title("SNAKE GAME")
screen.bgcolor("Pink")
screen.setup(750, 750)
screen.tracer(0)

pen = turtle.Turtle("square")
pen.penup()

food = turtle.Turtle()
food.shape("circle")
food.color("blue")
food.shapesize(foodS /20)
food.penup()

screen.listen()
screen.onkey(go_up, "Up")
screen.onkey(go_right, "Right")
screen.onkey(go_down, "Down")
screen.onkey(go_left, "Left")

reset()
turtle.done()
