
import traceback
import pytmx
from Stage import *
from math import floor

def update(stage,window):

    
    
    for b in stage.animations :
        if b[-1] :
            b[2] += 0.2
            b[2] = b[2]%len(b[3])
            window.blit(pygame.image.load(b[3][round(b[2])]),(b[0],b[1]))
    for b in stage.animations :
        if not b[-1] :
            b[2] += 0.2
            if b[2] >= len(b[3]) :
                b[2] = 0
            window.blit(pygame.image.load(b[3][floor(b[2])]),(b[0],b[1]))


def load(file):
    gameMap = pytmx.load_pygame(file,pixilalpha=True)

    stage = Stage([],[],[],[],[])

    
    for layer in gameMap.visible_layers:
        for x, y, gid, in layer:
            props = gameMap.get_tile_properties_by_gid(gid)
            tile = gameMap.get_tile_image_by_gid(gid)
            if tile is not None:
                if props["type"] == "Platform" :
                    stage.platforms.append(Platform(x * gameMap.tilewidth,y * gameMap.tileheight, gameMap.tilewidth, gameMap.tileheight, tile, props["animated"]))

                if props["type"] == "Swap" :
                    stage.swaps.append(Swap(x * gameMap.tilewidth,y * gameMap.tileheight, gameMap.tilewidth, gameMap.tileheight, tile, props["animated"]))

                if props["type"] == "Door" :
                    stage.doors.append(Door(x * gameMap.tilewidth,y * gameMap.tileheight, gameMap.tilewidth, gameMap.tileheight, tile,props["number"], props["animated"]))

                if props["type"] == "End" :
                    stage.end.append(End(x * gameMap.tilewidth,y * gameMap.tileheight, gameMap.tilewidth, gameMap.tileheight, tile, props["animated"]))

                if props["type"] == "Secret Cookie" :
                    stage.cookies.append(Secret_Cookie(x * gameMap.tilewidth,y * gameMap.tileheight, gameMap.tilewidth, gameMap.tileheight, tile, props["animated"]))

                if props["type"] == "Background":
                    stage.background.append([pygame.Rect(x * gameMap.tilewidth,y * gameMap.tileheight, gameMap.tilewidth, gameMap.tileheight), tile, props["animated"]])
                
                if props["animated"] :
                    animation = []
                    error = False
                    i = 0
                    while not error :
                        try :
                            animation.append(str(props[f"frame{i}"][1:]))
                            i += 1
                        except:
                            error = True
                    stage.animations.append([x* gameMap.tilewidth,y * gameMap.tileheight,0,animation, props["type"] == "Background"])

    return stage, gameMap.timeswap, gameMap.x_player1*gameMap.tileheight, gameMap.y_player1*gameMap.tileheight, gameMap.x_player2*gameMap.tileheight, gameMap.y_player2*gameMap.tileheight

def draw_game(gameMap,gameScreen):
    # draw map data on screen
    for layer in gameMap.visible_layers:
        for x, y, gid, in layer:
            tile = gameMap.get_tile_image_by_gid(gid)
            gameScreen.blit(tile, (x * gameMap.tilewidth,
                                   y * gameMap.tileheight))