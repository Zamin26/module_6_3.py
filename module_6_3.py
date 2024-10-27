class Horse:
    x_distance = 0                  # пройденный путь.
    sound = 'Frrr'                  #звук, который издаёт лошадь.
    def run (self, dx):             #dx - изменение дистанции, увеличивает x_distance на dx.
        self.x_distance += dx
        self.sound = 'Frrr'


class Eagle:
    y_distance = 0
    sound = 'I train, eat, sleep, and repeat'
    def fly (self,dy):                              #   изменение дистанции, увеличивает y_distance на dy.
        self.y_distance += dy
        self.sound = 'I train, eat, sleep, and repeat'


class Pegasus(Horse, Eagle):
    def move (self, dx, dy):                        # Наследованные методы run и fly соответственно
        super().run(dx)
        super().fly(dy)

    def get_pos(self):                              # Возвращает текущее положение пегаса в виде кортежа
        return self.x_distance, self.y_distance

    def voice(self):                                # Печатает значение унаследованного атрибута sound
        print(self.sound)


p1 = Pegasus()
print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())

p1.voice()





