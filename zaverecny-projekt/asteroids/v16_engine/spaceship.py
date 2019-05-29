import pyglet
import math
from space_object import SpaceObject

# Degrees per second
ROTATION_SPEED = 4
ACCELERATION = 200

class Spaceship(SpaceObject):
    def __init__(self, batch):
        super().__init__(batch)
        engine_image = pyglet.image.load("../assets/PNG/effects/fire06.png")
        engine_image.anchor_x = engine_image.width //2
        engine_image.anchor_y = -engine_image.height -5

        self.engine_sprite = pyglet.sprite.Sprite(engine_image, batch=batch)

    def image_path(self):
        return "../assets/PNG/playerShip1_orange.png"

    def tick(self, time_elapsed, keys_pressed, window):
        self.engine_sprite.visible = False
        if pyglet.window.key.LEFT in keys_pressed:
            self.rotation = self.rotation + time_elapsed*ROTATION_SPEED
        if pyglet.window.key.RIGHT in keys_pressed:
            self.rotation = self.rotation - time_elapsed*ROTATION_SPEED
        if pyglet.window.key.UP in keys_pressed:
            self.engine_sprite.visible = True
            self.x_speed += time_elapsed * ACCELERATION * math.cos(self.rotation)
            self.y_speed += time_elapsed * ACCELERATION * math.sin(self.rotation)

        self.x = self.x + time_elapsed*self.x_speed
        self.y = self.y + time_elapsed*self.y_speed

        # infinite space - wraparound coordinates
        self.x %= window.width
        self.y %= window.height

        self.engine_sprite.x = self.x
        self.engine_sprite.y = self.y
        self.engine_sprite.rotation = 270 - math.degrees(self.rotation)

        super().update_sprite()


    def destroy_object(self):
        super().destroy_object()
        self.engine_sprite.delete()
