import math
import operator
from collections import deque



class RPN():

    def __init__(self):
        self.stack = deque()
        self.ops = {'+':operator.add,
        '-':operator.sub,
        '*':operator.mul,
        '/':operator.div}

    def eval_expression(self, expression):
        self.stack = deque()
        result = 0
        for token in expression.split(' '):
            if token.isdigit():
                self.stack.appendleft(token)
            elif token in self.ops:
                self._eval_opt(token)
        if len(self.stack) == 1:
            return self.stack[0]
        else:
            print 'Error! Re-check Expression'

    def _eval_opt(self, token):
        n1 = float(self.stack.popleft())
        n2 = float(self.stack.popleft())
        result = self.ops[token](n2,n1)
        self.stack.appendleft(result)

    def compute(self):
        running = True
        while running:
            token = raw_input('Enter #: ')
            if token in ('q', 'quit', 'exit'):
                running = False
            else:
                if token.isdigit():
                    self.stack.appendleft(token)
                    print self.stack
                elif token in self.ops:
                    self._eval_opt(token)
                    print self.stack
