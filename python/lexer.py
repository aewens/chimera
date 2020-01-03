from tokens import *
from typing import Optional

class Lexer:
    _input: str
    _position: int = 0
    _read_position: int = 0
    _ch: Optional[str]

    def __init__(self, data: str) -> None:
        self._input = data
        self.read_char()

    def read_char(self) -> None:
        if self._read_position >= len(self._input):
            self._ch = None

        else:
            self._ch = self._input[self._read_position]

        self._position = self._read_position
        self._read_position = self._read_position + 1

    def next_token(self) -> Token:
        tokens = dict()
        tokens["="] = lambda ch: Token(ASSIGN, ch)
        tokens[";"] = lambda ch: Token(SEMICOLON, ch)
        tokens["("] = lambda ch: Token(LPAREN, ch)
        tokens[")"] = lambda ch: Token(RPAREN, ch)
        tokens[","] = lambda ch: Token(COMMA, ch)
        tokens["+"] = lambda ch: Token(PLUS, ch)
        tokens["{"] = lambda ch: Token(LBRACE, ch)
        tokens["}"] = lambda ch: Token(RBRACE, ch)
        tokens[None] = lambda ch: Token(EOF, "")

        illegal = lambda ch: Token(ILLEGAL, ch)
        tok = tokens.get(self._ch, illegal)(self._ch)
        self.read_char()
        return tok
