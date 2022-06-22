#!/bin/bash

printf "\n"
if [ $# -ne 1 ]; then
    echo Bitte nur die Anzahl der Pizzen angeben!
    exit 1
fi

echo "Mehl (glatt): $(($1*150))g"
echo "Wasser:       $(($1*85))ml"
echo "Olivenoel:    $(($1*7))ml"
echo "Frischhefe:   $(($1*7))g"
echo "Salz:         $(($1*3))g"
echo "Zucker:       ca. 1 Prise"
printf "\n"

printf "Im lauwarmen Wasser und dem Olivenoel die Hefe mit dem Salz und Zucker aufloesen. \nDann das Mehl hinzufuegen und einen glatten Teig kneten. \nEine halbe Stunde an einem warmen Ort gehen lassen, \nzusammenkneten und abgedeckt im Kuehlschrank 2 Tage ruhen lassen."

printf "\n"
printf "\n"
echo "Guten Appetit!"

printf "\n"
echo "Quelle: https://www.chefkoch.de/rezepte/716331174378295/Italienischer-Pizzateig.html (22.06.2022)"