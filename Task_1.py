from os import system
from random import choice, randint


candies = 140


def take_candy( player ):
    global candies

    taken_candies = int( input( f"{ player }, сколько вы возьмете: " ) )
    while taken_candies < 1 or taken_candies > 28 or taken_candies > candies:
        if candies > 29:
            print( "Вы должны взять не менее 1 и не более 28 конфет..." )

        else:
            print( "Помните взяв последнюю конету вы проиграете..." )

        taken_candies = int( input( f"{ player } сколько вы возьмете: ") )

    else:
        candies -= taken_candies


def players_mode( players_count: int = 2 ):
    global candies
    players = [ "Игрок 1", "Игрок 2" ]

    for i in range( players_count ):
        players[ i ] = name if ( name:= input( f"Введите имя { i + 1 }-го игрока: " ) ) else players[ i ]

    print()
    first_player = choice( players )

    while candies > 0:
        for i in range( len( players )):
            if first_player:
                if first_player != players[ i ]:
                    first_player = False
                    continue

                else:
                    first_player = False

            take_candy( players[ i ] )

            if candies == 0:
                if i == 0:
                    print( f"Победил игрок: { players[ 1 ] }\n" )
                else:
                    print( f"Победил игрок: { players[ 0 ] }\n" )
                break

            print( f"Конфет осталось: {candies}\n" )


def main():
    print( "Игра: \"Конфеты\"\n" )
    candies = 140

    print( "0 - Играть с другом\n1 - Играть с простым ботом\n2 - Играть с умным ботом\n" )

    game_mode = ""
    while (game_mode := input( "Выберите режим игры: " )) not in ["0", "1", "2"]:
            print( "0 - Играть с другом\n1 - Играть с простым ботом\n2 - Играть с умным ботом\n" )
    else:
        print()
        if game_mode == "0":
            players_mode()
        else:
            print( "Приносим извинения. Игра в находится в разрабоке, боты будут добавлены позднее...\n" )
            print( "Вы играете в ознакомительную версию: Игрок против Игрока.\n" )
            players_mode()

            if game_mode == "1":
                pass
                # easy_bot()
            else:
                pass
                # hard_bot()


if __name__ == "__main__":
    system( "cls" )
    main()
