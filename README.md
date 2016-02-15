## Експрес-курс по Python/Теорія інформації та кодування для групи ІБ-21

###UPDATE 1. 
Отже, щоб трошки упростити Вам завдання по пошуку необхідних функцій/команд пропоную використати даний самоучитель http://pythonworld.ru/samouchitel-python. Тут все дуже класно і шо саме головне коротко описано і показані приклади. Звертаю Вашу увагу Python не вимагає від Вас якихось особливих вмінь/навичок написання коду. Якщо хочете розвязати якусь задачу, то спочатку логічно продумайте як ви збираєтесь її розвязувати. 
Для прикладу задача "Якщо а * 4 > 9 вивести значення a, в іншому випадку вивести "дуже маленьке число""
Як думаєте так і записуєте:

1. Нам необхідно ввести якесь значення а. Шукаємо яка команда відповідає за команду введення. Найшли - input()
>     a = input()

2. Нам необхідно знати скільки буде а * 4.
>     b = a * 4

3. Згідно умови задачі якщо(if) a * 4 (в нашому випадку це b) більше девяти (> 9) вивести значення a (print a), в іншому випадку (else:)  вивести (print) "мале число" ("small number"). Складаємо все докупи і получаємо
>     if b > 9:
>        print a
>     else: print "small number"

P.S. Якщо будуть якісь у Вас проблеми - підходьте, спробую пояснити. 

###Індивідуальні домашні завдання:
Реєструємося за наступним посиланням http://informatics.mccme.ru/login/signup.php
В графі школа вказуємо LSULS. Входимо під своїм аккаунтом і переходим за посиланням http://informatics.mccme.ru/course/view.php?id=1434. Вибираємо практичні завдання на текущий тиждень, і вирішуємо. Для цього в графі "Сдать" нажимаємо "Выбор файла" і закідуємо наше рішення, справа вибираємо мову програмування і нажимаємо "Отправить". Не переживайте якщо в Вас якусь задачу не зарахує, я потім все перегляну. Додатково розберіться в Github-i, підпишіться на даний репозитарій і в своєму власному заливайте розвязки задач в якості практики.

##Лабораторні роботи, які необхідно буде виконати:
1. Ймовірнісний підхід до вимірювання обсягу дискретної інформації;
2. Кодування Шеннона-Фено;
3. Кодування Хаффмена;
4. Арифметичне кодування;
5. Адаптивне арифметичне кодування;
6. Алгоритми LZ77, LZSS;
7. Алгоритми LZ78, LZW;
Додаткову інформацію по ним буду заливати в папку Lab.

