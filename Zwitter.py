class Zwitter:

    def __init__(self):
       # self.wool   ##шерсть
       # self.paws   ##лапы
       # self.eyes   ##глаза
       # self.tail   ##хвост
        self.body = 20 ##тело
       # self.mouth  ##пасть
       # self.teeth  ##клыки
       # self.head   ##голова
       # self.ears   ##уши
        self.color = 'Red'

 #   def run(self):
    def breath(self, breathing):
        if breathing is True:
            self.body = 20
            self.color = 'Red'
        else:
            self.body = 10
            self.color = 'Black'


  #  def jump(self):

  #  def kill(self):

  #  def growl(self):

  #  def sleep(self):