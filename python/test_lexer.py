from tokens import *
from lexer import Lexer

def test_next_token():
    test_input = "=+(){},;"
    test_tokens = [
        Token(ASSIGN, "="),
        Token(PLUS, "+"),
        Token(LPAREN, "("),
        Token(RPAREN, ")"),
        Token(LBRACE, "{"),
        Token(RBRACE, "}"),
        Token(COMMA, ","),
        Token(SEMICOLON, ";"),
        Token(EOF, "")
    ]

    lex = Lexer(test_input)

    for i, test_token in enumerate(test_tokens):
        tok = lex.next_token()
        
        expected_type = test_token.Type
        got_type = tok.Type
        wrong_type = "tests[{}] - wrong type, expected={}, got={}"
        wt_args = i, expected_type, got_type
        assert got_type == expected_type, wrong_type.format(*wt_args)
        
        expected_literal = test_token.Literal
        got_literal = tok.Literal
        wrong_literal = "tests[{}] - wrong literal, expected={}, got={}"
        wl_args = i, expected_literal, got_literal
        assert got_literal == expected_literal, wrong_literal.format(*wl_args)
