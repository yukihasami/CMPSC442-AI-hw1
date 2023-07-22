############################################################
# CMPSC 442: Homework 1
############################################################

student_name = "Yuxuan Xu"


############################################################
# Section 1: Working with Lists
############################################################

def extract_and_apply(l, p, f):
    return [f(x) for x in l if p(x)]


def concatenate(seqs):
    return [v for k in [seqs[0], seqs[1]] for v in k]
    # return [x for x in seqs[0]]+[y for y in seqs[1]]


def transpose(matrix):
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]


############################################################
# Section 2: Sequence Slicing
############################################################

def copy(seq):
    return seq[:]


def all_but_last(seq):
    return seq[:-1]


def every_other(seq):
    return seq[::2]


############################################################
# Section 3: Combinatorial Algorithms
############################################################

def prefixes(seq):
   """ pf = []
    for i in range(len(seq) + 1):
        pf.append(seq[:i])
    return pf"""
   n = len(seq)
   for i in range(n+1):
       yield seq[:i]


def suffixes(seq):
    """sf = []
    a = len(seq)
    for i in range(a + 1):
        sf.append(seq[:a - i])
    return sf"""
    n = len(seq)
    for i in range(n + 1):
        yield seq[i:]


def slices(seq):
    n = len(seq)
    for i in range(n + 1):
        for j in range(n + 1):
            yield seq[j:i]


############################################################
# Section 4: Text Processing
############################################################

def normalize(text):
    return text.lower()


def no_vowels(text):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    return ''.join([x for x in text if x not in vowels])


def digits_to_words(text):
    new = ""
    words = ["zero", "one", "two", "three",
             "four", "five", "six", "seven",
             "eight", "nine"]
    for c in text:
        if c.isdigit():
            new += " "
            new += words[int(c)]

    return new


def to_mixed_case(name):
    # use filter method
    x = list(filter(None, name.split('_')))
    return x[0].lower() + ''.join(y.title() for y in x[1:])


############################################################
# Section 5: Polynomials
############################################################

class Polynomial(object):

    def __init__(self, polynomial):
        self.polynomial = polynomial

    def get_polynomial(self):
        return self.polynomial

    def __neg__(self):
        negpoly = []
        for i in self.polynomial:
            negpoly.append((-i[0], i[1]))
        return Polynomial(negpoly)

    def __add__(self, other):
        addpoly = [x for x in self.polynomial]
        for i in other.polynomial:
            addpoly.append(i)
        return Polynomial(addpoly)

    def __sub__(self, other):
        subpoly = [x for x in self.polynomial]
        for i in other.polynomial:
            subpoly.append((-i[0], i[1]))
        return Polynomial(subpoly)

    def __mul__(self, other):
        # %mulpoly = [x for x in self.polynomial]
        # for i in other.polynomial:
        # mulpoly.append(*i)
        # return Polynomial(mulpoly)
        mulpoly = []
        for i in range(0, len(self.polynomial)):
            for j in range(0, len(other.polynomial)):
                mulpoly.append(
                    (self.polynomial[i][0] * other.polynomial[j][0], self.polynomial[i][1] + other.polynomial[j][1]))
        return Polynomial(mulpoly)

    def __call__(self, x):
        calln1 = 0
        for i in self.polynomial:
            calln1 = i[0] * (x ** i[1])
        return calln1

    def simplify(self):
        # set value
        x, y, s = 0, 0, 0
        new = []
        for i in range(0, len(self.polynomial)):
            for j in range(i + 1, len(self.polynomial)):
                if self.polynomial[i][1] < self.polynomial[j][1]:
                    (self.polynomial[i], self.polynomial[j]) = (self.polynomial[j], self.polynomial[i])

        while x < len(self.polynomial) and y < len(self.polynomial):
            if self.polynomial[x][1] == self.polynomial[y][1]:
                s += self.polynomial[y][0]
                y += 1
            else:
                new.append((s, self.polynomial[x][1]))
                x = y
                s = 0
        new.append((s, self.polynomial[x][1]))
        self.polynomial = new

    def __str__(self):
        return None


############################################################
# Section 6: Feedback
############################################################

feedback_question_1 = """
Type your response here.
Your response may span multiple lines.
Do not include these instructions in your response.

7.25 hours
"""

feedback_question_2 = """
Type your response here.
Your response may span multiple lines.
Do not include these instructions in your response.

I think the most chanllege part is to actully pick up all the thing from python without thinking to use really hard way to solve question
when there are some simplfy method that can be used in python compare with other programming language. I really stuck with the last 
question
"""

feedback_question_3 = """
Type your response here.
Your response may span multiple lines.
Do not include these instructions in your response.

I really like to learn more useful methods that only python has and to be surperise how much easier my life can be with all the method
that python has, and I guess what I would have change is to start this assignment earlier, so I might could have solve the problems that
I can not solve this time
"""
