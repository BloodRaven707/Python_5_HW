from os import system
from random import randint


def generate_random_string( chars_count: int ) -> str:
    symbols = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"

    result = []
    for i in range ( chars_count ):
        amount_symb = randint( 1, 5 )
        result += [ amount_symb * symbols[ randint( 0, 51 ) ] ]

    return "".join( result )


def compression ( encode_txt: str, decode_txt: str ) -> float:
    return round( ( 1 - len( encode_txt ) / len( decode_txt ) ) * 100, 2 )


def import_to_file( text: str, file_name: str ):
    with open( file_name, "w" ) as fl:
        fl.writelines( text )


def export_from_file ( file_name: str ) -> str:
    with open( file_name ) as fl:
        return fl.read()


def rle_encode( text: str ) -> str:
    if not text:
        return ""

    encode = []
    count = 1
    for i in range( 1, len( text ) ):
        if text[ i ] != text[ i - 1 ]:
            if text[ i - 1 ]:
                encode += [ f"{ count }{ text[ i - 1 ] }" ]

            count = 1

        else:
            count += 1

    else:
        encode += [ f"{ count }{ text[ i ] }" ]
        return "".join( encode )


def rle_decode( text: str ) -> str:
    if not text:
        return ""

    decode = []
    count = ""
    for i in range( len( text ) ):
        if text[ i ].isdigit():
            count += text[ i ]

        else:
            decode += [ text[ i ] * int( count ) ]
            count = ""

    return "".join( decode )


if __name__ == "__main__":
    system( "cls" )

    test_string = generate_random_string( int( input( "Введите число последовательностей символов в тестовой строке: " ) ) )
    test_file = "Test_string.txt"
    import_to_file( test_string, test_file )
    print( f"\nИнформация в первоначальном виде: \"{ test_string }\", записана в файл { test_file }\n" )

    encode_text = rle_encode( export_from_file( test_file ) )
    encode_file = "Encode_string.txt"
    import_to_file( encode_text, encode_file )
    print( f"Информация c RLE сжатием: \"{ encode_text }\", записана в файл { encode_file }\n" )

    decode_text = rle_decode( export_from_file( encode_file ) )
    decode_file = 'Decode_string.txt'
    import_to_file( decode_text, decode_file )
    print( f"Декодированная информация в виде: \"{ decode_text }\", записана в файл { decode_file }\n" )

    print( f"Степень сжатия информации составила { compression ( encode_text, decode_text ) }%\n" )
