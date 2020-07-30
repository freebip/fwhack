# Немного о show_big_digit

Есть в библиотеке Libbip такая функциия show_big_digit (адрес 0x080204BC для FW 1.1.5.36 latin) с прототипом:

```
// отображение цифр большим шрифтом
extern void show_big_digit(int color, const char * digits, int pos_x, unsigned int pos_y, int space);
```

Занимаясь написанием эмулятора BipEmulator пришлось эту функцию эмулировать и как следствие
изучать, что это за функция такая и чем она занимается.
Как показало изучение прошивки, название функции не совсем отражает её суть, а первый аргумент,
так и вовсе отвечает не за цвет.

По-сути это функция печати символов на экране, только в отличии text_out и text_out_center,
растры символов она берет не из файла шрифтов (.ft), а из файла ресурсов.

Проектировали эту функцию тупо т.к. таблица символов, ширина каждого символа и идентификатор
ресурса жестко запрограммирована в прошивке, ну а данные соответственно, ресурсы, лежат
в файле ресурсов. Изменяя данные либо в прошивке, либо в ресурса, потребуют двойную работу
по изменению данных в ресурсах, либо прошивке соответственно.

Ясно-понятно в ресурсах символы поместили, чтобы каждый создатель программ мог их использовать,
но секундочку ведь создатель программ для часов и создатель прошивки он же как бы официально всего один ...

Итак, первый символ отображает не цвет, а номер набора символов, которые данная функция может 
отображать. Наборов всего 16 (0-15), с разным количеством символов в каждом наборе.
Чтобы оценить все прелести шрифтов и в дальнейшем выбрать шрифт для ваших приложений, я
сформировал картинки с каждым набором символов.

### Набор 0.

![alt-текст](https://github.com/freebip/fwhack/raw/master/images/symset_00.png)

### Набор 1.

![alt-текст](https://github.com/freebip/fwhack/raw/master/images/symset_01.png)

### Набор 2.

![alt-текст](https://github.com/freebip/fwhack/raw/master/images/symset_02.png)

### Набор 3.

![alt-текст](https://github.com/freebip/fwhack/raw/master/images/symset_03.png)

### Набор 4.

![alt-текст](https://github.com/freebip/fwhack/raw/master/images/symset_04.png)

### Набор 5.

![alt-текст](https://github.com/freebip/fwhack/raw/master/images/symset_05.png)

### Набор 6.

![alt-текст](https://github.com/freebip/fwhack/raw/master/images/symset_06.png)

### Набор 7.

![alt-текст](https://github.com/freebip/fwhack/raw/master/images/symset_07.png)

### Набор 8.

![alt-текст](https://github.com/freebip/fwhack/raw/master/images/symset_08.png)

### Набор 9.

![alt-текст](https://github.com/freebip/fwhack/raw/master/images/symset_09.png)

### Набор 10.

![alt-текст](https://github.com/freebip/fwhack/raw/master/images/symset_10.png)

### Набор 11.

![alt-текст](https://github.com/freebip/fwhack/raw/master/images/symset_11.png)

### Набор 12.

![alt-текст](https://github.com/freebip/fwhack/raw/master/images/symset_12.png)

### Набор 13.

![alt-текст](https://github.com/freebip/fwhack/raw/master/images/symset_13.png)

### Набор 14.

![alt-текст](https://github.com/freebip/fwhack/raw/master/images/symset_14.png)

### Набор 15.

![alt-текст](https://github.com/freebip/fwhack/raw/master/images/symset_15.png)
