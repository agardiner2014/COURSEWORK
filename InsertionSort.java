/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package Insert;

import java.util.Random;

/**
 *
 * @author Ace
 */
public class InsertionSort {
    
 
    public static void main(String[] args) {
         
        int size = 1000;
        int max = 32000; 
 

        Random generator = new Random();
 
        while (size != 21000)
        {
            double sum = 0;
            int[] input = new int[size];
            System.out.print("Wave "+ input.length + "\n");
            for (int m = 0; m < 10; m++)
            {
                for (int i =0; i<size; i++)
                {
                    input[i] = generator.nextInt(max);
                }
                
                long startTime = System.currentTimeMillis();
                insertionSort(input);
                long endTime = System.currentTimeMillis();
                long result = endTime-startTime;
                sum += result;
                printNumbers(input);
            
            } 
            System.out.print("The Avg Runtime: " + (sum/10) + " milliseconds"+ "\n");
            System.out.print("\n");
            size += 1000;
        
        }
    }
     
    private static void printNumbers(int[] input) {
         
        for (int i = 0; i < input.length; i++) {
            System.out.print(input[i] + ", ");
        }
        System.out.println("\n");
    }
 
    public static void insertionSort(int array[]) {
        int n = array.length;
        for (int j = 1; j < n; j++) {
            int key = array[j];
            int i = j-1;
            while ( (i > -1) && ( array [i] > key ) ) {
                array [i+1] = array [i];
                i--;
            }
            array[i+1] = key;
        }
    }
}

    
