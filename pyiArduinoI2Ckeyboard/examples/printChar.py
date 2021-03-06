# ДАННЫЙ ПРИМЕР ПОСИМВОЛЬНО ВЫВОДИТ СТРОКУ:         #
# (нажимайте или удерживайте кнопки клавиатуры)     #
                                                    #
from pyiArduinoI2Ckeyboard import *                 #   Подключаем библиотеку для работы с клавиатурой I2C-flash.
kbd = pyiArduinoI2Ckeyboard(0x09,4,2)               #   Объявляем объект kbd для работы с функциями и методами библиотеки pyiArduinoI2Ckeyboard, указывая адрес модуля на шине I2C, количество кнопок в линии, количество линий с кнопками.
                                                    #   Если объявить объект без указания адреса (pyiArduinoI2Ckeyboard kbd(false,4,2) ), то адрес будет найден автоматически.
kbd.setEncoding("abcd0123")                         # * Присваиваем символы всем кнопкам клавиатуры. По умолчанию кнопкам присвоены символы "12345678".
kbd.setEncoding(4,1,'f')                            # * Символ можно присвоить каждой кнопке по отдельности (присвоить 4 кнопке, в 1 ряду, символ 'f').
kbd.setEncoding(4,2,'\n')                           # * Символ можно присвоить каждой кнопке по отдельности (присвоить 4 кнопке, в 2 ряду, символ новой строки '\n').
                                                    #
while True:                                         #
    #  Получаем и выводим символы с клавиатуры:     #
    if kbd.available():                             #   Если в буфере истории нажатий кнопок есть символы, то ...
        print(kbd.readChar())                       #   Выводим очередной символ из буфера истории нажатий кнопок.
                                                    #
#  ПРИМЕЧАНИЕ:                                      #
#  Буфер историй нажатий кнопок находится в модуле  #
#  клавиатуры, память которого равна 255 байт.      #
#                                                   #
#  Функция available() возвращает количество        #
#  символов находящихся в буфере клавиатуры.        #
#  Буфер можно очистить функцией flush().           #
#  В примере printString данные из буфера читаются  #
#  не посимвольно readChar(), а все сразу одной     #
#  строкой readString().                            #
