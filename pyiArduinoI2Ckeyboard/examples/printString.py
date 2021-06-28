# ДАННЫЙ ПРИМЕР ВЫВОДИТ СТРОКУ В МОНИТОР:           #
# (нажимайте кнопки и ждите их появления)           #
                                                    #
from pyiArduinoI2Ckeyboard import *                 #   Подключаем библиотеку для работы с клавиатурой I2C-flash.
from time import sleep
kbd = pyiArduinoI2Ckeyboard(0x09,4,2)               #   Объявляем объект kbd для работы с функциями и методами библиотеки pyiArduinoI2Ckeyboard, указывая адрес модуля на шине I2C, количество кнопок в линии, количество линий с кнопками.
                                                    #   Если объявить объект без указания адреса (pyiArduinoI2Ckeyboard kbd(false,4,2) ), то адрес будет найден автоматически.
                                                    #
kbd.setEncoding("abcd012\n")                        # * Присваиваем символы всем кнопкам клавиатуры. По умолчанию кнопкам присвоены символы "12345678".
kbd.setEncoding(4,1,'f')                            # * Символ можно присвоить каждой кнопке по отдельности (присвоить 4 кнопке, в 1 ряду, символ 'f').
                                                    #
while True:                                         #
#  Получаем и выводим строку символов с клавиатуры: #
    if kbd.available():                             #   Если в буфере истории нажатий кнопок есть символы, то ...
       myString, _ = kbd.readString(49)             #   Читаем не более 49 символов из буфера истории нажатий кнопок в строку myString.
       print(myString)                              #   Выводим строку myString.
#  Тут может быть код с большими задержками:        #
    sleep(10)                                       #   Пока система "отдыхает", клавиатура мониторит нажатые клавиши и сохраняет их в свой буфер историй.
                                                    #
#  Буфер историй нажатий кнопок находится в модуле  #
#  клавиатуры, память которого равна 255 байт.      #
#                                                   #
#  Функция available() возвращает количество        #
#  символов находящихся в буфере клавиатуры.        #
#  Буфер можно очистить функцией flush().           #
#                                                   #
#  В примере printChar данные из буфера читаются    #
#  не целой строкой, а посимвольно readChar().      #
