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

    STATE_NONE = 0
    STATE_FALLING = 1
    STATE_SELECTED = 2
    STATE_DEAD = 3

    M_IDX_MOVES = 0
    M_IDX_TYPE = 1
    M_IDX_STATE = 2
    M_IDX_POS = 3
    M_IDX_VEL = 4

    P_IDX_X = 0
    P_IDX_Y = 1

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

        self.__setSelectedMarble__([-1, -1])
        self.__selectionRect__ = None
        self.__selectionSurface__ = pygame.Surface(
            (Game.MARBLE_WIDTH, Game.MARBLE_HEIGHT),
            pygame.SRCALPHA | pygame.HWSURFACE)
        self.__selectionSurface__.fill((255,255,255, 128))

        self.__gameFont__ = pygame.font.SysFont(pygame.font.get_default_font(), 18)

        self.__mapIndex__ = 0
        self.__setMap__(maps[self.__mapIndex__])

    def __load_marbles__(self):
        self.__marbles__.append(None)
        self.__marbles__.append(pygame.image.load('gfx/BlueSwirl.png'))
        self.__marbles__.append(pygame.image.load('gfx/MochaVolcano.png'))
        self.__marbles__.append(pygame.image.load('gfx/SwirlyEyeball.png'))
        self.__marbles__.append(pygame.image.load('gfx/ZebraGum.png'))

    def __setMap__(self, maparray):
        self.__curMap__ = []
        self.__curMapRect__ = pygame.Rect(
            ((Game.SCREEN_WIDTH - (Game.MARBLE_WIDTH * len(maparray[0])))/2),
            ((Game.SCREEN_HEIGHT - (Game.MARBLE_HEIGHT * len(maparray)))/2),
            (Game.MARBLE_WIDTH * len(maparray[0])),
            (Game.MARBLE_HEIGHT * len(maparray))
        )

        x = self.__curMapRect__.left
        y = self.__curMapRect__.top
        for row in maparray:
            x = self.__curMapRect__.left
            mrow = []
            self.__curMap__.append(mrow) 
            for col in row:
                mrow.append(
                    [self.__maxMarbleMoves__, 
                     col, 
                     Game.STATE_NONE, 
                     [x, y], 
                     [0, 0]])
                x += Game.MARBLE_WIDTH
            y += Game.MARBLE_HEIGHT

    def __update__(self):
        return

    def __draw__(self):
        self.__display__.fill(Game.COLOR_BLACK)
        self.__blitTarget__.fill(Game.COLOR_MAGICPINK)
        if not self.__curMap__:
            return
        for row in self.__curMap__:
            for col in row:
                if col[Game.M_IDX_TYPE]:
                    x = col[Game.M_IDX_POS][Game.P_IDX_X]
                    y = col[Game.M_IDX_POS][Game.P_IDX_Y]
                    self.__blitTarget__.blit(self.__marbles__[col[Game.M_IDX_TYPE]], (x, y))
                    text = self.__gameFont__.render("{}".format(col[Game.M_IDX_MOVES]), 1, Game.COLOR_WHITE)
                    textpos = text.get_rect(right = x + (Game.MARBLE_WIDTH),
                                            top = y)
                    self.__blitTarget__.blit(text, textpos)
        if self.__selectionRect__ :
            self.__blitTarget__.blit(
                self.__selectionSurface__, 
                (self.__selectionRect__.left, self.__selectionRect__.top)
                )
        self.__display__.blit(self.__blitTarget__, (0, 0))

    def __canSelectMarble__(self, x, y):
        if self.__selectedMarble__ == [-1, -1]:
            return True
        curx = self.__selectedMarble__[Game.P_IDX_X]
        cury = self.__selectedMarble__[Game.P_IDX_Y]
        selectable = [
            [curx, cury - 1],     # --S--
            [curx - 1, cury],     # -SX--
            [curx + 1, cury],     # --XS-
            [curx, cury + 1]      # --S--
        ]
        if [x, y] not in selectable:
            return False
        if self.__curMap__[y][x][Game.M_IDX_STATE] != Game.STATE_NONE:
            return False
        return True

    def __flipMarbles__(self, m1, m2):
        if self.__selectedMarble__ == [-1, -1]:
            return
        # Skip empty (black) marbles
        if ( ( self.__curMap__[m1[Game.P_IDX_Y]][m1[Game.P_IDX_X]][Game.M_IDX_TYPE] == 0 ) or
             ( self.__curMap__[m2[Game.P_IDX_Y]][m2[Game.P_IDX_X]][Game.M_IDX_TYPE] == 0 ) ):
            return

        # Swap marbles
        tmp = self.__curMap__[m1[Game.P_IDX_Y]][m1[Game.P_IDX_X]]
        self.__curMap__[m1[Game.P_IDX_Y]][m1[Game.P_IDX_X]] = self.__curMap__[m2[Game.P_IDX_Y]][m2[Game.P_IDX_X]]
        self.__curMap__[m2[Game.P_IDX_Y]][m2[Game.P_IDX_X]] = tmp

        # Swap positions of the marbles
        tmp = self.__curMap__[m1[Game.P_IDX_Y]][m1[Game.P_IDX_X]][Game.M_IDX_POS]
        self.__curMap__[m1[Game.P_IDX_Y]][m1[Game.P_IDX_X]][Game.M_IDX_POS] = self.__curMap__[m2[Game.P_IDX_Y]][m2[Game.P_IDX_X]][Game.M_IDX_POS]
        self.__curMap__[m2[Game.P_IDX_Y]][m2[Game.P_IDX_X]][Game.M_IDX_POS] = tmp

        # Decrement movecount remaining on both marbles
        self.__curMap__[m1[Game.P_IDX_Y]][m1[Game.P_IDX_X]][Game.M_IDX_MOVES] -= 1
        self.__curMap__[m2[Game.P_IDX_Y]][m2[Game.P_IDX_X]][Game.M_IDX_MOVES] -= 1
        self.__setSelectedMarble__(m2)

    def __setMarbleState__(self, x, y, state):
        self.__curMap__[y][x][2] = state

    def __setSelectedMarble__(self, pos):
        self.__selectedMarble__ = pos
        if pos == [-1, -1]:
            self.__selectionRect__ = None
            return
        self.__selectionRect__ = pygame.Rect(
            (self.__curMapRect__.left + (pos[Game.P_IDX_X] * Game.MARBLE_WIDTH)),
            (self.__curMapRect__.top + (pos[Game.P_IDX_Y] * Game.MARBLE_HEIGHT)),
            Game.MARBLE_WIDTH,
            Game.MARBLE_HEIGHT)
        self.__setMarbleState__(pos[Game.P_IDX_X], pos[Game.P_IDX_Y], Game.STATE_SELECTED)

    def __mouseClicked__(self, event):
        mouse_x = event.pos[Game.P_IDX_X]
        mouse_y = event.pos[Game.P_IDX_Y]
        marble_x = ( (mouse_x - self.__curMapRect__.left) / Game.MARBLE_WIDTH)
        marble_y = ( (mouse_y - self.__curMapRect__.top) / Game.MARBLE_HEIGHT)

        if ( ( not self.__curMapRect__.collidepoint((mouse_x, mouse_y)))  or
             (self.__curMap__[marble_y][marble_x][Game.M_IDX_TYPE] == 0 ) ):
            if self.__curMap__[self.__selectedMarble__[Game.P_IDX_Y]][self.__selectedMarble__[Game.P_IDX_X]][2] == Game.STATE_SELECTED :
                self.__curMap__[self.__selectedMarble__[Game.P_IDX_Y]][self.__selectedMarble__[Game.P_IDX_X]][2] = Game.STATE_NONE
            self.__setSelectedMarble__([-1, -1])
            self.__selectionRect__ = None
            return
        if self.__curMap__[marble_y][marble_x][Game.M_IDX_TYPE] == 0:
            return False
        if event.button == 1:
            self.__setSelectedMarble__([marble_x, marble_y])
        elif event.button in [2, 3]:
            if not self.__canSelectMarble__(marble_x, marble_y):
                return
            self.__flipMarbles__(self.__selectedMarble__, [marble_x, marble_y])
            #self.__setGroupState__()
        return

    def __setGroupState__(self):
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
                    candidates = [
                        [x, y - 1],     # --C--
                        [x - 1, y],     # -CX--
                        [x + 1, y],     # --XC-
                        [x, y + 1]      # --C--
                    ]
                    for c in candidates:
                        if self.__curMap__[c[Game.P_IDX_Y]][c[Game.P_IDX_X]][Game.M_IDX_TYPE] == col[Game.M_IDX_TYPE]:
                            if ( (prevy != y and curMatchMarble != col[Game.M_IDX_TYPE]) or
                                 (prevy != y) ):
                                curMatchMarble = col[Game.M_IDX_TYPE]
                                group = None
                                for group in groups[curMatchMarble]:
                                    if ( ( [c[Game.P_IDX_Y], c[Game.P_IDX_X]] in group ) or 
                                         ( self.__curMap__[c[Game.P_IDX_Y]][c[Game.P_IDX_X]] in group ) ):
                                        break
                                if not group:
                                    group = [[c[Game.P_IDX_Y], c[Game.P_IDX_X]]]
                                    groups[curMatchMarble].append(group)
                                group.append([self.__curMap__[c[Game.P_IDX_Y]][c[Game.P_IDX_X]]])
                x += 1
            prevy = y
            y += 1
        # Go through all the matches, and make sets of all the marbles in groups > 3
        for marble, group in groups.iteritems():
            for grp in group:
              if len(grp) > 2:
                  groups_of_3[marble] += grp
        for group in groups_of_3:
            for pair in set(group):
                self.__curMap__[pair[Game.P_IDX_Y]][pair[Game.P_IDX_X]][2] = Game.STATE_FALLING

    def run(self):
        while True:
            self.__update__()
            self.__draw__()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                elif event.type == pygame.KEYUP:
                    if ( (pygame.key.get_pressed()[pygame.K_LCTRL]) and 
                         (event.key == pygame.K_LEFT) and
                         (self.__mapIndex__ > 0) ):
                        self.__mapIndex__ -= 1
                        self.__setMap__(maps[self.__mapIndex__])
                    elif ( (pygame.key.get_pressed()[pygame.K_LCTRL]) and 
                           (event.key == pygame.K_RIGHT) and
                           (self.__mapIndex__ < (len(maps)-1))):
                        self.__mapIndex__ += 1
                        self.__setMap__(maps[self.__mapIndex__])
                        

                elif event.type == pygame.MOUSEBUTTONUP:
                    self.__mouseClicked__(event)
            pygame.display.update()
        return
