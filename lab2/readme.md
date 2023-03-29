\usepackage{amsmath}

## Лабороторная работа №2

### Задание 1

Построить зависимость между количеством элементов и количеством шагов для алгоритмов со сложностью $ О(1) $, $ O(log n) $, $ O(n^2) $, $ O(2^n) $. Сравнить сложность данных алгоритмов.

### Задание 2

Написать программу для пузырьковой сортировки. Оценить сложность данного метода. Сравнить с методом sort

### Задание 3

Придумать и реализовать алгоритмы, имеющие сложность $ O(3n) $, $ O(nlogn) $, $ O(n!) $, $ O(n^3) $, $ O(3log(n)) $

var md = require('markdown-it')(),
    mathjax3 = require('markdown-it-mathjax3');

md.use(mathjax3);

// double backslash is required for javascript strings, but not html input
var result = md.render('# Math Rulez! \n  $\\sqrt{3x-1}+(1+x)^2$');