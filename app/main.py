class Battleship:
    def __init__(self, ships):
        self.ship_fields = {}
        self.field = {}
        self.next_id = 0

        for start, end in ships:
            coords = []

            if start[0] == end[0]:
                for y in range(min(start[1], end[1]), max(start[1], end[1]) + 1):
                    coords.append((start[0], y))
            elif start[1] == end[1]:
                for x in range(min(start[0], end[0]), max(start[0], end[0]) + 1):
                    coords.append((x, start[1]))

            ship_id = self.next_id
            self.next_id += 1

            self.ship_fields[ship_id] = coords.copy()
            for coord in coords:
                self.field[coord] = ship_id

    def fire(self, location):
        if location not in self.field:
            return "Miss!"

        ship_id = self.field[location]

        if location in self.ship_fields[ship_id]:
            self.ship_fields[ship_id].remove(location)

        if not self.ship_fields[ship_id]:
            return "Sunk!"
        else:
            return "Hit!"
