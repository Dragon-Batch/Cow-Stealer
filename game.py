import pygame

def check_plus_or_negative(num:int):
    if num > 0:
        return(True)
    elif num < 0:
        return(False)

pygame.init()

w,h = int(700),int(600)

pygame.display.set_caption('cow stealer')
gameScreen = pygame.display.set_mode((w,h))

black = (0, 0, 0)
white = (255, 255, 255)
backround = (21, 38, 48)
playerImage = pygame.image.load('player.png')
playerSize = playerImage.get_rect().size
playerAcceleration = int(1)
gameClock = pygame.time.Clock()
fps = int(60)

startingPosition = (100,1)
playerPosX = int(1)
playerPosY = int(100)

gameScreen.fill(white)
gameScreen.blit(playerImage, (startingPosition))
pygame.display.update()

def movePlayer(x: int, y: int):
    gameScreen.blit(playerImage, (x,y))
    return()

while True:
    gameScreen.fill(backround)
    if check_plus_or_negative(playerAcceleration) == True:
        if int(playerPosX + playerAcceleration + playerSize[0]) > w:
            playerAcceleration -= int(playerAcceleration*2)
    else:
        if int(playerPosX + playerAcceleration) < 0:
            playerAcceleration -= int(playerAcceleration*2)

    playerPosX += playerAcceleration
    movePlayer(playerPosX,playerPosY)
    pygame.display.update()
    gameClock.tick(fps)