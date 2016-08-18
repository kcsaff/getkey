

class Code(object):
    def __init__(self, name, code=None, chars=None):
        self.name = name
        self.code = code or self.name
        self.chars = chars or self.code

    def __str__(self):
        return self.chars

    def __repr__(self):
        return '<{}>'.format(self.name.upper())

    def __eq__(self, other):
        if isinstance(other, Code):
            return self.chars == other.chars or self.code == other.code
        else:
            raise NotImplementedError

    def __ne__(self, other):
        return not self.__eq__(other)


class AsciiControl:
    NUL = Code('NUL', chr(0x00))
    SOH = Code('SOH', chr(0x01))
    STX = Code('STX', chr(0x02))
    ETX = Code('ETX', chr(0x03))
    EOT = Code('EOT', chr(0x04))
    ENQ = Code('ENQ', chr(0x05))
    ACK = Code('ACK', chr(0x06))
    BEL = Code('BEL', chr(0x07))
    BS  = Code('BS',  chr(0x08))
    TAB = Code('TAB', chr(0x09))
    LF  = Code('LF',  chr(0x0a))
    VT  = Code('VT',  chr(0x0b))
    FF  = Code('FF',  chr(0x0c))
    CR  = Code('CR',  chr(0x0d))
    SO  = Code('SO',  chr(0x0e))
    SI  = Code('SI',  chr(0x0f))
    DLE = Code('DLE', chr(0x10))
    DC1 = Code('DC1', chr(0x11))
    DC2 = Code('DC2', chr(0x12))
    DC3 = Code('DC3', chr(0x13))
    DC4 = Code('DC4', chr(0x14))
    NAK = Code('NAK', chr(0x15))
    SYN = Code('SYN', chr(0x16))
    ETB = Code('ETB', chr(0x17))
    CAN = Code('CAN', chr(0x18))
    EM  = Code('EM',  chr(0x19))
    SUB = Code('SUB', chr(0x1a))
    ESC = Code('ESC', chr(0x1b))
    FS  = Code('FS',  chr(0x1c))
    GS  = Code('GS',  chr(0x1d))
    RS  = Code('RS',  chr(0x1e))
    US  = Code('US',  chr(0x1f))
    DEL = Code('DEL', chr(0x7f))


class AsciiPrintable:
    SPACE = Code('space', ' ')
    EXCLAMATION = Code('!')
    DOUBLE_QUOTE = Code('"')
    HASH = Code('#')
    DOLLAR = Code('$')
    PERCENT = Code('%')
    AMPERSAND = Code('&')
    SINGLE_QUOTE = Code('\'')
    OPEN_PARENTHESIS = Code('(')
    CLOSE_PARENTHESIS = Code(')')
    ASTERISK = Code('*')
    PLUS = Code('+')
    COMMA = Code(',')
    MINUS = Code('-')
    PERIOD = Code('.')
    SLASH = Code('/')
    N0 = Code('0')
    N1 = Code('1')
    N2 = Code('2')
    N3 = Code('3')
    N4 = Code('4')
    N5 = Code('5')
    N6 = Code('6')
    N7 = Code('7')
    N8 = Code('8')
    N9 = Code('9')
    COLON = Code(':')
    SEMICOLON = Code(';')
    LESS_THAN = Code('<')
    EQUALS = Code('=')
    GREATER_THAN = Code('>')
    QUESTION = Code('?')

    AT = Code('@')
    A = Code('A')
    B = Code('B')
    C = Code('C')
    D = Code('D')
    E = Code('E')
    F = Code('F')
    G = Code('G')
    H = Code('H')
    I = Code('I')
    J = Code('J')
    K = Code('K')
    L = Code('L')
    M = Code('M')
    N = Code('N')
    O = Code('O')
    P = Code('P')
    Q = Code('Q')
    R = Code('R')
    S = Code('S')
    T = Code('T')
    U = Code('U')
    V = Code('V')
    W = Code('W')
    X = Code('X')
    Y = Code('Y')
    Z = Code('Z')
    LEFT_BRACKET = Code('[')
    BACKSLASH = Code('\\')
    RIGHT_BRACKET = Code(']')
    CARET = Code('^')
    UNDERSCORE = Code('_')

    TICK = Code('`')
    a = Code('a')
    b = Code('b')
    c = Code('c')
    d = Code('d')
    e = Code('e')
    f = Code('f')
    g = Code('g')
    h = Code('h')
    i = Code('i')
    j = Code('j')
    k = Code('k')
    l = Code('l')
    m = Code('m')
    n = Code('n')
    o = Code('o')
    p = Code('p')
    q = Code('q')
    r = Code('r')
    s = Code('s')
    t = Code('t')
    u = Code('u')
    v = Code('v')
    w = Code('w')
    x = Code('x')
    y = Code('y')
    z = Code('z')
    LEFT_CURLY = Code('{')
    PIPE = Code('|')
    RIGHT_CURLY = Code('}')
    TILDE = Code('~')


class Control(object):
    def __init__(self, format=None):
        if not format:
            return
        for attr, value in dir(self.__class__):
            if attr.startswith('CTRL'):
                char = value.name[1]
                newname = format.format(lower=char.lower(), upper=char.upper())
                newvalue = Code(newname, value.code, value.chars)
                setattr(self, attr, newvalue)

    CTRL_AT = Code('^@', chr(0x00), '^@')
    CTRL_A = Code('^A', chr(0x01), '^A')
    CTRL_B = Code('^B', chr(0x02), '^B')
    CTRL_C = Code('^C', chr(0x03), '^C')
    CTRL_D = Code('^D', chr(0x04), '^D')
    CTRL_E = Code('^E', chr(0x05), '^E')
    CTRL_F = Code('^F', chr(0x06), '^F')
    CTRL_G = Code('^G', chr(0x07), '^G')
    CTRL_H = Code('^H', chr(0x08), '^H')
    CTRL_I = Code('^I', chr(0x09), '^I')
    CTRL_J = Code('^J', chr(0x0a), '^J')
    CTRL_K = Code('^K', chr(0x0b), '^K')
    CTRL_L = Code('^L', chr(0x0c), '^L')
    CTRL_M = Code('^M', chr(0x0d), '^M')
    CTRL_N = Code('^N', chr(0x0e), '^N')
    CTRL_O = Code('^O', chr(0x0f), '^O')
    CTRL_P = Code('^P', chr(0x10), '^P')
    CTRL_Q = Code('^Q', chr(0x11), '^Q')
    CTRL_R = Code('^R', chr(0x12), '^R')
    CTRL_S = Code('^S', chr(0x13), '^S')
    CTRL_T = Code('^T', chr(0x14), '^T')
    CTRL_U = Code('^U', chr(0x15), '^U')
    CTRL_V = Code('^V', chr(0x16), '^V')
    CTRL_W = Code('^W', chr(0x17), '^W')
    CTRL_X = Code('^X', chr(0x18), '^X')
    CTRL_Y = Code('^Y', chr(0x19), '^Y')
    CTRL_Z = Code('^Z', chr(0x1a), '^Z')
    CTRL_LEFT_BRACKET = Code('^[', chr(0x1b), '^[')
    CTRL_BACKSLASH = Code('^\\', chr(0x1c), '^\\')
    CTRL_RIGHT_BRACKET = Code('^]', chr(0x1d), '^]')
    CTRL_CARET = Code('^^', chr(0x1e), '^^')
    CTRL_UNDERSCORE = Code('^_', chr(0x1f), '^_')


control_editor = Control('C-{lower}')
control_windows_old = Control('CTRL-{upper}')
control_windows = Control('Ctrl+{upper}')
control_vms = Control('Ctrl/{upper}')
control_mac_menu = Control()
control_mac_prose = Control('Control-{upper}')


class Ascii(AsciiControl, AsciiPrintable):
    pass
