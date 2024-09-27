class Block:
    def __init__(self):
        pass
        

class Components:
    def __init__(self):
        pass
       
        
class Screen:
    def __init__(self):
        self.screen_body = []
        self.screen_width = 10
        self.screen_height = 20
    
    
    def display_edge(self, x, y):
        print('\t<!', end='')
        for i in range(x * 2 + 1):
            print('=', end='')
        print('!>')
        
    
    def set_screen_body(self) -> None:
        for i in range(self.screen_height):
            element = ". "
            row = []
            for j in range(self.screen_width):
                row.append(element)
            self.screen_body.append(row)
            
      
    def display_screen(self):
        
        x = self.screen_width
        y = self.screen_height
        
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
    
    
    def run(self):
        pass
    
    
def main():
    screen: Screen = Screen()
    
    screen.display_screen()
    
if __name__ == '__main__':
    main()
    