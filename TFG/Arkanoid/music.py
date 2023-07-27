import pygame,random

class Music():
    def __init__(self):
        pygame.mixer.pre_init(44100, -16, 1, 512)
        pygame.mixer.init()
        self.music_on=True
        self.music_effects=True
        self.ping=pygame.mixer.Sound('./Arkanoid/snd/pong.wav')
        self.ping.set_volume(0.2)
        if self.music_on:
            self.playMenu()
        self.punch=[]
        self.punch.append(pygame.mixer.Sound('./Arkanoid/snd/punch1.wav'))
        self.punch.append(pygame.mixer.Sound('./Arkanoid/snd/punch2.wav'))
        self.punch.append(pygame.mixer.Sound('./Arkanoid/snd/punch3.wav'))
        self.punch.append(pygame.mixer.Sound('./Arkanoid/snd/punch4.wav'))
        for sound in self.punch:
            sound.set_volume(0.1)
        self.fail=pygame.mixer.Sound('./Arkanoid/snd/fail.wav')
        self.fail.set_volume(0.5)
        self.next=pygame.mixer.Sound('./Arkanoid/snd/nextlvl.wav')
        self.next.set_volume(0.5)
        

        
    def playMenu(self):
        pygame.mixer.music.load('./Arkanoid/snd/menu.wav')
        pygame.mixer.music.set_volume(0.4)
        pygame.mixer.music.play()
    
    def playGame(self):
        pygame.mixer.music.load('./Arkanoid/snd/play.mp3')
        pygame.mixer.music.play()
        pygame.mixer.music.set_volume(0.4)
        
    def playPunch(self):
        i=random.randrange(4)
        pygame.mixer.Sound.play(self.punch[i])
        
    def playFail(self):
        pygame.mixer.Sound.play(self.fail)
    
    def playNext(self):
        pygame.mixer.Sound.play(self.next)
    
    def playBounce(self):
        pygame.mixer.Sound.play(self.ping)