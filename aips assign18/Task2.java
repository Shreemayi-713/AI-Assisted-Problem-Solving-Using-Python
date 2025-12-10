/**
 * Task 2: Convert Conditional Statements (Java → Python)
 * This class contains a Java method that checks if a number is positive, negative, or zero.
 */

public class Task2 {
    
    /**
     * Check if a number is positive, negative, or zero.
     * 
     * @param num The number to check
     * @return A message indicating whether the number is positive, negative, or zero
     */
    public static String checkNumber(int num) {
        if (num > 0) {
            return "The number is positive";
        } else if (num < 0) {
            return "The number is negative";
        } else {
            return "The number is zero";
        }
    }
    
    /**
     * Main method to call the function with different inputs and display results.
     */
    public static void main(String[] args) {
        System.out.println("Input: -5 → Output: " + checkNumber(-5));
        System.out.println("Input: 0 → Output: " + checkNumber(0));
        System.out.println("Input: 7 → Output: " + checkNumber(7));
    }
}
