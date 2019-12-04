#!/usr/bin/env python

import math

import pygame
from pygame.locals import *

import random, time
from datetime import datetime
from multiprocessing import Process, Queue, Semaphore
from threading import Thread

s = Semaphore(1)


class World(object):
    """ contains all of our game state """

    RENDER_OPTIONS = HWSURFACE | DOUBLEBUF | RESIZABLE
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    NEGRO  = (  0,   0,   0)
    ROJO   = (255,   0,   0)

    def __init__(self, size, player):
        # setting up the screen
        self.size = size
        self.surface = pygame.display.set_mode(size, self.RENDER_OPTIONS)
        self.surface.fill(self.BLACK)

        # stash the player sprite
        self.player = player

        # adding a sprite group
        self.sprites = pygame.sprite.RenderUpdates()
        self.sprites.add(player)

        # setup our event handlers
        self.event_handlers = {
            VIDEORESIZE: self.handle_resize,
            KEYDOWN: self.handle_keydown,
            KEYUP: self.handle_keyup
        }

    def update(self):
        # allow any sprites to update themselves
        self.sprites.update()

        # change the sprite's location to match it's proper motion
        for sprite in self.sprites:

            # grab the next position the sprite should be at
            new_center = Vector.from_position(sprite.rect.center) + sprite.motion
            new_center = new_center.to_position()

            # do the screen wrap for the x and y positions
            x = new_center[0] % self.size[0]
            y = new_center[1] % self.size[1]
            sprite.rect.center = (x, y)


    def render(self):
        """ render the sprites to the window """
        def clear_callback(surface, rect):
            surface.fill(self.BLACK, rect)

        self.sprites.clear(self.surface, clear_callback)
        updatedRects = self.sprites.draw(self.surface)
        pygame.display.update(updatedRects)

    def handle_event(self, event):
        handler = self.event_handlers.get(event.type, lambda x: None)
        handler(event)

    def handle_resize(self, event):
        """ set the window size """
        self.size = event.dict['size']
        self.surface = pygame.display.set_mode(self.size, self.RENDER_OPTIONS)

    def handle_keyup(self, event):
        """ set a ship up moviment  """
        if event.key == pygame.K_UP:
            player.forward = False
        if event.key == pygame.K_DOWN:
            player.backward = False
        if event.key == pygame.K_RIGHT:
            player.turn_right = False
        if event.key == pygame.K_LEFT:
            player.turn_left = False
        if event.key == pygame.K_SPACE:
            bullet = Bullet((Vector(*self.player.rect.center) - self.player.facing*2).to_position(), self.player.facing.to_degrees()[0] + 180, self.player.motion.magnitude() + 10) #position, direction, magnitude

            self.sprites.add(bullet)

    def handle_keydown(self, event):
        """ set a ship down moviment  """
        if event.key == pygame.K_UP:
            player.forward = True
        if event.key == pygame.K_DOWN:
            player.backward = True
        if event.key == pygame.K_RIGHT:
            player.turn_right = True
        if event.key == pygame.K_LEFT:
            player.turn_left = True







class Vector(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def magnitude(self):
        """ return the magnitude (aka: distance) this vector represents """
        return math.sqrt(self.x * self.x + self.y * self.y)

    def normalize(self):
        """ return a unit vector """
        return self / self.magnitude()

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(round(x, 2), round(y, 2))

    def __sub__(self, other):
        x = self.x - other.x
        y = self.y - other.y
        return Vector(round(x, 2), round(y, 2))

    def __mul__(self, n):
        x = self.x * n
        y = self.y * n
        return Vector(round(x, 2), round(y, 2))

    def __div__(self, n):
        x = self.x / n
        y = self.y / n
        return Vector(round(x, 2), round(y, 2))

    def __repr__(self):
        return "Vector({}, {})".format(self.x, self.y)

    def to_position(self):
        return (self.x, self.y)

    def to_radians(self):
        radians = math.atan2(self.x, self.y)
        return (radians, self.magnitude())

    def to_degrees(self):
        radians, magnitude = self.to_radians()
        return (math.degrees(radians), magnitude)

    @classmethod
    def from_position(self, position):
        return Vector(position[0], position[1])

    @classmethod
    def from_radians(self, radians, magnitude=1):
        return Vector(math.sin(radians), math.cos(radians)) * magnitude

    @classmethod
    def from_degrees(self, degrees, magnitude=1):
        return Vector.from_radians(math.radians(degrees), magnitude)


class Entity(pygame.sprite.Sprite):

    def __init__(self, image, position):
        super(Entity, self).__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = position
        self.motion = Vector(0, 0)



class Player(Entity):
    """ represents the player """

    def __init__(self, position):
        self.orig_image = pygame.image.load('assets/ship.png')
        super(Player, self).__init__(self.orig_image, position)
        self.facing = Vector.from_degrees(90)
        self.forward = False
        self.backward = False
        self.turn_left = False
        self.turn_right = False
        self.accel = 0.15
        self.life = 3

    def update(self):
        # if we are thrusting, add the vector of our facing to the motion
        if self.forward:
            self.motion = self.motion - self.facing * self.accel

        if self.backward:
            #self.motion = self.motion + self.facing * self.accel
            self.motion = self.motion + self.facing * self.accel

        degrees, _ = self.facing.to_degrees()
        if self.turn_left:
            degrees = (degrees + 10) % 360

        if self.turn_right:
            degrees = (degrees - 10) % 360


        self.facing = Vector.from_degrees(degrees)

        # rotate our sprite to match our direction, and put it in the right place
        current = self.rect.center
        self.image = pygame.transform.rotate(self.orig_image, degrees)
        self.rect = self.image.get_rect()
        self.rect.center = current




class Bullet(Entity):
    """ A bullet. Pew Pew. """

    def __init__(self, position, direction, magnitude):
        self.orig_image = pygame.image.load('assets/bullet.png')
        super(Bullet, self).__init__(self.orig_image, position)
        self.motion = Vector.from_degrees(direction, magnitude)
        self.duration = 50

    def update(self):
        self.duration = self.duration - 1
        if self.duration <= 0:
            self.kill()

class Asteroid(Entity):

    def __init__(self, position):
        image = pygame.image.load('assets/asteroid.png')
        super(Asteroid, self).__init__(image, position)
        self.motion = Vector.from_degrees(random.randint(0, 360)) * 3
        self.duration = 500

    def update(self):
        #time.sleep(1)
        self.duration = self.duration - 1
        if self.duration <= 0:
            self.kill()

def update_s():
    #print "entra"
    i = 0
    while world.running:
        s.acquire()
        if i == 10 and len([x for x in world.sprites if isinstance(x, Asteroid)]) < 30:
            asteroid = Asteroid((random.randint(0, 800), random.randint(0,600)))
            world.sprites.add(asteroid)
            i = 0
        i += 1


        world.update()
        world.render()
        pygame.display.flip()
        s.release()
        clock.tick(60)


    #print 'acaba'
    return 0

def update_collision():

    while world.running:

        s.acquire()

        cShootVSAsteroid()

        cShipVSAsteroid()

        s.release()

        clock.tick(60)

    return 0

def cShootVSAsteroid():
    for i in [x for x in world.sprites if isinstance(x, Asteroid)]:
        for f in [y for y in world.sprites if isinstance(y, Bullet)]:
            if ( abs( f.rect.center[0] - i.rect.center[0]) < 25 and abs(f.rect.center[1] - i.rect.center[1]) < 25 ):
                i.kill()
                f.kill()

def cShipVSAsteroid():
    for i in [x for x in world.sprites if isinstance(x,  Asteroid)]:
        if ( abs( player.rect.center[0] - i.rect.center[0]) < 15 and abs(player.rect.center[1] - i.rect.center[1]) < 15 ):
                gameOver(i)
"""
    I've added a: 
        - Method gameOver()
        - Method to eliminate asteroids [ killAsteroid() ], 
        - Method to add a background image
    And i've removed:
        - The step of filling the red background
 """


def gameOver(asteroidKiller):

    killAsteroid(asteroidKiller)
    world.update()
    world.render()

    loadImageGameOver()

    pygame.display.flip()
    pygame.time.wait(5000) #5 segundos
    world.running = False

def loadImageGameOver():
    background = pygame.image.load('img/gameoverphrase.png')
    world.surface.blit(background,(260,150))

def killAsteroid(asteroidKiller):
        for i in [x for x in world.sprites if isinstance(x, Asteroid)]:
            if (i.rect.center[0] == asteroidKiller.rect.center[0]) and (i.rect.center[1] == asteroidKiller.rect.center[1]):
                print("Fuera")
            else:
                i.kill()


# setup pygame
pygame.init()
pygame.font.init()
pygame.mixer.init()
pygame.display.set_caption("Asteroids 0.2")

# store our game state
player = Player((400, 300))
world = World((800, 600), player)
world.pew = pygame.mixer.Sound('assets/pew.wav')
world.running = True
# use the clock to throttle the fps to something reasonable
clock = pygame.time.Clock()

def main():
    """ runs our application """

    # main loop
    s_update = Thread(target=update_s)
    c_update = Thread(target=update_collision)
    s_update.start()
    c_update.start()
    while world.running:

        events = pygame.event.get()

        # handle our events
        for event in events:
            if event.type == QUIT:
                world.running = False
                break

            world.handle_event(event)

        '''
        if len(world.sprites) < 30:
            asteroid = Asteroid((random.randint(0, 800), random.randint(0,600)))
            world.sprites.add(asteroid)


        world.update()
        world.render()
        pygame.display.flip()
        '''
        clock.tick(40)
        #supdate.join()


if __name__ == "__main__":
    main()
