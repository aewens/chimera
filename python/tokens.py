from typing import NamedTuple

Token = NamedTuple("Token", [("Type", str), ("Literal", str)])

ILLEGAL = "ILLEGAL"
EOF = "EOF"
IDENT = "IDENT"
INT = "INT"
ASSIGN = "="
PLUS = "+"
COMMA = ","
SEMICOLON = ";"
LPAREN = "("
RPAREN = ")"
LBRACE = "{"
RBRACE = "}"
FUNCTION = "FUNCTION"
LET = "let"
