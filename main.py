class Block:
    def __init__(self):
        pass
        

class Components:
    def __init__(self):
        pass
       
        
class Screen:
    def __init__(self):
        self.screen_width = 10
        self.screen_height = 20
    
    def display_edges(self, x, y):
        print('\t<!', end='')
        for i in range(x * 2 + 1):
            print('=', end='')
        print('!>')
    
    
    def display_screen(self):
        
        x = self.screen_width
        y = self.screen_height
        
        self.display_edges(x, y)
        
        for i in range(y):
            print("\t<! ", end='')
            for j in range(x):
                print('. ', end='')
            print("!>")
            
        self.display_edges(x, y)


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