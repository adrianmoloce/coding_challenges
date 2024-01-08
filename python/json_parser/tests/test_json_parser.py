from json_parser import Lexer



def lexer():
    lexer = Lexer()
    return lexer


def test_parser_with_empty_brackets(lexer):
    assert lexer.scan("{}") == 0


def test_parser_fails_with_empty_json(lexer):
    assert lexer.scan("") == 1
