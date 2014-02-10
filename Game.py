#Bowling Kata
class Game:

  #bonus frames are frames that got a strike or spare and whose score is still being calculated.
  bonusFrames = {}

  def Roll(self, pins):
    currFrame = self.gameFrames.pop()
    if (currFrame.isFull()):
      #If the current frame is full, put it back onto the frame list and start a new frame
      oldFrame = currFrame
      if (oldFrame.isStrike() or oldFrame.isSpare()):
        self.addBonusFrame(oldFrame)

      self.gameFrames.append(oldFrame)
      currFrame = Frame()
    currFrame.addScore(pins)
    self.updateBonusFrames(pins)
    self.gameFrames.append(currFrame)
    

  def Score(self):
    return sum([frame.getScore() for frame in self.gameFrames])

  def __init__(self):
    self.score = 0
    self.gameFrames = [Frame()]

  def addBonusFrame(self, oldFrame):
    if (oldFrame.isStrike()):
      self.bonusFrames.__setitem__(oldFrame,2)
    if (oldFrame.isSpare()):
      self.bonusFrames.__setitem__(oldFrame,1)

  def updateBonusFrames(self, pins):
    for frame in self.bonusFrames.keys():
      frame.addBonus(pins)
      self.bonusFrames[frame] = self.bonusFrames[frame] - 1
      if (self.bonusFrames[frame] == 0):
        self.bonusFrames.pop(frame)

#Class that will hold any frame information
class Frame:

  def addScore(self, score):
    if (self.frameScore.__len__() == 0):
      self.frameScore.append(score)
    elif (self.frameScore.__len__() == 1 and self.frameScore[0] < 10):
      self.frameScore.append(score)
    else:
      raise FrameError("Can't put any more points into this frame!")

  def addBonus(self, score):
    if (sum(self.frameScore) >= 10):
      self.frameScore.append(score)

  def getScore(self):
    return sum(self.frameScore)

  def isFull(self):
    return self.frameScore.__len__() >= 2 or sum(self.frameScore) >= 10

  def isStrike(self):
    return self.frameScore.__len__() > 0 and self.frameScore[0] == 10

  def isSpare(self):
    return self.frameScore.__len__() > 1 and self.frameScore[0] + self.frameScore[1] == 10 and not self.isStrike()

  def __init__(self):
    self.frameScore = []


class FrameError(StandardError):
  pass

