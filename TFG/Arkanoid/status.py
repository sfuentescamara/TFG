import time
class Status:
  def __init__(self):
    self.level = 1
    self.points = 0
    self.lives=2
    self.f=open('./Arkanoid/highscore.txt','r+')
    self.highscore=int(self.f.readline())
    self.mnoznik=0
    self.last_hit=time.time()