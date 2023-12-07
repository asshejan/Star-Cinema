class Star_Cinema:

    def __init__(self):
        self._hall_list = []

    def entry_hall(self, hall):
        self._hall_list.append(hall)

    def view_all_shows(self):
        for hall in self._hall_list:
            hall.view_show_list()


class Hall:

    def __init__(self, rows, cols, hall_no):
        self._seats = {}
        self._show_list = []
        self._rows = rows
        self._cols = cols
        self._hall_no = hall_no
        Star_Cinema().entry_hall(self)

    def entry_show(self, id, movie_name, time):
        self._show_list.append((id, movie_name, time))
        self._seats[id] = [[False] * self._cols for _ in range(self._rows)]

    def book_seats(self, id, seat_list):
        if id not in self._seats:
            raise ValueError(f"Invalid show ID: {id}")
        for row, col in seat_list:
            if not (0 <= row < self._rows and 0 <= col < self._cols):
                raise ValueError(f"Invalid seat: {row}, {col}")
            if self._seats[id][row][col]:
                raise ValueError(f"Seat {row}, {col} is already booked")
            self._seats[id][row][col] = True

    def view_show_list(self):
        print(f"Hall {self._hall_no}:")
        for show_id, movie_name, time in self._show_list:
            print(f"\tShow ID: {show_id}, Movie: {movie_name}, Time: {time}")

    def view_available_seats(self, id):
        if id not in self._seats:
            raise ValueError(f"Invalid show ID: {id}")
        print(f"Hall {self._hall_no}, Show ID: {id}, Available Seats:")
        for row in range(self._rows):
            for col in range(self._cols):
                if not self._seats[id][row][col]:
                    print(f"Row: {row + 1}, Col: {col + 1}")


hall_1 = Hall(rows=8, cols=8, hall_no=1)

hall_1.entry_show(id=123, movie_name="Animal", time="12:00pm")

cinema_counter = Star_Cinema()

cinema_counter.view_all_shows()

hall_1.view_available_seats(id=123)

hall_1.book_seats(id=123, seat_list=[(2, 3), (3, 4)])

hall_1.view_available_seats(id=123)
