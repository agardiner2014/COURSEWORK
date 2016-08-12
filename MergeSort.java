/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package Merge;

import java.util.Random;

/**
 *
 * @author Ace
 */
public class MergeSort {
     
    private int[] array;
    private int[] tempMergArr;
    private int length;
 
    public static void main(String a[]){
     
        int size = 1000;
        int max = 32000; 
        //int loop = 0; 

        Random generator = new Random();
        
        MergeSort mms = new MergeSort();
        
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
                mms.sort(input);
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
     
    public void sort(int inputArr[]) {
        this.array = inputArr;
        this.length = inputArr.length;
        this.tempMergArr = new int[length];
        doMergeSort(0, length - 1);
    }
 
    private void doMergeSort(int lowerIndex, int higherIndex) {
         
        if (lowerIndex < higherIndex) {
            int middle = lowerIndex + (higherIndex - lowerIndex) / 2;
            // Below step sorts the left side of the array
            doMergeSort(lowerIndex, middle);
            // Below step sorts the right side of the array
            doMergeSort(middle + 1, higherIndex);
            // Now merge both sides
            mergeParts(lowerIndex, middle, higherIndex);
        }
    }
 
    private void mergeParts(int lowerIndex, int middle, int higherIndex) {
 
        for (int i = lowerIndex; i <= higherIndex; i++) {
            tempMergArr[i] = array[i];
        }
        int i = lowerIndex;
        int j = middle + 1;
        int k = lowerIndex;
        while (i <= middle && j <= higherIndex) {
            if (tempMergArr[i] <= tempMergArr[j]) {
                array[k] = tempMergArr[i];
                i++;
            } else {
                array[k] = tempMergArr[j];
                j++;
            }
            k++;
        }
        while (i <= middle) {
            array[k] = tempMergArr[i];
            k++;
            i++;
        }
 
    }
}

    
