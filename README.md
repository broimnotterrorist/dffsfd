# selica-php-botnet

![image](https://user-images.githubusercontent.com/90555583/169706841-77efbf0b-070c-40c8-aa8c-75eb555f8689.png)


Запуск скрипта: python3 main.py

Загрузить ботов: bots


Как добавить ботов?

Создаем много аккаунтов на https://sprinthost.ru/ и заливаем на него файлик payload.php

Копируем ссылку на этот файл, вставляем в файл bots.txt

В скрипте пишем refresh (если скрипт уже был запущен), если первый запуск - пишем bots

Если боты отобразились в консоли - пишем install (установка методов на бота)

Использование: 

L7: .method_id host time

L4 .method_id host port time



1 бот выдает около 150к запросов по л7, л4 - около 100мб/с (в зависимости от хостинга)
