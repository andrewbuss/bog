import string
from sys import stdout

class Trie:
    def __init__(self):
        self.children = {}
    def add(self, word):
        if not len(word): pass
        elif word[0] in self.children:
            self.children[word[0]].add(word[1::])
        else:
            self.children[word[0]] = Trie()
            self.children[word[0]].add(word[1::])
    def check(self,word):
        if not len(word): return 1
        elif word[0] in self.children: return self.children[word[0]].check(word[1::])
        else: return 0
    def __repr__(self):
        return self.children

trie = Trie()

ifile = open("words.txt")
uf = [filter(str.isalnum, word).lower() for word in ifile.readlines()]
f = []
for word in uf:
    if len(word)<3: continue
    c = 1
    for letter in word:
        if letter not in string.ascii_lowercase:
            c = 0
            break
    if c: f.append(word)

for word in f:
    trie.add(word)

board = []
found = []
v = []
def test(y, x, wi):
    global board, found, v
    if v[y][x]: return
    w = wi+board[y][x]
    if not trie.check(w): return
    if w in f: found.append(w)
    v[y][x] = 1
    if y>0:
        if x>0: test(y-1,x-1,w)
        test(y-1,x,w)
        if x<3: test(y-1,x+1,w)
    if x>0: test(y,x-1,w)
    if x<3: test(y,x+1,w)
    if y<3:
        if x>0: test(y+1,x-1,w)
        test(y+1,x,w)
        if x<3: test(y+1,x+1,w)
    v[y][x] = 0

values = [0,0,0,1,1,2,3,5,11,11,11,11,11,11,11,11,11]

def testboard(boardi):
    global board, found, v
    board = boardi
    found = []
    v = [[0 for _ in range(4)] for __ in range(4)]
    for y in range(4):
        for x in range(4):
            test(y,x, "")
    found = set(found)
    return sum([values[len(word)] for word in found])