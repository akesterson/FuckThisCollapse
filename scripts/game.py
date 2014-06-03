import fuckthiscollapse.Game
import sys

def main(argc, argv):
    game = fuckthiscollapse.Game.Game()
    return game.run()

if __name__ == "__main__":
    sys.exit(main(len(sys.argv), sys.argv))
