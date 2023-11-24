class Snake():

    def __init__(self, lst) -> None:
        self.x = lst[0][0]
        self.y = lst[0][1]
        self.body = lst
    
    def move(self, new_dir):
        pass