# Telegram-бот для преобразования аудио в текст

## Описание
В учебном проекте реализован простейший Telegram-бот для преобразования аудиосообщения в текст

Будьте внимательны: знаки препинания не проставляются!

Бот работает через метод полинга

Проект выполнен на языке Python 3.9

Используемые библиотеки и пакеты сохранены в файле requirements.txt

## Как запустить проект

Перед запуском проекта необходимо создать собственного Telegram-бота

### Создание Telegram-бота

Для создания Telegram-бота требуется выполнить некотрые действия в Telegram:

* в окно поиска над списком контактов ввести @BotFather
* среди полученного списка выбрать одноименный Telegram-бот с иконкой в виде белой галочкой на голубом фоне (шестеренка?)

> Ради Вашего же блага будьте внимательны и остерегайтесь подделок!

* в Telegram-боте @BotFather нажать кнопку ***Start***
* ввести команду ```/newbot```
* ввести имя вашего бота, под которым он будет отображаться (читайте сообщения, которые Вам высылает Telegram-бот)
* ввести техническое имя вашего бота, по которому его можно будет найти в Telegram. Имя должно оканчиваться на слово ```bot``` (читайте сообщения, которые Вам высылает Telegram-бот)

После успешного создания Telegram-бота Вам придет сообщение с поздравлениями и его данными. Под строкой ```Use this token to access the HTTP API:``` указан токен. Он Вам понадобится дальше

### Запуск проекта

**Клонировать репозиторий:**

```
git clone https://github.com/Anquientas/bot_transform_audio.git
```

**Перейти в склонированный репозиторий в командной строке:**

```
cd bot_transform_audio
```

**Cоздать  виртуальное окружение (рекомендуется использовать Python 3.9):**

* для Linux:

    + *без учета версии*

    ```
    python3 -m venv venv
    ```

    + *с учетом версии*

    ```
    python3.9 -m venv venv
    ```

> Далее в командах для Linux версия Python не указывается, т.е. команды будут начинаться с ```python3```.

> Если при создании виртуальной машины указана конкретная версия, например, ```python3.9```,  то команды следует начинать с нее

* для Windows:

    + *без учета версии*

    ```
    py -m venv venv
    ```

    + *с учетом версии*

    ```
    py -3.9 -m venv venv
    ```

> Python в Windows после создания виртуальной машины не требует постоянного указания используемой версии, поэтому указанные далее команды можно использовать без оглядки на версию

**Активировать виртуальное окружение:**

* для Linux:

```
source venv/bin/activate
```

* для Windows:

```
source venv/Scripts/activate
```

**Обновить установщик пакетов Python до последней версии (рекомендуется):**

* для Linux:

```
python3 -m pip install --upgrade pip
```

* для Windows:

```
py -m pip install --upgrade pip
```

**Установить зависимости из файла requirements.txt:**

```
pip install -r requirements.txt
```

**Установить токен Telegram-бота:**

* изменить расширение файла ```.env.example``` на ```.env```
* с помощью текстового редактора открыть файл
* после указанной переменной приписать ```=``` и токен, полученный в чате от Telegram-бота BotFather
* сохранить файл

**Запусть программу:**

* для Linux:

```
python3 -m main.py
```

* для Windows:

```
py -m main.py
```

**Запустить Telegram-бот:**

Перейдите в свой созданный Telegram-бот и отправьте команду ```/start```

**Отправить сообщение:**

Отправьте голосовое сообщение и получите его в тексте

***Повторить последнее действие столько раз, сколько нужно :)***

## Остановка работы проекта

Для остановки работы бэка Telegram-бота нажмите в консоли комбинацию клавиш ```Ctrl+C```

## Перезапуск проекта

Для повторного запуска проекта достаточно выполнить действия, указанные в пункте "Запустить программу" в подразделе "Запуск проекта"

## Проблемы при запуске проекта

Если при запуске проекта возникли проблемы, то попробуйте сначала прочитать файлы в папке ```help```

Удачи :)