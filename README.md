# Group_Up
<h3> Пособие для чайников по запуску сервера: </h3>

1) Скачиваем и устанавливаем PyCharm Community Edition https://www.jetbrains.com/pycharm/download/#section=windows
2) Скачиваем и устанавливаем GIT https://git-scm.com/downloads
3) Скачиваем и устанавливаем Python версии 3.8 https://www.python.org/downloads/
4) Открываем PyCharm Community Edition выбираем пункт Check out from Version Control там выбираем подпункт GIT https://prnt.sc/py683m
5) Вставляем ссыллку на репозиторий в пункте URL выбираем дерикторию и нажимаем Clone https://prnt.sc/py69oh
6) После копирования проекта сохдаем виртуальное окружение и выбираем интерпритатер, нажимаем сочитание клавиш для WIN (CTRL + ALT + S) или для OSX (COMMAND + , ) выбираем пункт Project:ИМЯ_ПРОЕКТА далее выбираем Project interpreter нажимаем по шестеренке и выбираем пункт Add... https://prnt.sc/py6f9l
7) В появившемся меню выбираем Virtualenv Environment выбираем чекбокс New environment выбираем базовый интерпиритатор и расположение файлов виртуальной оболочки для удобства чтобы на сервер не загружалась ваша личная оболочка называем папку venv и нажимаем кнопку OK https://prnt.sc/py6hjy после нажимаем Apply 
8) Теперь устанавливаем сторонние библиотеки в нашу среду, в низу нашей IDEA выбираем терминал https://prnt.sc/py6k63 и вводим поочередно туда эти команды список будет со временем увиличеваться ( pip install django ), ( pip install py-trello ), ( pip install Pillow )
9) Теперь вводим в консоль комманду ( python manage.py runserver )
10) Сервер запущен теперь просто заходим в браузер и переходим по ссылке http://127.0.0.1:8000/

<h3> Несколько небольших пометок: </h3>

<ul>
  <li> Статичные файлы как шрифты, стили, скрипты, картинки храняться в папке static </li>
  <li> Админ панель находиться по ссылке http://127.0.0.1:8000/admin/ </li>
  <li> HTML код находиться в папке templates/названия_приложения/ </li>
  <li> Ссылки в коде на стотичные файлы формируються автоматически поэтому на месте ссылки вводим такую конструкцию {% static 'ПАПКА_ТИПА_ФАЙЛА/ФАИЛ' %}
</ul>
