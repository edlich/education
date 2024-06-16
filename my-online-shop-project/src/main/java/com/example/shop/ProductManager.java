package com.example.shop;

import java.util.ArrayList;
import java.util.Scanner;

public class ProductManager {
    private ArrayList<Product> products;
    private Scanner scanner;

    public ProductManager() {
        products = new ArrayList<>();
        scanner = new Scanner(System.in);
    }

    public void addProduct() {
        System.out.print("Enter product ID: ");
        String id = scanner.nextLine();
        System.out.print("Enter product name: ");
        String name = scanner.nextLine();
        System.out.print("Enter product price: ");
        double price = scanner.nextDouble();
        scanner.nextLine(); // consume newline
        products.add(new Product(id, name, price));
        System.out.println("Product added.");
    }

    public void showProducts() {
        System.out.println("Products:");
        for (Product product : products) {
            System.out.println(product);
        }
    }

    public void updateProduct() {
        System.out.print("Enter product ID to update: ");
        String id = scanner.nextLine();
        for (Product product : products) {
            if (product.getId().equals(id)) {
                System.out.print("Enter new product name: ");
                String name = scanner.nextLine();
                System.out.print("Enter new product price: ");
                double price = scanner.nextDouble();
                scanner.nextLine(); // consume newline
                product.setName(name);
                product.setPrice(price);
                System.out.println("Product updated.");
                return;
            }
        }
        System.out.println("Product not found.");
    }

    public void removeProduct() {
        System.out.print("Enter product ID to remove: ");
        String id = scanner.nextLine();
        products.removeIf(product -> product.getId().equals(id));
        System.out.println("Product removed.");
    }

    public void searchProduct() {
        System.out.print("Enter product ID to search: ");
        String id = scanner.nextLine();
        for (Product product : products) {
            if (product.getId().equals(id)) {
                System.out.println(product);
                return;
            }
        }
        System.out.println("Product not found.");
    }
	// Feature-Branch 1: Fügt eine Methode zur Produktsuche hinzu
	// Feature-Branch 2: Fügt eine Methode zur Produktaktualisierung hinzu

