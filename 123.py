from multiprocessing import Process
from time import sleep
from PIL import Image, ImageDraw  # Подключим необходимые библиотеки.

image = Image.open("snim.jpg")  # Открываем изображение.
draw = ImageDraw.Draw(image)  # Создаем инструмент для рисования.
width = image.size[0]  # Определяем ширину.
height = image.size[1]  # Определяем высоту.
pix = image.load()  # Выгружаем значения пикселей.
mas = [[0 for x in range(width)] for y in range(height)] 


class A:
    def __call__(self):
        for i in range(0, 340):
            for j in range(height):
                a = pix[i, j][0]
                b = pix[i, j][1]
                c = pix[i, j][2]
                S = (a * 30 + b * 59 + c * 11) // 100
                mas[i][j] = S
                #mas = [S for x in range(0, 340)], [S for y in range(height)]
                print(S)
                draw.point((i, j), (S, S, S))
            sleep(0)


class B:
    def __call__(self):
        for i in range(341, 680):
            for j in range(height):
                a = pix[i, j][0]
                b = pix[i, j][1]
                c = pix[i, j][2]
                S = (a * 30 + b * 59 + c * 11) // 100
                mas = [S for x in range(341, 680)], [S for y in range(height)]
                print(S)
                draw.point((i, j), (S, S, S))
            sleep(0)


class C:
    def __call__(self):
        for i in range(681, 1024):
            for j in range(height):
                a = pix[i, j][0]
                b = pix[i, j][1]
                c = pix[i, j][2]
                S = (a * 30 + b * 59 + c * 11) // 100
                mas = [S for x in range(681, 1024)], [S for y in range(height)]
                print(S)
                draw.point((i, j), (S, S, S))
            sleep(0)


# image.save("ans.jpg", "JPEG")
# del draw
if __name__ == '__main__':
    a = A()
    b = B()
    c = C()

    p1 = Process(target=a, args=())
    p2 = Process(target=b, args=())
    p3 = Process(target=c, args=())

    p1.start()
    p2.start()
    p3.start()

    p1.join()
    p2.join()
    p3.join()
    print(mas)
