package Birb;

import java.util.Random;
import java.util.Scanner;

public class BirbGPT {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Random random = new Random();

        System.out.println("Willkommen zu BirbGPT! Geben Sie ihre Frage ein:");

        while (scanner.hasNext()) {
            String input = scanner.nextLine();

            // Generiere eine zufällige Anzahl von Piep-Wiederholungen
            int numberOfPeeps = random.nextInt(25) + 1;  // Zahl zwischen 1 und 25
            StringBuilder response = new StringBuilder("Piep");

            for (int i = 1; i < numberOfPeeps; i++) {
                response.append(" Piep");
            }
            response.append("!");

            System.out.println(response.toString());
        }
        
        scanner.close();
    }
}