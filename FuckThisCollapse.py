import sys
import pygame
import time
import random
import os
import inspect

levelTitles = [
    [
        [1,0,0, 0, 1,3,2, 0, 1,0,3, 0, 3,1,4, 0, 4,0,0, 0, 0,1,0],
        [2,0,0, 0, 2,0,0, 0, 3,0,4, 0, 1,0,0, 0, 2,0,0, 0, 2,3,0],
        [1,0,0, 0, 3,1,4, 0, 4,0,2, 0, 2,4,2, 0, 1,0,0, 0, 0,1,0],
        [3,0,0, 0, 4,0,0, 0, 0,1,0, 0, 4,0,0, 0, 3,0,0, 0, 0,4,0],
        [4,3,2, 0, 1,2,1, 0, 0,3,0, 0, 3,1,2, 0, 4,1,2, 0, 1,2,4],
    ],
    [
        [1,0,0, 0, 1,3,2, 0, 1,0,3, 0, 3,1,4, 0, 4,0,0, 0, 0,1,0],
        [2,0,0, 0, 2,0,0, 0, 3,0,4, 0, 1,0,0, 0, 2,0,0, 0, 2,0,3],
        [1,0,0, 0, 3,1,4, 0, 4,0,2, 0, 2,4,2, 0, 1,0,0, 0, 0,0,1],
        [3,0,0, 0, 4,0,0, 0, 0,1,0, 0, 4,0,0, 0, 3,0,0, 0, 1,2,0],
        [4,3,2, 0, 1,2,1, 0, 0,3,0, 0, 3,1,2, 0, 4,1,2, 0, 3,2,1]
    ],
    [
        [1,0,0, 0, 1,3,2, 0, 1,0,3, 0, 3,1,4, 0, 4,0,0, 0, 4,1,3],
        [2,0,0, 0, 2,0,0, 0, 3,0,4, 0, 1,0,0, 0, 2,0,0, 0, 0,0,3],
        [1,0,0, 0, 3,1,4, 0, 4,0,2, 0, 2,4,2, 0, 1,0,0, 0, 1,1,2],
        [3,0,0, 0, 4,0,0, 0, 0,1,0, 0, 4,0,0, 0, 3,0,0, 0, 0,0,4],
        [4,3,2, 0, 1,2,1, 0, 0,3,0, 0, 3,1,2, 0, 4,1,2, 0, 3,2,1],
    ],
    [
        [1,0,0, 0, 1,3,2, 0, 1,0,3, 0, 3,1,4, 0, 4,0,0, 0, 4,0,2],
        [2,0,0, 0, 2,0,0, 0, 3,0,4, 0, 1,0,0, 0, 2,0,0, 0, 2,0,3],
        [1,0,0, 0, 3,1,4, 0, 4,0,2, 0, 2,4,2, 0, 1,0,0, 0, 3,1,2],
        [3,0,0, 0, 4,0,0, 0, 0,1,0, 0, 4,0,0, 0, 3,0,0, 0, 0,0,3],
        [4,3,2, 0, 1,2,1, 0, 0,3,0, 0, 3,1,2, 0, 4,1,2, 0, 0,0,4],
    ],
    [
        [1,0,0, 0, 1,3,2, 0, 1,0,3, 0, 3,1,4, 0, 4,0,0, 0, 1,2,1],
        [2,0,0, 0, 2,0,0, 0, 3,0,4, 0, 1,0,0, 0, 2,0,0, 0, 4,0,0],
        [1,0,0, 0, 3,1,4, 0, 4,0,2, 0, 2,4,2, 0, 1,0,0, 0, 1,3,4],
        [3,0,0, 0, 4,0,0, 0, 0,1,0, 0, 4,0,0, 0, 3,0,0, 0, 0,0,1],
        [4,3,2, 0, 1,2,1, 0, 0,3,0, 0, 3,1,2, 0, 4,1,2, 0, 4,3,2],
    ],
    [
        [1,0,0, 0, 1,3,2, 0, 1,0,3, 0, 3,1,4, 0, 4,0,0, 0, 1,1,4],
        [2,0,0, 0, 2,0,0, 0, 3,0,4, 0, 1,0,0, 0, 2,0,0, 0, 2,0,0],
        [1,0,0, 0, 3,1,4, 0, 4,0,2, 0, 2,4,2, 0, 1,0,0, 0, 1,3,1],
        [3,0,0, 0, 4,0,0, 0, 0,1,0, 0, 4,0,0, 0, 3,0,0, 0, 4,0,1],
        [4,3,2, 0, 1,2,1, 0, 0,3,0, 0, 3,1,2, 0, 4,1,2, 0, 3,2,4],
    ],
    [
        [1,0,0, 0, 1,3,2, 0, 1,0,3, 0, 3,1,4, 0, 4,0,0, 0, 3,1,4],
        [2,0,0, 0, 2,0,0, 0, 3,0,4, 0, 1,0,0, 0, 2,0,0, 0, 0,0,2],
        [1,0,0, 0, 3,1,4, 0, 4,0,2, 0, 2,4,2, 0, 1,0,0, 0, 0,4,0],
        [3,0,0, 0, 4,0,0, 0, 0,1,0, 0, 4,0,0, 0, 3,0,0, 0, 0,3,0],
        [4,3,2, 0, 1,2,1, 0, 0,3,0, 0, 3,1,2, 0, 4,1,2, 0, 0,1,0],
    ]
]
        
maps = [                                                                   
    [                                                                      
        [4,2,1,3,2,1],                                                     
        [3,4,4,4,1,3],                                                     
        [2,3,2,3,3,3],                                                     
        [4,4,3,1,3,3],                                                     
        [3,1,4,2,2,1],                                                     
        [2,3,1,1,4,2]
    ],                                                                     
    [                                                                      
        [4,1,3,4,2,2,4],                                                   
        [1,4,4,2,1,4,4],                                                   
        [1,1,4,2,1,3,1],                                                   
        [4,1,1,3,1,3,4],                                                   
        [2,4,4,3,1,4,2],                                                   
        [4,3,2,4,3,4,3],                                                   
        [3,4,1,3,3,3,3]
    ],                                                                     
    [                                                                      
        [4,1,2,2,4,3,1,3],                                                 
        [2,3,1,3,2,1,3,1],                                                 
        [3,4,1,3,2,4,1,1],                                                 
        [4,3,1,3,4,1,1,4],                                                 
        [2,4,2,1,1,2,4,1],                                                 
        [1,3,2,1,2,1,1,2],                                                 
        [4,3,1,3,4,3,1,2],                                                 
        [1,1,3,2,4,2,2,1]
    ],                                                                     
    [                                                                      
        [2,3,3,3,2,2,3,4,4],                                               
        [4,4,3,3,1,3,2,1,3],                                               
        [4,3,4,2,1,3,4,1,2],                                               
        [4,3,1,1,1,1,3,1,1],                                               
        [4,2,3,3,1,1,4,4,2],                                               
        [2,4,2,2,3,1,2,2,2],                                               
        [1,4,3,2,4,4,1,3,1],                                               
        [1,3,4,4,2,1,3,4,1],                                               
        [2,1,2,2,1,4,4,3,2]
    ],                                                                     
    [                                                                      
        [2,2,3,4,4,1,3,4,3,1],                                             
        [1,2,1,4,3,1,4,1,1,1],                                             
        [1,2,3,4,2,4,1,1,3,3],                                             
        [3,4,1,4,2,4,4,2,4,4],                                             
        [3,3,1,1,2,1,2,2,2,1],                                             
        [4,1,2,4,4,2,3,4,1,1],                                             
        [2,2,4,3,2,4,3,1,1,1],                                             
        [4,3,1,2,3,1,1,1,3,3],                                             
        [2,2,3,3,1,4,1,3,1,1],                                             
        [3,3,4,2,2,4,3,4,1,4]
    ],                                                                     
    [                                                                      
        [1,1,1,4,3,2,2,2,4,2,1],                                           
        [2,3,3,2,2,2,1,2,1,1,1],                                           
        [4,3,2,3,1,3,2,4,4,2,2],                                           
        [1,4,3,2,2,2,2,1,3,3,3],                                           
        [3,2,2,3,1,4,3,1,4,3,2],                                           
        [3,1,1,1,1,3,1,2,3,2,4],                                           
        [1,2,4,1,1,2,1,1,4,1,4],                                           
        [3,2,4,1,3,2,3,3,4,1,4],                                           
        [2,4,3,4,2,3,1,2,1,2,3],                                           
        [1,2,1,2,3,3,4,4,3,2,3],                                           
        [3,3,3,3,3,4,1,4,4,2,3]
    ],                                                                     
    [                                                                      
        [4,4,1,3,2,4,4,2,3,2,2,3],                                         
        [2,4,1,3,2,3,3,4,4,3,1,2],                                         
        [1,3,3,4,3,1,4,3,1,1,3,2],                                         
        [4,2,2,1,2,2,3,3,1,3,4,1],                                         
        [3,2,2,3,4,4,2,2,3,2,2,2],                                         
        [1,1,3,3,1,4,3,2,2,4,4,2],                                         
        [3,1,3,3,3,2,2,3,3,1,4,3],                                         
        [2,3,2,3,4,4,3,3,3,4,2,3],                                         
        [1,4,2,3,2,1,3,4,2,3,4,2],                                         
        [1,2,3,2,1,4,2,2,3,1,3,3],                                         
        [4,4,4,2,2,4,3,4,2,2,2,1],                                         
        [4,1,1,3,2,1,3,3,1,1,4,2]
    ],
    [                                                                      
        [4,4,1,3,2,4,4,2,3,2,2,3,2],                                         
        [2,4,1,3,2,3,3,4,4,3,1,2,3],                                         
        [1,3,3,4,3,1,4,3,1,1,3,2,1],                                         
        [4,2,2,1,2,2,3,3,1,3,4,1,1],                                         
        [3,2,2,3,4,4,2,2,3,2,2,2,3],                                         
        [1,1,3,3,1,4,3,2,2,4,4,2,3],                                         
        [3,1,3,3,3,2,2,3,3,1,4,3,2],                                         
        [2,3,2,3,4,4,3,3,3,4,2,3,4],                                         
        [1,4,2,3,2,1,3,4,2,3,4,2,4],                                         
        [1,2,3,2,1,4,2,2,3,1,3,3,1],                                         
        [4,4,4,2,2,4,3,4,2,2,2,1,4],                                         
        [4,1,1,3,2,1,3,3,1,1,4,2,2],
        [3,2,2,3,4,4,2,2,3,2,2,2,3]                                         
    ]
]                                                                          

class Game:
    LOAD_PATH = os.path.dirname(inspect.stack()[0][1])
    # Debug flags, disable these before production
    DEBUG_MODE = False
    DRAW_MOVES = True
    # -----

    MARBLE_WIDTH = 40
    MARBLE_HEIGHT = 40
    MARBLE_CENTER_X = 20
    MARBLE_CENTER_Y = 20

    COLOR_MAGICPINK = (255, 0, 255, 0)
    COLOR_WHITE = (255, 255, 255, 255)
    COLOR_BLACK = (0, 0, 0, 255)
    SCREEN_WIDTH = 960
    SCREEN_HEIGHT = 540

    STATE_NONE = 0
    STATE_FALLING = 1
    STATE_SELECTED = 1 << 1
    STATE_DEAD = 1 << 2
    STATE_PLAYERTOUCHED = 1 << 3
    STATE_DRAGGING = 1 << 4

    STATE_GAME_MAIN = 1 << 1
    STATE_GAME_TITLE = 1 << 2
    STATE_GAME_TITLE_FALLING = 1 << 3
    STATE_GAME_WIN = 1 << 5

    M_IDX_MOVES = 0
    M_IDX_TYPE = 1
    M_IDX_STATE = 2
    M_IDX_POS = 3
    M_IDX_VEL = 4

    P_IDX_X = 0
    P_IDX_Y = 1

    VELOCITY_CUMULATIVE = 1
    VELOCITY_STATIC = 2

    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.__velocity_mode__ = Game.VELOCITY_CUMULATIVE
        self.__gamestate__ = Game.STATE_GAME_TITLE
        self.__display__ = pygame.display.set_mode((Game.SCREEN_WIDTH, Game.SCREEN_HEIGHT))
        self.__blitTarget__ = self.__display__.convert_alpha()
        self.__marbles__ = []
        pygame.display.set_caption("Fuck This Collapse")
        self.__load_marbles__()
        self.__sound_falling__ = pygame.mixer.Sound(self.__loadpath__(['snd', 'marblefall.wav']))
        self.__sound_click__ = pygame.mixer.Sound(self.__loadpath__(['snd', 'marbleclick.wav']))
        self.__sound_level__ = pygame.mixer.Sound(self.__loadpath__(['snd', 'newlevel.wav']))
        pygame.mixer.music.load(self.__loadpath__(['snd', 'POL-lurking-short.wav']))
        pygame.mixer.music.play(-1)

        self.__curMap__ = None
        self.__curMapRect__ = None
        self.__moves__ = 0
        self.__maxMarbleMoves__ = 4

        self.__selectedMarble__ = [-1, -1]
        self.__setSelectedMarble__([-1, -1])
        self.__selectionRect__ = None
        self.__selectionSurface__ = pygame.Surface(
            (Game.MARBLE_WIDTH, Game.MARBLE_HEIGHT),
            pygame.SRCALPHA | pygame.HWSURFACE)
        self.__selectionSurface__.fill((255,255,255, 128))

        self.__gameFont__ = pygame.font.SysFont(pygame.font.get_default_font(), 18)
        self.__debugFont__ = pygame.font.SysFont(pygame.font.get_default_font(), 12)
        self.__mapIndex__ = 0
        self.__setMap__(levelTitles[self.__mapIndex__], isTitle = True)

    def __loadpath__(self, items):
        return os.path.join(Game.LOAD_PATH, *items)

    def __load_marbles__(self):
        self.__marbles__.append(None)
        self.__marbles__.append(pygame.image.load(self.__loadpath__(['gfx', 'BlueSwirl.png'])))
        self.__marbles__.append(pygame.image.load(self.__loadpath__(['gfx', 'MochaVolcano.png'])))
        self.__marbles__.append(pygame.image.load(self.__loadpath__(['gfx', 'SwirlyEyeball.png'])))
        self.__marbles__.append(pygame.image.load(self.__loadpath__(['gfx', 'ZebraGum.png'])))

    def __setMap__(self, maparray, isTitle=False):
        self.__curMap__ = []
        self.__curMapRect__ = pygame.Rect(
            ((Game.SCREEN_WIDTH - (Game.MARBLE_WIDTH * len(maparray[0])))/2),
            0,
            (Game.MARBLE_WIDTH * len(maparray[0])),
            (Game.MARBLE_HEIGHT * len(maparray))
        )

        initState = Game.STATE_NONE
        x = self.__curMapRect__.left
        y = self.__curMapRect__.top
        self.__gamestate__ = Game.STATE_GAME_MAIN
        self.__velocity_mode__ = Game.VELOCITY_CUMULATIVE
        Game.DRAW_MOVES = True

        if isTitle:
            Game.DRAW_MOVES = False
            self.__gamestate__ = Game.STATE_GAME_TITLE
            self.__sound_level__.play()

        for row in maparray:
            x = self.__curMapRect__.left
            mrow = []
            self.__curMap__.append(mrow) 
            for col in row:
                mrow.append(
                    [self.__maxMarbleMoves__, 
                     col, 
                     initState, 
                     [x, y], 
                     [0.0, 0.0]])
                x += Game.MARBLE_WIDTH
            y += Game.MARBLE_HEIGHT

    def __update__(self):
        if self.__gamestate__ == Game.STATE_GAME_WIN:
            return

        all_are_dead = True

        for ri in range(len(self.__curMap__)-1, -1, -1):
            row = self.__curMap__[ri]
            ci = 0
            for col in row:
                if ( (col[Game.M_IDX_TYPE]) and (not self.__hasMarbleState__([ci, ri], Game.STATE_DEAD)) ):
                    if ( self.__curMap__[ri][ci][Game.M_IDX_TYPE] == 0 ):
                        self.__curMap__[ri][ci][Game.M_IDX_STATE] = Game.STATE_DEAD
                    elif ( self.__hasMarbleState__([ci, ri], Game.STATE_FALLING) ):
                        all_are_dead = False
                        if ( col[Game.M_IDX_POS][Game.P_IDX_Y] > Game.SCREEN_HEIGHT ):
                            self.__sound_falling__.play()
                            self.__curMap__[ri][ci] = [99999999, 
                                                       0,
                                                       Game.STATE_DEAD, 
                                                       [ self.__curMapRect__.left + (ci * Game.MARBLE_WIDTH),
                                                         self.__curMapRect__.top + (ri * Game.MARBLE_HEIGHT) ],
                                                       [0, 0]
                                                   ]
                            continue
                        col[Game.M_IDX_VEL][Game.P_IDX_Y] += 0.2

                        # OH GOD, MY EYES
                        nextri = (col[Game.M_IDX_POS][Game.P_IDX_Y] + (Game.MARBLE_HEIGHT)) / Game.MARBLE_HEIGHT
                        if ( ( (nextri) >= (len(self.__curMap__)) ) or
                             ( self.__hasMarbleState__([ci, nextri], Game.STATE_FALLING) ) or
                             ( self.__hasMarbleState__([ci, nextri], Game.STATE_DEAD) ) ):
                            col[Game.M_IDX_POS][Game.P_IDX_Y] += int(col[Game.M_IDX_VEL][Game.P_IDX_Y])
                        else:
                            self.__flipMarbles__([ci, ri], [ci, nextri-1])
                            self.__delMarbleState__([ci, nextri-1], Game.STATE_FALLING)
                        # --- THE GOGGLES DO NOTHING
                    elif ( not self.__hasMarbleState__([ci, ri], Game.STATE_DEAD) ):
                        all_are_dead = False
                ci += 1
            ri += 1
        if ( all_are_dead ) and ( self.__gamestate__ == Game.STATE_GAME_TITLE_FALLING ):
            self.__setMap__(maps[self.__mapIndex__])
        elif ( all_are_dead ) and ( self.__gamestate__ == Game.STATE_GAME_MAIN ):
            if ( (self.__mapIndex__ + 1) >= (len(maps)-1) ):
                self.__gamestate__ = Game.STATE_GAME_WIN
                return
            self.__mapIndex__ += 1
            self.__setMap__(levelTitles[self.__mapIndex__], isTitle = True)
        return

    def __draw_marble__(self, mx, my, marble):
        if ( (marble[Game.M_IDX_TYPE] or Game.DEBUG_MODE ) and (marble[Game.M_IDX_STATE] != Game.STATE_DEAD)):
            if self.__hasMarbleState__([mx, my], Game.STATE_DRAGGING):
                mpos = pygame.mouse.get_pos()
                x = mpos[Game.P_IDX_X] - Game.MARBLE_CENTER_X
                y = mpos[Game.P_IDX_Y] - Game.MARBLE_CENTER_Y
            else:
                x = marble[Game.M_IDX_POS][Game.P_IDX_X]
                y = marble[Game.M_IDX_POS][Game.P_IDX_Y]
            if ( marble[Game.M_IDX_TYPE] ):
                self.__blitTarget__.blit(self.__marbles__[marble[Game.M_IDX_TYPE]], (x, y))
            if ( Game.DRAW_MOVES ):
                text = self.__gameFont__.render("{}".format(marble[Game.M_IDX_MOVES]), 1, Game.COLOR_WHITE)
                textpos = text.get_rect(right = x + (Game.MARBLE_WIDTH),
                                        top = y)
                self.__blitTarget__.blit(text, textpos)

            if Game.DEBUG_MODE:
                text = self.__gameFont__.render("{}".format(marble[Game.M_IDX_STATE]), 1, Game.COLOR_WHITE)
                textpos = text.get_rect(left = x,
                                        bottom = y + Game.MARBLE_HEIGHT)
                self.__blitTarget__.blit(text, textpos)
                text = self.__gameFont__.render("{},{}".format(mx, my), 1, Game.COLOR_BLACK)
                textpos = text.get_rect(centerx = x + (Game.MARBLE_WIDTH/2),
                                        centery = y + (Game.MARBLE_HEIGHT/2))
                self.__blitTarget__.blit(text, textpos)

    def __draw__(self):
        self.__display__.fill(Game.COLOR_BLACK)
        self.__blitTarget__.fill(Game.COLOR_MAGICPINK)

        if self.__gamestate__ == Game.STATE_GAME_WIN:
            text = self.__gameFont__.render("CONGLATURATIONS! YOU HAVE COMPLETED A GREAT GAME!", 1, Game.COLOR_WHITE)
            textpos = text.get_rect(centerx = Game.SCREEN_WIDTH / 2,
                                    centery = Game.SCREEN_HEIGHT / 2)
            self.__blitTarget__.blit(text, textpos)

            text = self.__gameFont__.render("NOW GO, AND REST OUR HEROS!", 1, Game.COLOR_WHITE)
            textpos = text.get_rect(centerx = Game.SCREEN_WIDTH / 2,
                                    centery = ( Game.SCREEN_HEIGHT / 2) + 40)
            self.__blitTarget__.blit(text, textpos)

            self.__display__.blit(self.__blitTarget__, (0, 0))
            return

        if not self.__curMap__:
            return

        if self.__gamestate__ == Game.STATE_GAME_MAIN and self.__mapIndex__ == 0:
            y = Game.SCREEN_HEIGHT / 2
            for textline in ["* Make vertical lines of 3 marbles of the same color",
                             "* Click and Drag to Move Marbles",
                             "* Marbles can move horizontal, vertical, and diagonal",
                             "* Marbles can move one space at a time only",
                             "* Lines will collapse onto marbles beneath them",
                             "* Lines will fall completely if there is nothing below them",
                             "* The number shows how many times a marble can be moved",
                             "* Levels end when no more moves can be made",
                             "* Get as many lines off the screen as you can"]:
                text = self.__gameFont__.render(textline, 1, Game.COLOR_WHITE)
                textpos = text.get_rect(left = (Game.SCREEN_WIDTH / 3), 
                                        centery = y)
                self.__blitTarget__.blit(text, textpos)
                y += textpos.height

        drawLast = []
        ri = 0
        for row in self.__curMap__:
            ci = 0
            for col in row:
                if self.__hasMarbleState__([ci, ri], Game.STATE_DRAGGING):
                    drawLast = [ci, ri, col]
                else:
                    self.__draw_marble__(ci, ri, col)
                ci += 1
            ri += 1
            if drawLast:
                self.__draw_marble__(drawLast[0], drawLast[1], drawLast[2])

        if self.__selectionRect__ :
            self.__blitTarget__.blit(
                self.__selectionSurface__, 
                (self.__selectionRect__.left, self.__selectionRect__.top)
                )

        if self.__gamestate__ == Game.STATE_GAME_TITLE and self.__mapIndex__ == 0:
            text = self.__gameFont__.render("Fuck This Collapse", 1, Game.COLOR_WHITE)
            textpos = text.get_rect(centerx = Game.SCREEN_WIDTH / 2,
                                    centery = Game.SCREEN_HEIGHT / 2)
            self.__blitTarget__.blit(text, textpos)

            text = self.__gameFont__.render("for Fuck This Jam", 1, Game.COLOR_WHITE)
            textpos = text.get_rect(centerx = Game.SCREEN_WIDTH / 2,
                                    centery = ( Game.SCREEN_HEIGHT / 2) + (textpos.height * 2))
            self.__blitTarget__.blit(text, textpos)

            text = self.__gameFont__.render("Andrew Kesterson <andrew@aklabs.net>", 1, Game.COLOR_WHITE)
            textpos = text.get_rect(centerx = Game.SCREEN_WIDTH / 2,
                                    centery = ( Game.SCREEN_HEIGHT / 2) + (textpos.height * 3))
            self.__blitTarget__.blit(text, textpos)

            text = self.__gameFont__.render("https://www.github.com/akesterson/", 1, Game.COLOR_WHITE)
            textpos = text.get_rect(centerx = Game.SCREEN_WIDTH / 2,
                                    centery = ( Game.SCREEN_HEIGHT / 2) + (textpos.height * 4))
            self.__blitTarget__.blit(text, textpos)

        self.__display__.blit(self.__blitTarget__, (0, 0))

    def __canSelectMarble__(self, x, y):
        if ( (self.__curMap__[y][x][Game.M_IDX_STATE] == Game.STATE_DEAD) and 
             (not self.__hasMarbleState__(self.__selectedMarble__, Game.STATE_DRAGGING)) ):
            return False
        if self.__selectedMarble__ == [-1, -1]:
            return True
        left = self.__selectedMarble__[Game.P_IDX_X]
        top = self.__selectedMarble__[Game.P_IDX_Y]
        if ( left > 0 ):
            left -= 1
        if ( top > 0 ):
            top -= 1

        selectable = pygame.Rect(left, top, 3, 3)
        return selectable.collidepoint(x, y)

    def __flipMarbles__(self, m1, m2, force=False):
        if ( m1 == m2 ):
            return
        # Skip empty (black) marbles (unless we're dragging or falling)
        if ( ( not self.__hasMarbleState__(self.__selectedMarble__, Game.STATE_DRAGGING)) and
             ( ( not self.__hasMarbleState__(m1, Game.STATE_FALLING)) and
               ( not self.__hasMarbleState__(m2, Game.STATE_FALLING)) ) and
             ( ( self.__curMap__[m1[Game.P_IDX_Y]][m1[Game.P_IDX_X]][Game.M_IDX_TYPE] == 0 ) or
               ( self.__curMap__[m2[Game.P_IDX_Y]][m2[Game.P_IDX_X]][Game.M_IDX_TYPE] == 0 ) )
           ):
            return
        if ( ( self.__curMap__[m1[Game.P_IDX_Y]][m1[Game.P_IDX_X]][Game.M_IDX_MOVES] <= 0 ) or
             ( self.__curMap__[m2[Game.P_IDX_Y]][m2[Game.P_IDX_X]][Game.M_IDX_MOVES] <= 0 ) ):
            return

        # Swap marbles
        tmp = self.__curMap__[m1[Game.P_IDX_Y]][m1[Game.P_IDX_X]]
        self.__curMap__[m1[Game.P_IDX_Y]][m1[Game.P_IDX_X]] = self.__curMap__[m2[Game.P_IDX_Y]][m2[Game.P_IDX_X]]
        self.__curMap__[m2[Game.P_IDX_Y]][m2[Game.P_IDX_X]] = tmp

        # FIX positions of the marbles
        for m in [m1, m2]:
            self.__curMap__[m[Game.P_IDX_Y]][m[Game.P_IDX_X]][Game.M_IDX_POS] = [
                self.__curMapRect__.left + (m[Game.P_IDX_X] * Game.MARBLE_WIDTH),
                self.__curMapRect__.top + (m[Game.P_IDX_Y] * Game.MARBLE_HEIGHT)
            ]
                
        # Decrement movecount remaining on both marbles
        self.__curMap__[m1[Game.P_IDX_Y]][m1[Game.P_IDX_X]][Game.M_IDX_MOVES] -= 1
        self.__curMap__[m2[Game.P_IDX_Y]][m2[Game.P_IDX_X]][Game.M_IDX_MOVES] -= 1

    def __setMarbleState__(self, pos, state):
        self.__curMap__[pos[Game.P_IDX_Y]][pos[Game.P_IDX_X]][Game.M_IDX_STATE] = state

    def __addMarbleState__(self, pos, state):
        cs = self.__curMap__[pos[Game.P_IDX_Y]][pos[Game.P_IDX_X]][Game.M_IDX_STATE]
        cs = ( cs | state )
        self.__curMap__[pos[Game.P_IDX_Y]][pos[Game.P_IDX_X]][Game.M_IDX_STATE] = cs

    def __delMarbleState__(self, pos, state):
        if ( not self.__hasMarbleState__(pos, state) ):
            return
        cs = self.__curMap__[pos[Game.P_IDX_Y]][pos[Game.P_IDX_X]][Game.M_IDX_STATE]
        cs = ( cs ^ state )
        self.__curMap__[pos[Game.P_IDX_Y]][pos[Game.P_IDX_X]][Game.M_IDX_STATE] = cs

    def __hasMarbleState__(self, pos, state):
        return ( (self.__curMap__[pos[Game.P_IDX_Y]][pos[Game.P_IDX_X]][Game.M_IDX_STATE] & state) == state)

    def __setSelectedMarble__(self, pos):
        if self.__selectedMarble__ != [-1, -1]:
            self.__delMarbleState__(self.__selectedMarble__, Game.STATE_SELECTED)
        self.__selectedMarble__ = pos
        if pos == [-1, -1]:
            self.__selectionRect__ = None
            return
        if ((self.__curMap__) and (self.__curMap__[pos[Game.P_IDX_Y]][pos[Game.P_IDX_X]][Game.M_IDX_STATE] == Game.STATE_DEAD)):
            self.__setSelectedMarble__([-1, -1])
            return
        self.__selectionRect__ = pygame.Rect(
            (self.__curMapRect__.left + (pos[Game.P_IDX_X] * Game.MARBLE_WIDTH)),
            (self.__curMapRect__.top + (pos[Game.P_IDX_Y] * Game.MARBLE_HEIGHT)),
            Game.MARBLE_WIDTH,
            Game.MARBLE_HEIGHT)
        self.__addMarbleState__(pos, Game.STATE_SELECTED)

    def __mouseReleased__(self, event):
        if self.__gamestate__ == Game.STATE_GAME_WIN:
            return
        elif self.__gamestate__ == Game.STATE_GAME_TITLE:
            return
        elif self.__gamestate__ == Game.STATE_GAME_TITLE_FALLING:
            return

        self.__sound_click__.play()

        mouse_x = event.pos[Game.P_IDX_X]
        mouse_y = event.pos[Game.P_IDX_Y]
        marble_x = ( (mouse_x - self.__curMapRect__.left) / Game.MARBLE_WIDTH)
        marble_y = ( (mouse_y - self.__curMapRect__.top) / Game.MARBLE_HEIGHT)

        if ( ( not self.__curMapRect__.collidepoint((mouse_x, mouse_y)) )  or
             ( (not self.__hasMarbleState__(self.__selectedMarble__, Game.STATE_DRAGGING)) and
               self.__curMap__[marble_y][marble_x][Game.M_IDX_TYPE] == 0 ) 
        ):
            self.__delMarbleState__(self.__selectedMarble__, Game.STATE_SELECTED)
            self.__delMarbleState__(self.__selectedMarble__, Game.STATE_DRAGGING)
            self.__setSelectedMarble__([-1, -1])
            self.__selectionRect__ = None
            return

        if event.button == 1:
            if self.__hasMarbleState__(self.__selectedMarble__,
                                       Game.STATE_DRAGGING):
                flipMarble = self.__selectedMarble__
                if not self.__canSelectMarble__(marble_x, marble_y):
                    self.__delMarbleState__(self.__selectedMarble__, Game.STATE_DRAGGING)
                    self.__delMarbleState__(self.__selectedMarble__, Game.STATE_SELECTED)
                    self.__setSelectedMarble__([-1, -1])
                    return
                self.__addMarbleState__(flipMarble, Game.STATE_PLAYERTOUCHED)
                self.__addMarbleState__([marble_x, marble_y], Game.STATE_PLAYERTOUCHED)
                self.__flipMarbles__(flipMarble, [marble_x, marble_y])
                self.__setSelectedMarble__([-1, -1])
                for marble in [[marble_x, marble_y], flipMarble]:
                    for state in [Game.STATE_SELECTED, Game.STATE_DRAGGING]:
                        self.__delMarbleState__(marble, state)
                        
                self.__setGroupState__()
            else:
                self.__setSelectedMarble__([marble_x, marble_y])
                self.__addMarbleState__([marble_x, marble_y], Game.STATE_PLAYERTOUCHED)
                self.__setGroupState__()
        return

    def __mouseClicked__(self, event):
        self.__sound_click__.play()

        if self.__gamestate__ == Game.STATE_GAME_WIN:
            return
        elif self.__gamestate__ == Game.STATE_GAME_TITLE:
            self.__sound_falling__.play()
            self.__gamestate__ = Game.STATE_GAME_TITLE_FALLING
            for row in self.__curMap__:
                for col in row:
                    col[Game.M_IDX_STATE] = Game.STATE_PLAYERTOUCHED | Game.STATE_FALLING
            return

        mouse_x = event.pos[Game.P_IDX_X]
        mouse_y = event.pos[Game.P_IDX_Y]
        marble_x = ( (mouse_x - self.__curMapRect__.left) / Game.MARBLE_WIDTH)
        marble_y = ( (mouse_y - self.__curMapRect__.top) / Game.MARBLE_HEIGHT)

        if ( ( not self.__curMapRect__.collidepoint((mouse_x, mouse_y)))  or
             (self.__curMap__[marble_y][marble_x][Game.M_IDX_TYPE] == 0 ) ):
            # We can't drag empty space or space outside the map
            return
        
        if not self.__canSelectMarble__(marble_x, marble_y):
            return
        self.__setSelectedMarble__([marble_x, marble_y])
        self.__addMarbleState__([marble_x, marble_y], Game.STATE_DRAGGING)
        self.__addMarbleState__([marble_x, marble_y], Game.STATE_PLAYERTOUCHED)

    def __setGroupState__(self, zap=False):
        amount_by_type_with_moves = {
            1: 0,
            2: 0,
            3: 0,
            4: 0
        }
        groups = {
            0: [],
            1: [],
            2: [],
            3: [],
            4: []
        }
        groups_of_3 = [
            [],
            [],
            [],
            [],
            []
        ]
        x = 0
        y = 0
        curMatchMarble = 0
        prevy = 0
        group = None
        for row in self.__curMap__: 
            x = 0
            for col in row:
                if col[Game.M_IDX_TYPE] != 0:
                    if col[Game.M_IDX_MOVES] > 0 and col[Game.M_IDX_MOVES] < 99 :
                        amount_by_type_with_moves[col[Game.M_IDX_TYPE]] += 1
                    candidates = [
                                        # --X--
                        [x, y + 1]      # --C--
                    ]
                    for c in candidates:
                        cx = c[Game.P_IDX_X]
                        cy = c[Game.P_IDX_Y]
                        if ( (cy >= len(self.__curMap__)) or
                             (cy < 0 ) or
                             (cx >= len(self.__curMap__[cy])) or
                             (cx < 0 ) ):
                             continue
                        if ( self.__curMap__[cy][cx][Game.M_IDX_TYPE] == col[Game.M_IDX_TYPE] ):
                            curMatchMarble = col[Game.M_IDX_TYPE]
                            group = None
                            for group in groups[curMatchMarble]:
                                if ( ( [cx, cy] in group ) or 
                                     ( [x, y] in group ) ):
                                    break
                                group = None
                            if not group:
                                group = [[x, y]]
                                groups[curMatchMarble].append(group)
                            if [cx, cy] in group:
                                group.append([x, y])
                            else:
                                group.append([cx, cy])

                x += 1
            y += 1

        game_can_continue = False
        for k, v in amount_by_type_with_moves.iteritems():
            if v >= 3:
                game_can_continue = True
        if not game_can_continue:
            for row in self.__curMap__:
                for col in row:
                    col[Game.M_IDX_STATE] = Game.STATE_DEAD

        for marble, group in groups.iteritems():
            for grp in group:
                if len(grp) < 3:
                    continue
                # At least one marble in the set has to have been touched by the player
                for tpair in grp:
                    if self.__hasMarbleState__([tpair[Game.P_IDX_X], tpair[Game.P_IDX_Y]],
                                               Game.STATE_PLAYERTOUCHED):
                        break
                    tpair = None
                if not tpair:
                    continue

                for pair in grp:
                    if self.__hasMarbleState__([tpair[Game.P_IDX_X], tpair[Game.P_IDX_Y]],
                                               Game.STATE_SELECTED):
                        self.__setSelectedMarble__([-1, -1])
                    if zap:
                        self.__curMap__[pair[Game.P_IDX_Y]][pair[Game.P_IDX_X]][Game.M_IDX_STATE] = Game.STATE_DEAD
                    else:
                        self.__addMarbleState__(pair, Game.STATE_FALLING)

    def run(self):
        while True:
            self.__update__()
            self.__draw__()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                elif event.type == pygame.KEYUP:
                    if ( Game.DEBUG_MODE ):
                        if ( (pygame.key.get_pressed()[pygame.K_LCTRL]) and 
                             (event.key == pygame.K_LEFT) and
                             (self.__mapIndex__ > 0) ):
                            self.__mapIndex__ -= 1
                            self.__setMap__(maps[self.__mapIndex__])
                            self.__setSelectedMarble__([-1, -1])
                        elif ( (pygame.key.get_pressed()[pygame.K_LCTRL]) and 
                               (event.key == pygame.K_RIGHT) and
                               (self.__mapIndex__ < (len(maps)-1))):
                            self.__mapIndex__ += 1
                            self.__setMap__(maps[self.__mapIndex__])
                            self.__setSelectedMarble__([-1, -1])
                        
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.__mouseClicked__(event)
                elif event.type == pygame.MOUSEBUTTONUP:
                    self.__mouseReleased__(event)
            pygame.display.update()
        return

def main(argc, argv):
    game = Game()
    return game.run()

if __name__ == "__main__":
    sys.exit(main(len(sys.argv), sys.argv))
