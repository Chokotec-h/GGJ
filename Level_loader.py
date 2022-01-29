
import pytmx
from Stage import *

def load(file):
    gameMap = pytmx.load_pygame(file,pixilalpha=True)

    stage = Stage([],[],[],[])

    
    for layer in gameMap.visible_layers:
        for x, y, gid, in layer:
            props = gameMap.get_tile_properties_by_gid(gid)
            tile = gameMap.get_tile_image_by_gid(gid)
            #if tile.type == "platform":
            if tile is not None :
                if props["type"] == "Platform" :
                    stage.platforms.append(Platform(x * gameMap.tilewidth,y * gameMap.tileheight, gameMap.tilewidth, gameMap.tileheight, tile))

                if props["type"] == "Swap" :
                    stage.swaps.append(Swap(x * gameMap.tilewidth,y * gameMap.tileheight, gameMap.tilewidth, gameMap.tileheight, tile))

                if props["type"] == "Door" :
                    stage.doors.append(Door(x * gameMap.tilewidth,y * gameMap.tileheight, gameMap.tilewidth, gameMap.tileheight, tile,props["number"]))

                if props["type"] == "End" :
                    stage.end.append(End(x * gameMap.tilewidth,y * gameMap.tileheight, gameMap.tilewidth, gameMap.tileheight, tile))


    return stage, gameMap.timeswap, gameMap.x_player1*gameMap.tileheight, gameMap.y_player1*gameMap.tileheight, gameMap.x_player2*gameMap.tileheight, gameMap.y_player2*gameMap.tileheight

def draw_game(gameMap,gameScreen):
    # draw map data on screen
    for layer in gameMap.visible_layers:
        for x, y, gid, in layer:
            tile = gameMap.get_tile_image_by_gid(gid)
            gameScreen.blit(tile, (x * gameMap.tilewidth,
                                   y * gameMap.tileheight))