# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player
from shot import Shot
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    pygame.init()
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    updatable, drawable = pygame.sprite.Group() , pygame.sprite.Group()
    Player.containers = (updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)

    AsteroidField.containers = (updatable)
    asteroid_field = AsteroidField()

    shots = pygame.sprite.Group()

    Shot.containers = (shots, updatable, drawable)


    # GAME LOOP
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock_obj = pygame.time.Clock()
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # update step
        for obj in updatable:
            obj.update(dt)

        # Collision check
        for asteroid in asteroids:
            if asteroid.collision_check(player):
                print("Game over!")
                exit()

            for shot in shots:
                if asteroid.collision_check(shot):
                    shot.kill()
                    asteroid.split()


        screen.fill("black")

        
        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()

        # FPS Limit
        dt = clock_obj.tick(60) / 1000

        
        
        




if __name__ == "__main__":

    main()