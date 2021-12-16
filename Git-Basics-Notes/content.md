# BASICS

![image](2FB12856-88CC-40CF-BB4D-AB634848B55F.jpg)
### Git-Repository anlegen
> Repository in bestehendem Verzeichnis einrichten
>  ```css
> $ git init
> ```

### Existierendes Repository klonen
> lädt jede Version von jeder Datei der Projekt-> >Historie
>
> ```css  
>git clone [url]
>
> // geklontes Verzeichnis eigenen Namen geben
>$ git clone https://github.com/libgit2/libgit2 >mylibgit // <-- mylibgit = eigener Name
>```
> >

 ### Zustand von Dateien prüfen  
> ```css
> git status
> ```
>
> **Kurzform**
> ?? = Datei nicht versioniert
> A = neue Dateien (die der Staging-Area hinzugefügt wurden)
> M = geänderte Dateien
> ```css
> // Kurzform
> git status --short
> -----------------------------------------------------------------------
> $ git status -s
> M README
> MM Rakefile
> A  lib/git.rb
> M  lib/simplegit.rb
> ?? LICENSE.txt
> ```￼


### Anzeigen von Änderungen (detailliert)
> zeigt genau die hinzugefügten und entfernten Zeilen (git status zeigt nur geänderte Datei an)
> * zeigt nicht alle Änderungen seit Ihrem letzten Commit an – nur die Änderungen, die noch „unstaged“ sind
>```css
> git diff
>```



### Stagen – Neue Dateien zur Versionsverwaltung hinzufügen
> neue Dateien zur Versionsverwaltung hinzuzufügen
> (bestimmten Inhalt für den nächsten Commit vormerken)
> * wenn Änderungen an File vorgenommen wurden, werden diese rot angezeigt
> 	--> mittels git add <filename> lässt sich Datei dann für commit vormerken
> * Git merkt sich eine Datei  für den Commit in exakt dem Zustand, in dem sie sich befindet, wenn Befehl git add ausgeführt wurde
>
> ```css
> git add <file>
>
> ```
### git ignore
> * ziemlich umfassende Liste guter .gitignore Beispiel-Dateien für Dutzende von Projekten und Sprachen auf https://github.com/github/gitignore
>

### Comitten
> * Commit zeichnet Snapshot auf, der in Staging-Area eingerichtet wurde (und nur den)
> * Alles, was nicht zum Commit vorgemerkt wurde, liegt immer noch als modifiziert da.
> *  Sie können einen weiteren Commit durchführen, um es zu Ihrer Historie hinzuzufügen. Jedes Mal, wenn Sie einen Commit ausführen, zeichnen Sie einen Schnappschuss Ihres Projekts auf, auf den Sie zurückgreifen oder mit einem späteren Zeitpunkt vergleichen können.
> ```css
> git commit
> // Variationen:
> git commit -v // --> Differenz Ihrer Änderung in den Editor geschrieben, so dass Sie genau sehen können, welche Änderungen Sie committen
> git commit -m // --> erlaubt direkte Eingabe eines Kommentartextes
>
> **Staging-Area überspringen**
> **-a** = jede Datei, die bereits vor dem Commit versioniert war automatisch zum Commit vorgemerken (git add überspringen)
> ```css
> git commit -a -m 'Add new benchmarks'
>
> ```￼
 ￼
### Dateien löschen
> **Datei aus Git zu entfernen** = aus der Versionsverwaltung entfernen (genauer gesagt, aus Staging-Bereich löschen) und dann committen
> * wenn Datei geändert oder bereits zur Staging-Area hinzugefügt, muss das Entfernen mit der Option **-f** erzwungen werden (=Sicherheitsfunktion, die ein versehentliches Entfernen von Dateien verhindert, die noch nicht in einem Snapshot aufgezeichnet wurden und die nicht von Git wiederhergestellt werden können)
> ```css
> git rm / git rm -f
> ```
> **Datei auf Festplatte behalten, aber nicht mehr von Git protokollieren/versionieren lassen**
> * z.B. wenn versehentlich „gestaged“
> ```css
> git rm --cached README
> ```
