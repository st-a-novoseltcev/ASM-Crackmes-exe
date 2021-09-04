# ASM-Crackmes-exe

Репозиторий содержит непосредственно исполняемые файлы для обратной разработки.

# Задание

Нужно найти необходимые для корректной работы программы входные данные,
или **полностью** обезвредить в каждой из программ механизмы, отвечающие за 
ее защиту.

**Для сдачи необходимо написать скрипт**, который будет производить
патчинг программ в автоматическом режиме. Язык скрипта -- по желанию.
Рекомендуется использовать python, благодаря его предрасположенности к 
быстрому прототипированию.

Задачки будут сопротивляться вашим попыткам себя взломать, имейте это в виду.

**Если вы решились, то Fork'айте данный репозиторий и работайте в нем.
Это повышает как удобство сдачи, так и сохранность ваших трудов.**


Не хотите ставить линукс, но хотите решить задачи?
Воспользуйтесь [CODENVY](https://bellard.org/jslinux)

## Цели
 + cp -- найти ключ активации или снять полностью защиту
 + tp -- найти ключ активации или снять полностью защиту (ключ состоит из нескольких слов, разделенных пробелом)
 + game -- набрать трижды 10 очков в тетрисе

## Подсказка к решению crackme's

Все задачи решаются следующим итеративным процессом:

 1. Запускаем программу
 1. Видим, что что-то работает не так, как нам бы хотелось
 1. Догадываемся, где может находиться это место.
    Например мы уверены, что в интересном месте
    используется библиотечная функция -- ищем
    места ее иcпользования.
 1. Смотрим, как можно изменить найденное интересное место,
    желаемым образом, чтобы изменения уместились на том же месте, что
    занимали инструкции.


## Полезное

Для исследования и патчинга исполняемых файлов я советую использовать:

+ [rr](https://rr-project.org/) для безвременного дебаггинга -- сначала записывается
исполнение программы, а отлаживается уже запись
+ [radare2](https://rada.re/n/) для дизассемблирования исполняемых файлов
+ objdump -- для дизассемблирования исполняемых файлов
+ xxd -- для бинарного патчинга
+ gdb -- для отладки исполняемого файла
+ strings -- для вывода строк исполняемого файла
+ strace -- для трассирования системных вызовов

Если не понятно, как работает та или иная программа, то 
вызывайте ее с ключем `-h`, `--help` или командой `man программа`.

### Полезные команды в gdb

В gdb все команды полезные, но больше всего должны пригодиться:

+ В gdb есть автодополнение команд -- нужно нажать Tab
+ `set disassembly-flavor [att|intel]` -- выставляет диалект для ассемблерных листингов
+ `i r` -- просмотр значений всех регистров
+ `layout [asm|regs|...]` -- создает TUI для наглядности работы. Нужно заметить, что в таком
режиме для управления вводом не работают стрелочки, так как они двигают ассемблерный листинг.
Выйти из положения можно следующими комбинациями клавиш:
  - `ctrl+f` -- движение вперед (forward).
  - `ctrl+b` -- движение назад (back).
  - `ctrl+d` -- то же, что и Delete
  - при замене `ctrl` на `alt`, операции проходят со словами (т.е с [0-9a-zA-Z_]* до пробела или -)
  - `ctrl+u` -- удаляет все до начала строки
  - `ctrl+k` -- удаляет все до конца строки
  - все удаленное предыдущими командами можно вернуть нажав `ctrl+y`
  - `ctrl+p` -- предыдущая команда
  - `ctrl+n` -- следующая команда
+ `ni` -- выполнить инструкцию без перехода в подпроцедуру 
+ `si` -- выполнить инструкцию с переходом в подпроцедуру 
+ `set си-выражение` -- например `set *((char*)$rsp) = 0` зануляет байт, на который указывает регистр `rsp`.
+ `x` -- посмотреть, что находится по некоторому адресу (examine).
+ `starti` -- остановить исполнение программы на самой первой инструкции (правда может остановиться в сторонней библиотеке)
+ `bt` -- вывести стек вызовов


# Полезные ссылки

+ [Онлайн ассемблер отдельных инструкций](https://defuse.ca/online-x86-assembler.htm)
+ [Онлайн исследование скомпилированного кода](https://godbolt.org/)


# sha1sum

```
ae6146ce6c7b2c7627a76fb8bfd242b2ed3cfa78  cp
c20d2645bf7ac1b4aa4f6571f84b24bae6003ad9  game
c4703ab2c555b4e8bd3509bfc109bad32a1e1670  tp
```
