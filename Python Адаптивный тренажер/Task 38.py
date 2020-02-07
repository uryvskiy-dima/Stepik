"""
Кривая Коха -- это простой геометрический фрактал.
Строится этот фрактал следующим образом: берётся отрезок, разделяется на три равных части. Вместо средней части
вставляется два таких же отрезка, поставленные под углом 60 градусов друг к другу (см. иллюстрацию, переход от n=0 n=0
к n=1 n=1).
Этот процесс повторяется на каждой итерации: каждый отрезок заменяется четырьмя.
Напишите программу, которая принимает на вход число n n - − количество итераций генерации кривой и выводит
последовательность углов поворота при рисовании соответствующей линии от начальной точки к конечной, без отрыва пера.
Способ проверки своего решения приведён на следующем степе.
Формат ввода:
Строка с целым числом n, 1≤ n ≤10.
Формат вывода:
Строки, содержащие последовательность поворотов. Каждый поворот указывается на отдельной строке как слово "turn" и угол
поворота в градусах. Угол поворота должен находиться в интервале [-180; 180].

Sample Input:
1

Sample Output:
turn 60
turn -120
turn 60
"""





import turtle


def koch_turns(n):
    if n == 0:
        turtle.forward(60)
    else:
        for angle in [60, - 120, 60, 0]:
            koch_turns(n - 1)
            turtle.left(angle)
            if angle != 0:
               print(angle)




def turtle_koch_curve(n, speed, sw, sh):
    window = turtle.Screen()  # создали окно
    window.title('Koch curve')  # назвали
    window.screensize(sw, sh)  # задали размер

    mikey = turtle.Turtle()  # создали черепаху
    mikey.speed(speed)  # скорость
    mikey.up()
    mikey.setpos(-sw // 2, -sh // 3)  # позиция
    mikey.down()

    # посчитали необходимую длину линии
    length = sw * 3 // 10
    for _ in range(n - 1):
        length /= 3
    try:
        for move in koch_turns(n):
            mikey.forward(length)
            mikey.left(move)
        mikey.forward(length)
    except:
        pass

    window.exitonclick()  # выход из программы по клику на окно

num = int(input('Deep of Koch:'))
sp = int(input('Speed of drawing:'))
width = int(input('Width of window:'))
height = int(input('Height of window:'))

turtle_koch_curve(num, sp, width, height)