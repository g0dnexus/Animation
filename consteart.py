import math
import time

def draw_heart():
    angle = 0
    while True:
        heart = []
        for y in range(11, -10, -1):
            heart_row = []
            for x in range(-30, 30):
                if math.sqrt(x * x + y * y) <= abs(10 * math.sin(angle) * math.cos(angle)):
                    heart_row.append('♥️')
                else:
                    heart_row.append(' ')
            heart.append(' '.join(heart_row))
        print('\n'.join(heart))
        angle += 0.1
        time.sleep(0.1)
        print('\033[H\033[J')  

draw_heart()
