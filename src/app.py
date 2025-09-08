import sys
from os import path
sys.path.insert(0, path.abspath(path.dirname(__file__)))

from window import Window


def main() -> None:
    
    window = Window()
    

    window.mainloop()
if __name__ == "__main__":
    main()

    

