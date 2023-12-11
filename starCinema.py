class Star_Cinema:
    def __init__(self):
        self._hall_list = []

    def entry_hall(self, hall):
        self._hall_list.append(hall)

    def view_all_shows(self):
        for hall in self._hall_list:
            hall.view_show_list()


class Hall:
    def __init__(self, rows, cols, hall_no, star_cinema):
        self._seats = {}
        self._show_list = []
        self._rows = rows
        self._cols = cols
        self._hall_no = hall_no
        star_cinema.entry_hall(self)

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
            print(f"Show ID: {show_id}, Movie: {movie_name}, Time: {time}")

    def view_available_seats(self, id):
        if id not in self._seats:
            raise ValueError(f"Invalid show ID: {id}")
        print(f"Hall {self._hall_no}, Show ID: {id}, Available Seats:")
        for row in range(self._rows):
            for col in range(self._cols):
                if not self._seats[id][row][col]:
                    print(f"Row: {row + 1}, Col: {col + 1}")

        print(f'Available seats in matrix:(if available 1 else 0)\n')
        for row in range(self._rows):
            for col in range(self._cols):
                if not self._seats[id][row][col]:
                    print('1', end=' ')
                else:
                    print('0', end=' ')
            print('\n')

def find_hall_by_show_id(star_cinema, show_id):
    for hall in star_cinema._hall_list:
        if show_id in [show[0] for show in hall._show_list]:
            return hall
    raise ValueError(f"Show ID {show_id} not found.")



def main():
    star_cinema = Star_Cinema()

    hall_1 = Hall(rows=8, cols=8, hall_no=1, star_cinema=star_cinema)
    hall_1.entry_show(id=111, movie_name="Animal", time="11:00am")

    hall_2 = Hall(rows=8, cols=8, hall_no=2, star_cinema=star_cinema)
    hall_2.entry_show(id=222, movie_name="Jawan", time="11:00am")

    hall_3 = Hall(rows=8, cols=8, hall_no=3, star_cinema=star_cinema)
    hall_3.entry_show(id=333, movie_name="Pathan", time="11:00am")

    while True:
        print("\n1. View All Shows Today")
        print("2. View Available Seats")
        print("3. Book Tickets")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            star_cinema.view_all_shows()

        elif choice == "2":
            try:
                show_id = int(input("Enter the Show ID: "))
                hall = find_hall_by_show_id(star_cinema, show_id)
                hall.view_available_seats(show_id)
            except ValueError as e:
                print(e)

        elif choice == "3":
            try:
                show_id = int(input("Enter the Show ID: "))
                hall = find_hall_by_show_id(star_cinema, show_id)
                num_seats = int(input("Enter the number of seats to book: "))
                seat_list = []
                for _ in range(num_seats):
                    row = int(input("Enter the row number: "))
                    col = int(input("Enter the column number: "))
                    seat_list.append((row - 1, col - 1)) 
                hall.book_seats(show_id, seat_list)
                print("Ticket booked successfully.")
            except ValueError as e:
                print(e)

        elif choice == "4":
            print("Exiting program")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
