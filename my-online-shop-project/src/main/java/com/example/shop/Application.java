package com.example.shop;

public class Main {
    public static void main(String[] args) {
        ProductManager productManager = new ProductManager();
        while (true) {
            System.out.println("\n1. Add Product\n2. Show Products\n3. Update Product\n4. Remove Product\n5. Search Product\n6. Exit");
            System.out.print("Choose an option: ");
            int choice = productManager.scanner.nextInt();
            productManager.scanner.nextLine(); // consume newline
            switch (choice) {
                case 1:
                    productManager.addProduct();
                    break;
                case 2:
                    productManager.showProducts();
                    break;
                case 3:
                    productManager.updateProduct();
                    break;
                case 4:
                    productManager.removeProduct();
                    break;
                case 5:
                    productManager.searchProduct();
                    break;
                case 6:
                    return;
                default:
                    System.out.println("Invalid choice.");
            }
        }
    }