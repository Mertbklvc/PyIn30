ef random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    random_color = (r,g,b)
    return random_color

mert.speed("fastest")

for i in range(20):
    mert.color(random_color())
    mert.forward(30)
    mert.setheading(random.choice(directions))





screen.exitonclick()
