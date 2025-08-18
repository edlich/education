import java.util.*;

/**
 * Beschreibung: ESA DVC
 *
 * @author Alina Saße 
 * @version 1.00, 06/2025
 */
public class DVC {

    static class Aufgabe {
        String name;
        int geplanteMinuten;
        int prioritaet;
        long echteDauerMillis; // gemessene Zeit in Millisekunden

        Aufgabe(String name, int geplanteMinuten, int prioritaet) {
            this.name = name;
            this.geplanteMinuten = geplanteMinuten;
            this.prioritaet = prioritaet;
            this.echteDauerMillis = 0;
        }

        int getEchteDauerInMinuten() {
            return (int) (echteDauerMillis / 1000 / 60);
        }
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        List<Aufgabe> aufgaben = new ArrayList<>();
        long pausenDauer = 0;

        System.out.print("Wie viele Stunden möchtest du lernen? ");
        int stunden = scanner.nextInt();
        System.out.print("Wie viele Minuten zusätzlich? ");
        int minuten = scanner.nextInt();
        int verbleibendeMinuten = stunden * 60 + minuten;

        scanner.nextLine(); // Scanner-Puffer leeren

        while (true) {
            System.out.println("\nVerbleibende Zeit: " + verbleibendeMinuten / 60 + "h " + (verbleibendeMinuten % 60) + "min");

            String frage = aufgaben.isEmpty() ? "Woran möchtest du dich zuerst setzen? " : "Was steht sonst noch auf dem Plan?";
            System.out.print(frage);
            String name = scanner.nextLine();
            if (name.equalsIgnoreCase("ende")) break;

            System.out.print("Wie viele Minuten soll das dauern? ");
            int geplanteMinuten = scanner.nextInt();
            scanner.nextLine();

            if (geplanteMinuten > verbleibendeMinuten) {
                System.out.println("⚠️ Achtung: Du überschreitest deine verfügbare Zeit!");
            }

            System.out.print("Wie wichtig ist diese Aufgabe? (1 = hoch, 2 = mittel, 3 = niedrig): ");
            int prioritaet = scanner.nextInt();
            scanner.nextLine();

            aufgaben.add(new Aufgabe(name, geplanteMinuten, prioritaet));
            verbleibendeMinuten -= geplanteMinuten;
        }

        // Aufgaben sortieren nach Priorität
        aufgaben.sort(Comparator.comparingInt(a -> a.prioritaet));

        // 🎯 Echte Zeitmessung starten
        System.out.println("\n⏱ Aufgabenbearbeitung beginnt. Drücke [Enter], wenn du bereit bist mit einer Aufgabe zu starten.");
        Map<String, Integer> fachzeiten = new HashMap<>();

        for (Aufgabe a : aufgaben) {
            System.out.println("\n▶️ Aufgabe: " + a.name + " (geplant: " + a.geplanteMinuten + " Min)");
            System.out.print("Drücke [Enter], um zu starten...");
            scanner.nextLine();
            long start = System.currentTimeMillis();

            System.out.println("⏳ Aufgabe läuft... Bearbeite jetzt: " + a.name);
            System.out.print("Drücke [Enter], wenn du fertig bist: ");
            scanner.nextLine();

            long ende = System.currentTimeMillis();
            a.echteDauerMillis = ende - start;

            // Summe nach Thema
            fachzeiten.put(a.name, fachzeiten.getOrDefault(a.name, 0) + a.getEchteDauerInMinuten());

            System.out.println("✅ Fertig! Dauer: " + a.getEchteDauerInMinuten() + " Minuten.");

         // Neue Pausen-Funktion
         System.out.print("😌 Möchtest du eine Pause machen? (j/n): ");
         String pauseAntwort = scanner.nextLine();
         if (pauseAntwort.equalsIgnoreCase("j")) {
             System.out.print("Drücke [Enter], um die Pause zu starten...");
             scanner.nextLine();
             long pauseStart = System.currentTimeMillis();

             System.out.println("🧘‍♂️ Pause läuft... Drücke [Enter], wenn du weitermachen möchtest.");
             scanner.nextLine();

             long pauseEnde = System.currentTimeMillis();
             long pauseDauerMillis = pauseEnde - pauseStart;
             pausenDauer += pauseDauerMillis;

             System.out.println("☕️ Pause beendet! Dauer: " + (pauseDauerMillis / 1000 / 60) + " Minuten.");
         }

        }

        // Ausgabe
        System.out.println("\n📝 Zusammenfassung:");
        for (Aufgabe a : aufgaben) {
            String prio = switch (a.prioritaet) {
                case 1 -> "hoch";
                case 2 -> "mittel";
                case 3 -> "niedrig";
                default -> "unbekannt";
            };
            System.out.println("- [" + prio + "] " + a.name + ": " + a.getEchteDauerInMinuten() + " Minuten (geplant: " + a.geplanteMinuten + ")");
        }

        // 📊 Zeitübersicht nach Thema
        System.out.println("\n📊 Zeitübersicht nach Thema (gemessen):");
        for (Map.Entry<String, Integer> entry : fachzeiten.entrySet()) {
            int min = entry.getValue();
            System.out.println("- " + entry.getKey() + ": " + min / 60 + "h " + (min % 60) + "min");
        }
    }
}
