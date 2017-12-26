from multiprocessing import Process
from time import sleep
from PIL import Image, ImageDraw  # Подключим необходимые библиотеки.

image = Image.open("snim.jpg")  # Открываем изображение.
draw = ImageDraw.Draw(image)  # Создаем инструмент для рисования.
width = image.size[0]  # Определяем ширину.
height = image.size[1]  # Определяем высоту.
pix = image.load()  # Выгружаем значения пикселей.


class A:
    def __call__(self, count=10, sleep_time=0.5):
        for i in range(0, 340):
            for j in range(0 - 192):
                a = pix[i, j][0]
                b = pix[i, j][1]
                c = pix[i, j][2]
                S = (a * 30 + b * 59 + c * 11) // 100
                print(S)
                draw.point((i, j), (S, S, S))
            sleep(sleep_time)


class B:
    def __call__(self, count=10, sleep_time=0.5):
        for i in range(341, 680):
            for j in range(193, 385):
                a = pix[i, j][0]
                b = pix[i, j][1]
                c = pix[i, j][2]
                S = (a * 30 + b * 59 + c * 11) // 100
                print(S)
                draw.point((i, j), (S, S, S))

            sleep(sleep_time)


class C:
    def __call__(self, count=10, sleep_time=0.5):
        for i in range(681, 1024):
            for j in range(386, 578):
                a = pix[i, j][0]
                b = pix[i, j][1]
                c = pix[i, j][2]
                S = (a * 30 + b * 59 + c * 11) // 100
                print(S)
                draw.point((i, j), (S, S, S))
            sleep(sleep_time)


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