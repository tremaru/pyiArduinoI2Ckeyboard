# ДАННЫЙ ПРИМЕР УПРАВЛЯЕТ СВЕТОДИОДАМИ КНОПОК:                      #
                                                                    #
from pyiArduinoI2Ckeyboard import *                                 #   Подключаем библиотеку для работы с клавиатурой I2C-flash.
from time import sleep
kbd = pyiArduinoI2Ckeyboard(0x09,4,2)                               #   Объявляем объект kbd для работы с функциями и методами библиотеки pyiArduinoI2Ckeyboard, указывая адрес модуля на шине I2C, количество кнопок в линии, количество линий с кнопками.
                                                                    #   Если объявить объект без указания адреса (pyiArduinoI2Ckeyboard kbd(False,4,2) ), то адрес будет найден автоматически.
kbd.setEncoding(3,1,'s')                                            # * Присваиваем 3 кнопке в 1 ряду символ 's'.
                                                                    #
while True:                                                         #
#  Выполняем действия независимо от состояния клавиш:               #
    kbd.setLed(1,1,True),                        sleep(.5)          # Включаем светодиод 1 кнопки в 1 ряду.
    kbd.setLed(2,2,True), kbd.setLed(1,1,False), sleep(.5)          # Включаем светодиод 2 кнопки в 2 ряду и выключаем светодиод 1 кнопки в 1 ряду.
    kbd.setLed('s',True), kbd.setLed(2,2,False), sleep(.5)          # Включаем светодиод 3 кнопки в 1 ряду и выключаем светодиод 2 кнопки в 2 ряду.
    kbd.setLed(4,2,True), kbd.setLed(3,1,False), sleep(.5)          # Включаем светодиод 4 кнопки в 2 ряду и выключаем светодиод 3 кнопки в 1 ряду.
    kbd.setLed(4,2,False), sleep(.5)                                #                                        выключаем светодиод 4 кнопки в 2 ряду.
    kbd.setLed(LED_ALL,0b10100101),              sleep(.5)          # Управляем всеми светодиодами. Биты 0-3 управляют светодиодами 1-4 в 1 ряду, см. пример getAllKeyState.
    kbd.setLed(LED_ALL,0b01011010),              sleep(.5)          # Управляем всеми светодиодами. Биты 4-7 управляют светодиодами 1-4 в 2 ряду, см. пример getAllKeyState.
    kbd.setLed(LED_ALL,0b00000000),              sleep(.5)          # Выключаем все светодиоды.
    kbd.setLed(LED_ALL,0b11111111),              sleep(.5)          # Включаем  все светодиоды.
    kbd.setLed(LED_ALL,0b00000000),              sleep(.5)          # Выключаем все светодиоды.
                                                                    #
#  ПРИМЕЧАНИЕ:                                                      #
#  Так как функцией setEncoding(), в коде Setup(), 3 кнопке 1 ряда  #
#  был присвоен символ 's', то обращаться к светодиоду этой кнопки  #
#  можно либо по номеру и ряду, либо по привоенному ей символу.     #
