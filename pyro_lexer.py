import re

from pygments.lexer import RegexLexer, words
from pygments.token import Text, Comment, Operator, Keyword, Name, String, Number, Punctuation

__all__ = ['PyroLexer']
__version__ = "0.6.2"

class PyroLexer(RegexLexer):
    name = 'Pyro'
    filenames = ['*.pyro']
    aliases = ['pyro']

    flags = re.MULTILINE | re.UNICODE

    tokens = {
        'root': [
            (r'\n', Text),
            (r'\s+', Text),
            (r'#(.*?)\n', Comment.Single),
            (r'(>>>|[.]{3})', Comment.Preproc),

            (r'(import|as)\b', Keyword.Namespace),
            (r'(var|let|def|class|typedef|pub|pri|static|with|extends|enum|interface)\b', Keyword.Declaration),

            (words((
                'if', 'else', 'for', 'in', 'loop', 'while', 'defer',
                'break', 'continue', 'return',
                'echo', 'try', 'assert', 'mod', 'rem',
            ), suffix=r'\b'), Keyword),

            (r'(true|false|null|self|super)\b', Keyword.Constant),

            # Float literal.
            (r'\d[\d_]*(\.[\d_]+[eE][+\-]?[\d_]+|\.[\d_]*|[eE][+\-]?[\d_]+)', Number.Float),

            # Binary integer.
            (r'0[bB][01_]+', Number.Bin),

            # Octal integer.
            (r'0[oO][0-7_]+', Number.Oct),

            # Hex integer.
            (r'0[xX][0-9a-fA-F_]+', Number.Hex),

            # Decimal integer.
            (r'(0|[1-9][0-9_]*)', Number.Integer),

            # Character literal.
            (r"""'(\\['"\\abfnrtv]|\\x[0-9a-fA-F]{2}"""
             r"""|\\u[0-9a-fA-F]{4}|\\U[0-9a-fA-F]{8}|[^\\])'""",
             String.Char),

            # Raw string literal.
            (r'`[^`]*`', String),

            # String literal.
            (r'"(\\\\|\\[^\\]|[^"\\])*"', String),

            # Operators.
            (r'(<<|>>|!!|\?\?|<=|>=|\+=|-=|&&'
             r'|==|!=|[<>!+\-*/&|~^=%]|:\||:\?)', Operator),

            # Punctuation.
            (r'[()\[\]{}.,;:?]', Punctuation),

            # Identifiers.
            (r'[$\w_]\w*', Name.Other),
        ]
    }
