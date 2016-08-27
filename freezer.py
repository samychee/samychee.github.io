from flask_frozen import Freezer
from project import gchee

freezer = Freezer(gchee.app)

if __name__ == '__main__':
    freezer.freeze()

