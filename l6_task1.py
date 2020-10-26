import time


new_line = '\n'*50


class TrafficLight:

    __color = 'Красный'

    def light_switch(self, color, console_color, secs, blink_secs):
        self.__color = color
        print(new_line + '\x1b[' + console_color + 'm' + self.__color + '\x1b[0m')
        for i in range(1, secs*2):
            if secs * 2 - i <= blink_secs * 2:
                print(new_line + '\x1b[' + console_color + 'm' + self.__color + '\x1b[0m' if i % 2 == 0 else new_line)
            time.sleep(0.5)

    def running(self):
        while True:
            self.light_switch('Красный', '0;30;41', 7, 0)
            self.light_switch('Желтый', '0;30;43', 2, 0)
            self.light_switch('Зелёный', '0;30;42', 7, 3)
            self.light_switch('Желтый', '0;30;43', 2, 0)


tl = TrafficLight()
tl.running()
