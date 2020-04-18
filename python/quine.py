# NOTE: this does not work because the website executes it as:
# cat quine.py | python -
# Therefore __file__ = sys.stdin
# https://github.com/code-golf/code-golf/blob/5feb18bc741f6c3631bfe5748ebe4730fa6d69d8/hole/hole.go#L99
#  print(open(__file__).read(), end="")

# FIXME: empty
#  import sys
#  print(sys.stdin.read())
#  print(open(0).read())
#  Other hacks also do not work!
#  https://stackoverflow.com/a/38670261
#  open(1, 'w').write(open(0).read())

# FIXME: also empty
#  import fileinput
#  print(''.join(fileinput.input()))
#  try:
#      while True:
#          print(input())
#  except EOFError:
#      pass

# FIXME: EOFError
#  print(input())
# Related Python issue: https://bugs.python.org/issue17620

# FIXME: still empty
# from ctypes import *
# c = cdll.LoadLibrary("libc.so.6")
# s = create_string_buffer(100)
# c.scanf(b'%s', s)
# print(s.value)
