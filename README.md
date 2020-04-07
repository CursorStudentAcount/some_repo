## 1
```
Кирпич весит 1 кг плюс половина от веса кирпича -- сколько весит кирпич?
```

Щоб вирішити цю задачу, можна скласти звичайне лінійне рівняння:
x = 1 + 0.5x
0.5x = 1
x = 2


## 2
```
В массиве любого размера с целыми числами от 1 до 500,000 одно число повторяется дважды, все остальные числа уникальны.
 Предложите наиболее быстрый алгоритм поиска повторяющегося числа.
```

Я пропоную створити HashMap та ітеруватися по масиву, зберігаючи дані в мапу до моменту, коли ключ у HashMap вже існує.

## 3
```
Смотря в небо три минуты вероятность заметить самолет составляет 60%.
Определите вероятность заметить самолет за одну минуту и объясните решение.
```
Перше рішення виглядало ось так:
Все залежить від того, наскільки рівномірно летять літаки. 
Якщо за 3 хв шанс побачити 60% (це всі дані, що в нас є з умови), то допускаю, що літак пролітає кожні 5 хв 
і це регулярно повторювана дія. 
У такому випадку, якщо дивитися 1 хвилину, то шанс побачити 20%.  
1хв - Пролітає літак.  
2хв - Нічого не коїться(Важливого для задачі)  
3хв - Нічого не коїться(Важливого для задачі)  
4хв - Нічого не коїться(Важливого для задачі)  
5хв - Нічого не коїться(Важливого для задачі)  
6хв - Пролетів регулярний літак.  
Літак буде видно тільки для тих спостерігачів, які почали дивитися о 5 хвилині. 

Рішення 2: 
Пошукавши на простарах інтеренету схожого типажу задачі бачу інше рішення

Ми не можемо стверджувати про регулярність польоту літаків.
Проте ми можемо скласти рівняння для отримання вірогідності того, що літак не з'явиться. 


Якщо вірогідність побачити літак 60% за 3 хвилини, вірогідність не побачити його за 3 хвилини рівна 40%
Щоб не побачити його за 3 хвилини нам треба не побачити його за першу хвилину 
не побачити його за другу і не побачити його за третю 

(1 - X) * (1 - X) * (1 - X) = 0.4, де X -> вірогідність побачити літак за 1 хвилину. 

1 - X = ∛0.4
X = 1 - 0.7368
X = 0.2632 

Вірогідність побачити літак за 1 хвилину 26 відсотків.

## 4
```напишите консольную программу которая будет обходить матрицу улиткой начиная с левого верхнего угла. На входе, параметрами 2 числа, размерность матрицы IxJ, на выходе список текущих координат для каждой посещенной точки. Например:
visit.py 3x3
0,0
0,1
0,2
1,2
2,2
2,1
2,0
1,0
1,1
```
### Run tests 
python -m unittest test_snail.py 


### Run script 
python snail.py 3x3
>> [(0, 0), (0, 1), (0, 2), (1, 2), (2, 2), (2, 1), (2, 0), (1, 0), (1, 1)]


## 5
```
Напишите консольную программу которая по заданному числу находит обратное ему бинарное число
 (13 => 1101, обратное ему (читаем справа налево) 1011 => 11).
На входе параметром число N 1<= N <= 1000000000, на выходе обратное число
```

### Run tests 
`python -m unittest test_reverse_bin`

### Run script
`python reverse_bin.py 13`
>> 11
