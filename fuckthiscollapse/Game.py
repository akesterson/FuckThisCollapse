import pygame
import json
import copy

maps = [
    [
        [1,2,3,4,1,2,3,4,1,2,3,4],
        [1,2,3,4,1,2,3,4,1,2,3,4],
        [1,2,3,4,1,2,3,4,1,2,3,4],
        [1,2,3,4,1,2,3,4,1,2,3,4]
    ],
    [
        [1,1,3,4,1,2,3,4,1,2,3,4],
        [1,1,3,4,2,2,2,4,1,2,3,4],
        [1,1,3,4,1,2,3,4,1,2,3,4],
        [1,1,3,4,1,1,3,4,1,2,3,4]
    ],
    [
        [0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,1,3,0,0,3,3,0,0,0],
        [0,0,0,4,2,0,0,4,1,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,1,0,0,0,0,0,0,3,0,0],
        [0,0,0,3,0,0,0,0,1,0,0,0],
        [0,0,0,0,4,2,3,4,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0]
    ]
]

class Game:
    MARBLE_WIDTH = 40
    MARBLE_HEIGHT = 40
    COLOR_MAGICPINK = (255, 0, 255, 0)
    COLOR_WHITE = (255, 255, 255, 255)
    COLOR_BLACK = (0, 0, 0, 255)
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600
    STATE_FALLING = 0
    STATE_NONE = 1
    STATE_SELECTED = 2
    STATE_DEAD = 3

    def __init__(self):
        pygame.init()
        self.__display__ = pygame.display.set_mode((Game.SCREEN_WIDTH, Game.SCREEN_HEIGHT))
        self.__blitTarget__ = self.__display__.convert_alpha()
        self.__marbles__ = []
        pygame.display.set_caption("Fuck This Collapse")
        self.__load_marbles__()
        self.__curMap__ = None
        self.__curMapRect__ = None
        self.__moves__ = 0
        self.__maxMarbleMoves__ = 4

        self.__selectedMarble__ = [-1, -1]
        self.__selectionRect__ = None
        self.__selectionSurface__ = pygame.Surface(
            (Game.MARBLE_WIDTH, Game.MARBLE_HEIGHT),
            pygame.SRCALPHA | pygame.HWSURFACE)
        self.__selectionSurface__.fill((255,255,255, 128))

        self.__gameFont__ = pygame.font.SysFont(pygame.font.get_default_font(), 18)

        self.__setMap__(maps[2])

    def __load_marbles__(self):
        self.__marbles__.append(None)
        self.__marbles__.append(pygame.image.load('gfx/BlueSwirl.png'))
        self.__marbles__.append(pygame.image.load('gfx/MochaVolcano.png'))
        self.__marbles__.append(pygame.image.load('gfx/SwirlyEyeball.png'))
        self.__marbles__.append(pygame.image.load('gfx/ZebraGum.png'))

    def __setMap__(self, maparray):
        self.__curMap__ = []
        for row in maparray:
            mrow = []
            self.__curMap__.append(mrow)
            for col in row:
                mrow.append([self.__maxMarbleMoves__, col, Game.STATE_NONE, 0])

        self.__curMapRect__ = pygame.Rect(
            ((Game.SCREEN_WIDTH - (Game.MARBLE_WIDTH * len(self.__curMap__[0])))/2),
            ((Game.SCREEN_HEIGHT - (Game.MARBLE_HEIGHT * len(self.__curMap__)))/2),
            (Game.MARBLE_WIDTH * len(self.__curMap__[0])),
            (Game.MARBLE_HEIGHT * len(self.__curMap__))
        )

    def __draw__(self):
        self.__display__.fill(Game.COLOR_BLACK)
        self.__blitTarget__.fill(Game.COLOR_MAGICPINK)
        if not self.__curMap__:
            return
        x = self.__curMapRect__.left
        y = self.__curMapRect__.top
        for row in self.__curMap__:
            x = self.__curMapRect__.left
            for col in row:
                if col[1]:
                    self.__blitTarget__.blit(self.__marbles__[col[1]], (x, y))
                    text = self.__gameFont__.render("{}".format(col[0]), 1, Game.COLOR_WHITE)
                    textpos = text.get_rect(right = x + (Game.MARBLE_WIDTH),
                                            top = y)
                    self.__blitTarget__.blit(text, textpos)
                x += Game.MARBLE_WIDTH
            y += Game.MARBLE_HEIGHT
        if self.__selectionRect__ :
            self.__blitTarget__.blit(
                self.__selectionSurface__, 
                (self.__selectionRect__.left, self.__selectionRect__.top)
                )
        self.__display__.blit(self.__blitTarget__, (0, 0))

    def __canSelectMarble__(self, x, y):
        if self.__selectedMarble__ == [-1, -1]:
            return True
        curx = self.__selectedMarble__[0]
        cury = self.__selectedMarble__[1]
        selectable = [
            [curx, cury - 1],     # --S--
            [curx - 1, cury],     # -SX--
            [curx + 1, cury],     # --XS-
            [curx, cury + 1]      # --S--
        ]
        print selectable
        if [x, y] not in selectable:
            print "Marble at ({}, {}) is not my neighbor".format(x, y)
            return False
        #if self.__curMap__[y][x] != self.__curMap__[cury][curx] :
        #    print "Neighbor at ({}, {}) is type {} while I am {}".format(x, y,  self.__curMap__[cury][curx], self.__curMap__[y][x])
        #    return False
        return True

    def __flipMarbles__(self, m1, m2):
        if self.__selectedMarble__ == [-1, -1]:
            return
        if ( ( self.__curMap__[m1[1]][m1[0]][0] == 0 ) or
             ( self.__curMap__[m2[1]][m2[0]][0] == 0 ) ):
            print "No moves left on one of these marbles"
            return
        print "Flipping ({} = {}) and ({} = {})".format(
            m1, 
            self.__curMap__[m1[1]][m1[0]],
            m2,
            self.__curMap__[m2[1]][m2[0]])
        self.__curMap__[m1[1]][m1[0]][0] -= 1
        self.__curMap__[m2[1]][m2[0]][0] -= 1
        tmp = self.__curMap__[m1[1]][m1[0]][1]
        self.__curMap__[m1[1]][m1[0]][1] = self.__curMap__[m2[1]][m2[0]][1]
        self.__curMap__[m2[1]][m2[0]][1] = tmp
        tmp = self.__curMap__[m1[1]][m1[0]][0]
        self.__curMap__[m1[1]][m1[0]][0] = self.__curMap__[m2[1]][m2[0]][0]
        self.__curMap__[m2[1]][m2[0]][0] = tmp
        print "Flipped ({} = {}) and ({} = {})".format(
            m1, 
            self.__curMap__[m1[1]][m1[0]],
            m2,
            self.__curMap__[m2[1]][m2[0]])

    def __setMarbleState__(self, x, y, state):
        self.__curMap__[y][x][2] = state

    def __mouseClicked__(self, event):
        mouse_x = event.pos[0]
        mouse_y = event.pos[1]
        marble_x = ( (mouse_x - self.__curMapRect__.left) / Game.MARBLE_WIDTH)
        marble_y = ( (mouse_y - self.__curMapRect__.top) / Game.MARBLE_HEIGHT)
        if ( ( not self.__curMapRect__.collidepoint((mouse_x, mouse_y)))  or
             (self.__curMap__[marble_y][marble_x][1] == 0 ) ):
            if self.__curMap__[self.__selectedMarble__[1]][self.__selectedMarble__[0]][2] == Game.STATE_SELECTED :
                self.__curMap__[self.__selectedMarble__[1]][self.__selectedMarble__[0]][2] = Game.STATE_NONE
            self.__selectedMarble__ = [-1, -1]
            self.__selectionRect__ = None
            return
        if self.__curMap__[marble_y][marble_x][1] == 0:
            return False
        if event.button == 1:
            print "Selected marble [{}, {}]".format(marble_x, marble_y)
            self.__selectedMarble__ = [marble_x, marble_y]
            self.__selectionRect__ = pygame.Rect(
                (self.__curMapRect__.left + (marble_x * Game.MARBLE_WIDTH)),
                (self.__curMapRect__.top + (marble_y * Game.MARBLE_HEIGHT)),
                Game.MARBLE_WIDTH,
                Game.MARBLE_HEIGHT)
            self.__setMarbleState__(marble_x, marble_y, Game.STATE_SELECTED)
        elif event.button in [2, 3]:
            if not self.__canSelectMarble__(marble_x, marble_y):
                print "Silly rabbit, you can't select that marble!"
                return
            self.__flipMarbles__(self.__selectedMarble__, [marble_x, marble_y])
        return

    def run(self):
        while True:
            self.__draw__()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                if event.type == pygame.MOUSEBUTTONUP:
                    self.__mouseClicked__(event)
            pygame.display.update()
        return
