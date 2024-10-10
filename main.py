import os
from time import sleep
from pynput import keyboard

def clear():
    os.system('clear')
    
def delay():
    sleep(0.1)


class Block:
    def __init__(self):
        self.block = '[]'
        

class Components:
    def __init__(self):
        self.block = Block()
        self.screen = Screen()

    def square(self, screen, x, y, content=Block().block):
        screen[y][x] = content
        screen[y][x + 1] = content
        if y > 0:
            screen[y - 1][x] = content
            screen[y - 1][x + 1] = content
       
        
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
        self.screen = Screen()
        self.block = Block()
        self.component = Components()
        self.width = self.screen.screen_width
        self.height = self.screen.screen_height
        self.x = self.width // 2
        self.y = self.height
        self.component_position = [self.y, self.x]
        self.listener = keyboard.Listener(on_press=self.on_press)
    
    def move_component(self, dx):
        new_x = self.component_position[1] + dx
        if 0 <= new_x < self.width - 1:
            self.component_position[1] = new_x

    def on_press(self, key):
        if key == keyboard.Key.esc:
            return False  # Exit the listener
        elif key == keyboard.Key.left:
            self.move_component(-1)
        elif key == keyboard.Key.right:
            self.move_component(1)
    
    
    def run(self) -> None:
        self.listener.start()  # Start the listener
        running: bool = True

        block = self.block
        component = self.component
        
        screen_list = self.screen.screen_body
        block = block.block
        x: int = self.component_position[1]
        y: int = self.component_position[0]
        dot = '. '
    
        self.screen.display_screen()
        while(running):
            for dy in range(0, y, 1):
                if screen_list[dy + 1][self.component_position[1]] == '[]' and dy == 0:
                    running = False
                 
                component.square(screen_list, self.component_position[1], dy)
                clear()
                
                self.screen.display_screen()
                if screen_list[dy + 1][self.component_position[1]] == '[]' or dy == y - 1:
                    break
                
                component.square(screen_list, self.component_position[1], dy, dot)
                delay()
        
        print("Game over!")
    
    
def main() -> None:
    tetris: Tetris = Tetris()
    tetris.run()
    
if __name__ == '__main__':
    main()
    