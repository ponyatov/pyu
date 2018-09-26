
class Object:
	def __init__(self, V):
		self.tag = self.__class__.__name__
		self.val = V
	def __repr__(self):
		return self.dump()
	def dump(self, depth=0):
		return self.head()
	def head(self, prefix=''):
		return '%s<%s:%s> @ 0x%X' % (prefix, self.tag, self.val, id(self))

import pickle

try:
	pool = pickle.load(open('imagee','r'))
except IOError:
	pool = []

import ply.lex  as lex
import ply.yacc as yacc

tokens = ['SYM']

t_ignore = ' \t\r\n'

def t_SYM(t):
	r'[^ \t\r\n]+'
	t.value = Object(t.value) ; return t

def p_REPL_none(p):
	'REPL : '
def p_REPL_sym(p):
	'REPL : REPL SYM'
	print p[2]

def t_error(t): raise SyntaxError(t)	# lexer  error callback
def p_error(p): raise SyntaxError(p)	# parser error callback

lexer  = lex.lex()
parser = yacc.yacc(debug=False,write_tables=None)

import sys

try:
	SRC = open(sys.argv[1]).read()
except IndexError:
	SRC = open('src.src').read()

parser.parse(SRC)

pickle.dump(pool,open('image','w'))

print Object('some')