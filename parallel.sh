#!/bin/bash

URL='http://127.0.0.1:64435/factorial?n=1000'  # Замените хост/порт

COUNT=10000

# Генерируем последовательность чисел и запускаем curl параллельно с xargs
seq $COUNT | xargs -I{} -P $COUNT curl "$URL" -H 'accept: application/json'
