#! python 2.7.8

# knight.py

class Knight:

    # does it make sense to use an immutable type here?
    candidates = {
        1 : (8, 6),
        2 : (7, 9),
        3 : (4, 8),
        4 : (3, 9, 0),
        6 : (7, 1, 0), 
        7 : (6, 2),
        8 : (3, 1),
        9 : (4, 2),
        0 : (4, 6)
    }

    # stores intermediate moves
    moves = list()

    def __init__(self, start, target, total_moves):
        if (start == 5 or target == 5):
            print ('Invalid position reached. Done.')
            exit(1)

        # `start` contains a list of all the possible places 
        # that the knight can move. Initially `start` is only
        # one element long, but grows as the program is executed.
        self.start = [start]

        self.target = target
        self.total_moves = total_moves  

    def move(self):
        starting_points = self.start

        new_starting_points = []

        sub_moves = []

        i = 0
        while(starting_points):
            r = starting_points.pop()
            for destination in self.candidates[r]:
                sub_moves.append((destination, r))
                new_starting_points.append(destination)

        
        self.moves.append(sub_moves)
        self.start = new_starting_points
        self.total_moves -= 1

    def solve(self):
        while (self.total_moves > 0):
            self.move()

        last = len(self.moves) - 1
        valid = []

        # print (self.moves[last])

        for potential_target in (self.moves[last]):        
            if (self.target == potential_target[0]):                
                valid.append(potential_target)
                continue

        if (len(valid) == 0):
            print ('Target not found. Trace failed. Done.')

        print (len(valid))

if __name__ == '__main__':
    k = Knight(1, 4, 5)
    k.solve()
