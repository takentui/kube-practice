#!/bin/bash

URL='http://127.0.0.1:64701/sleep'  # Замените порт

COUNT=10

# Генерируем последовательность чисел и запускаем curl параллельно с xargs
seq $COUNT | xargs -I{} -P $COUNT curl -X 'POST' "$URL" -H 'accept: application/json'
