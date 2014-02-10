#!/usr/bin/python2.7
from Game import Game
import unittest

# Here's our "unit tests"
class GameTests(unittest.TestCase):

    def testOneBowl(self):
	bowlGame = Game()
	bowlGame.Roll(5)
        print(bowlGame.Score())
        self.failUnless(bowlGame.Score() == 5)

    def testOneFrame(self):
    	bowlGame = Game()
	bowlGame.Roll(5)
	bowlGame.Roll(4)
	self.failUnless(bowlGame.Score() == 9)

    def testSpare(self):
	bowlGame = Game()
	bowlGame.Roll(5)
	bowlGame.Roll(5)
	bowlGame.Roll(5)
	bowlGame.Roll(4)
	self.failUnless(bowlGame.Score() == 24)

    def testStrike(self):
	bowlGame = Game()
	bowlGame.Roll(10)
	bowlGame.Roll(5)
	bowlGame.Roll(5)
	self.failUnless(bowlGame.Score() == 30)     

    def testTurkey(self):
	bowlGame = Game()
	bowlGame.Roll(10)
	bowlGame.Roll(10)
	bowlGame.Roll(10)
	bowlGame.Roll(5)
	bowlGame.Roll(5)
	self.failUnless(bowlGame.Score() == 85)

    def testWorthlessSpare(self):
	bowlGame = Game()
	bowlGame.Roll(5)
	bowlGame.Roll(5)
	bowlGame.Roll(0)
	bowlGame.Roll(5)
	self.failUnless(bowlGame.Score() == 15)

def main():
    unittest.main()

if __name__ == '__main__':
    main()
