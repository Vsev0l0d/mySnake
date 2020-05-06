import time
import turtle
from random import randrange

BREAK_FLAG = False
LONG_SIDE_OF_THE_FIELD = 500

screen = turtle.Screen()
screen.title("mySnake")
screen.bgcolor('light green')
screen.setup(LONG_SIDE_OF_THE_FIELD, LONG_SIDE_OF_THE_FIELD)
screen.tracer(0)

border = turtle.Turtle()
border.hideturtle()
border.penup()

snake = []
for segment_number in range(3):
    snake_segment = turtle.Turtle()
    snake_segment.shape('circle')
    snake_segment.penup()
    snake_segment.color('dark green')
    snake.append(snake_segment)
snake[0].shapesize(1.4)
snake[1].shapesize(1.2)
snake[2].shapesize(1)

food = turtle.Turtle()
food.shape('square')
food.color("purple")
food.penup()
food.goto(randrange(-(LONG_SIDE_OF_THE_FIELD - 50) // 2, (LONG_SIDE_OF_THE_FIELD - 50) // 2, 20),
          randrange(-(LONG_SIDE_OF_THE_FIELD - 50) // 2, (LONG_SIDE_OF_THE_FIELD - 50) // 2, 20))


def is_the_head_in_the_field():
    x = snake[0].xcor()
    y = snake[0].ycor()
    if x > LONG_SIDE_OF_THE_FIELD // 2 \
            or x < -LONG_SIDE_OF_THE_FIELD // 2 \
            or y < -LONG_SIDE_OF_THE_FIELD // 2 \
            or y > LONG_SIDE_OF_THE_FIELD // 2:
        return False
    return True


direction_of_travel = 'Right'


def snake_turns(side):
    global direction_of_travel
    if side == 'Up' and direction_of_travel != 'Down' and is_the_head_in_the_field():
        snake[0].setheading(90)
        direction_of_travel = 'Up'
    if side == 'Down' and direction_of_travel != 'Up' and is_the_head_in_the_field():
        snake[0].setheading(270)
        direction_of_travel = 'Down'
    if side == 'Left' and direction_of_travel != 'Right' and is_the_head_in_the_field():
        snake[0].setheading(180)
        direction_of_travel = 'Left'
    if side == 'Right' and direction_of_travel != 'Left' and is_the_head_in_the_field():
        snake[0].setheading(0)
        direction_of_travel = 'Right'


screen.onkeypress(lambda: snake_turns('Up'), 'Up')
screen.onkeypress(lambda: snake_turns('Down'), 'Down')
screen.onkeypress(lambda: snake_turns('Left'), 'Left')
screen.onkeypress(lambda: snake_turns('Right'), 'Right')
screen.listen()


def snake_creeps(distance, direction=1):
    for i in range(len(snake) - 1, 0, -1):
        snake[i].goto(snake[i - 1].xcor(), snake[i - 1].ycor())
    if direction < 0:
        snake[0].back(distance)
    else:
        snake[0].forward(distance)

    screen.update()


while True:
    if snake[0].distance(food) < 20:
        while True:
            check = True
            for segment in snake:
                if segment.distance(food) < 20:
                    check = False
                    food.goto(randrange(-(LONG_SIDE_OF_THE_FIELD - 50) // 2, (LONG_SIDE_OF_THE_FIELD - 50) // 2, 20),
                              randrange(-(LONG_SIDE_OF_THE_FIELD - 50) // 2, (LONG_SIDE_OF_THE_FIELD - 50) // 2, 20))
            if check:
                break

        snake_segment = turtle.Turtle()
        snake_segment.shape('circle')
        snake_segment.color('dark green')
        snake_segment.penup()
        snake.append(snake_segment)
        for segment_number in range(1, len(snake) // 2):
            snake[segment_number].shapesize(1.2)

    if not is_the_head_in_the_field():
        snake_creeps(LONG_SIDE_OF_THE_FIELD, -1)
    else:
        snake_creeps(20)

    for segment_number in snake[1:]:
        segment_number = segment_number.position()
        if snake[0].distance(segment_number) < 10:
            BREAK_FLAG = True
    if BREAK_FLAG:
        screen.bgcolor('red')
        time.sleep(1)
        break
    time.sleep(0.18)
