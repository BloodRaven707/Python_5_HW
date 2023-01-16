from os import system


combination = (
        ( 0, 1, 2 ),
        ( 3, 4, 5 ),
        ( 6, 7, 8 ),
        ( 0, 3, 6 ),
        ( 1, 4, 7 ),
        ( 2, 5, 8 ),
        ( 0, 4, 8 ),
        ( 2, 4, 6 )
    )


def print_board( board: list ):
    print( "\n|---|---|---|" )

    for i in range( 3 ):
        print( f"| { board[ i * 3 ] } | { board[ 1 + i * 3 ] } | { board[ 2 + i * 3 ] } |" )

        if i != 2:
            print ( "|---|---|---|" )

        else:
            print ( "|---|---|---|\n" )


def move( sign: str, board: list ) -> None:

    while True:
        step = input( f"Введите номер ячейки, куда поставить { sign }: " )

        if not step.isdigit():
            print( "\nНужно ввести число от 1 до 9." )
            continue

        if 1 <= int ( step ) <= 9:
            if step in board:
                board[ board.index( str( step ) ) ] = sign
                return

            else:
                print( "\nЭта ячейка уже занята." )
        else:
            print( "\nНужно ввести число от 1 до 9." )


def win_check( board: list, combination: list = combination ) -> bool:

    for item in combination:

        if board[ item[ 0 ] ] == board[ item[ 1 ] ] == board[ item[ 2 ] ]:
            return True

    return False


def main( board: list ):
    print( "Игра: \"Крестики vs Нолики\"" )

    sign = "X"
    for move_count in range(9):
        print_board( board )
        move( sign, board )
        move_count += 1

        if move_count > 4 and win_check( board ):
            print( f"\n{ sign } выиграл." )
            break

        if sign == "X":
            sign = "O"

        else:
            sign = "X"

    else:
        print( "Ничья." )


if __name__ == "__main__":
    system( "cls" )

    board = [ str( i ) for i in [ 7, 8, 9, 4, 5, 6, 1, 2, 3 ] ]

    main( board )
    print_board( board )
