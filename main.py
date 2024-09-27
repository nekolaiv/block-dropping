import os
from time import sleep

def clear():
    os.system('clear')
    
def delay():
    sleep(0.5)


class Block:
    def __init__(self):
        self.block = '[]'
        

class Components:
    def __init__(self):
        pass
       
        
class Screen:
    def __init__(self, screen_width=10, screen_height=20) -> None:
        self.screen_body = []
        self.screen_width = screen_width
        self.screen_height = screen_height
    
    
    def display_edge(self, x, y) -> None:
        print('\t<!', end='')
        for i in range(x * 2 + 1):
            print('=', end='')
        print('!>')
        
    
    def set_screen_body(self) -> None:
        for i in range(self.screen_height):
            element: string = ". "
            row: list(string) = []
            for j in range(self.screen_width):
                row.append(element)
            self.screen_body.append(row)
            
      
    def display_screen(self) -> None:
        
        x: int = self.screen_width
        y: int = self.screen_height
        
        self.set_screen_body()
        
        self.display_edge(x, y)
        
        for i in range(y):
            print("\t<! ", end='')
            for j in range(x):
                print(self.screen_body[i][j], end='')
            print("!>")
            
        self.display_edge(x, y)


class Tetris:
    def __init__(self):
        pass
    
    def move(self):
        pass
        
    
    
    def run(self) -> None:
        running: bool = True
        
        block: Block = Block()
        screen: Screen = Screen()
        screen_list: list = screen.screen_body
        
        block = block.block
        x: int = screen.screen_width
        y: int = screen.screen_height
        mid: int = x // 2
    
        screen.display_screen()
        
        while(running):
            for i in range(0, y, 1):
                 temp = screen_list[i][mid]
                 screen_list[i][mid] = block
                 clear()
                 screen.display_screen()
                 screen_list[i][mid] = temp
                 delay()
               
            running = False

    
def main() -> None:
    tetris: Tetris = Tetris()
    tetris.run()
    
if __name__ == '__main__':
    main()