import turtle
import random
import time
import math


class Shape:
    def __init__(self, shape_type, max_health, speed, defeats, color, stretch):
        self.shape_type = shape_type
        self.health = max_health
        self.speed = speed
        self.defeats = defeats
        self.stretch = stretch  # (length, width, outline)
        
        self.turtle = turtle.Turtle()
        self.turtle.speed(0)
        self.turtle.penup()
        self.turtle.shape("circle")
        self.turtle.shapesize(*stretch)
        self.turtle.color(color)

        # Assign random initial direction
        angle = random.uniform(0, 360)
        rad = math.radians(angle)
        self.dx = math.cos(rad) * speed
        self.dy = math.sin(rad) * speed

    def move(self):
        self.turtle.setx(self.turtle.xcor() + self.dx)
        self.turtle.sety(self.turtle.ycor() + self.dy)

    def bounce(self):
        w = turtle.window_width() // 2 - 20
        h = turtle.window_height() // 2 - 20
        if not -w < self.turtle.xcor() < w:
            self.dx *= -1
        if not -h < self.turtle.ycor() < h:
            self.dy *= -1

    def is_collision(self, other):
        dist = self.turtle.distance(other.turtle)
        threshold = (self.stretch[0] + other.stretch[0]) * 10
        return dist < threshold


class Square(Shape):
    def __init__(self):
        super().__init__(
            shape_type='square',
            max_health=4,
            speed=2,
            defeats=['circle'],
            color='red',
            stretch=(1.5, 1.5, 1)
        )
        self.turtle.shape("square")


class Triangle(Shape):
    def __init__(self):
        super().__init__(
            shape_type='triangle',
            max_health=3,
            speed=2.5,
            defeats=['circle'],
            color='green',
            stretch=(1.3, 1.3, 1)
        )
        self.turtle.shape("triangle")


class Rectangle(Shape):
    def __init__(self):
        super().__init__(
            shape_type='rectangle',
            max_health=5,
            speed=1.8,
            defeats=['square'],
            color='blue',
            stretch=(2.0, 1.0, 1)
        )
        self.turtle.shape("square")  # Stretch makes it rectangular


class Circle(Shape):
    def __init__(self):
        super().__init__(
            shape_type='circle',
            max_health=6,
            speed=2.2,
            defeats=['rectangle'],
            color='yellow',
            stretch=(1.0, 1.0, 1)
        )
        self.turtle.shape("circle")


class ShapeBattleGame:
    def __init__(self):
        self.shapes = []
        self.setup_screen()
        self.spawn_shapes()

    def setup_screen(self):
        self.screen = turtle.Screen()
        self.screen.title("Shape Battle Game")
        self.screen.setup(width=800, height=600)
        self.screen.bgcolor("white")
        self.screen.tracer(0)

    def spawn_shapes(self):
        shape_classes = [Square, Triangle, Rectangle, Circle]
        for shape_cls in shape_classes:
            for _ in range(random.randint(3, 6)):
                shape = shape_cls()
                shape.turtle.goto(random.randint(-350, 350), random.randint(-250, 250))
                self.shapes.append(shape)

    def handle_collisions(self):
        to_remove = set()
        for i in range(len(self.shapes)):
            for j in range(i + 1, len(self.shapes)):
                a, b = self.shapes[i], self.shapes[j]
                if a.is_collision(b):
                    # Check if one can defeat the other
                    if b.shape_type in a.defeats:
                        b.health -= 1
                    elif a.shape_type in b.defeats:
                        a.health -= 1

                    # Bounce back
                    a.dx, a.dy = -a.dx, -a.dy
                    b.dx, b.dy = -b.dx, -b.dy

                    if a.health <= 0:
                        to_remove.add(a)
                    if b.health <= 0:
                        to_remove.add(b)

        for shape in to_remove:
            shape.turtle.hideturtle()
            if shape in self.shapes:
                self.shapes.remove(shape)

    def run(self):
        try:
            while self.shapes:
                self.screen.update()
                for shape in self.shapes:
                    shape.move()
                    shape.bounce()
                self.handle_collisions()
                time.sleep(0.01)
            print("Game Over!")
        except turtle.Terminator:
            pass
        finally:
            turtle.bye()


if __name__ == "__main__":
    ShapeBattleGame().run()
