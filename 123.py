from multiprocessing import Process, Array
from time import sleep
from PIL import Image, ImageDraw  # Подключим необходимые библиотеки.

image = Image.open("snim.jpg")  # Открываем изображение.
draw = ImageDraw.Draw(image)  # Создаем инструмент для рисования.
width = image.size[0]  # Определяем ширину.
height = image.size[1]  # Определяем высоту.
pix = image.load()  # Выгружаем значения пикселей.
mas = Array('i', range(width*height))

process_count = 3

def f(num, mas):
    for i in range(num*width//process_count, (num+1)*width//process_count):
        for j in range(height):
            a = pix[i, j][0]
            b = pix[i, j][1]
            c = pix[i, j][2]
            S = (a * 30 + b * 59 + c * 11) // 100
            mas[i*height + j] = S
            print(S)
            sleep(0)
      
if __name__ == '__main__':
    a = A()
    b = B()
    c = C()
    
    arr = []
    for i in range(process_count):
        p = Process(target=a, args=(i,mas))
        arr.append(p)
        p.start()
    
    for i in range(process_count):
        p = arr[i]
        p.join()

    print(mas)
    for i in range(width):
        for j in range(height):
            S = mas[i*height + j]
            draw.point((i,j), (S,S,S))
    del draw
    image.save("ans.jpg", "JPEG")
