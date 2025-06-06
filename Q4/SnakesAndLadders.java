/*

 ***Caution:
 ***The test case files can be accessed only by giving the full path link


 Q4_TC1.txt ---> A standard 10x10 board with a few valid snakes and ladders.
 Q4_TC2.txt ---> Board dimension is less than 8, which should be invalid.
 Q4_TC3.txt ---> A ladder directly from the start (1) to the end (dim*dim) is present, which should be invalid.
 Q4_TC4.txt ---> A ladder that goes down instead of up, which should be invalid.
 Q4_TC5.txt ---> A ladder whose start and end positions are the same, creating a loop, which should be invalid.
 Q4_TC6.txt ---> Ladders interconnected such that they create a direct path from START to FINISH, which should be invalid.
 Q4_TC7.txt ---> A snake head or ladder end occupies the same position multiple times, which should be invalid.
 Q4_TC8.txt ---> A snake whose head is below its tail, implying it is going upwards, which should be invalid.
 Q4_TC9.txt ---> A snake whose head and tail positions are the same, creating a loop, which should be invalid.
 Q4_TC10.txt --> A snake and ladder combination that forms a loop, which should be invalid.
 Q4_TC11.txt --> The bottom of a ladder and the head of a snake are in the same position, which should be invalid.
 Q4_TC12.txt --> There are six consecutive positions occupied by snake heads, which should be invalid.
 Q4_TC13.txt --> No viable path exists from the start to the end due to the placement of snakes.
 Q4_TC14.txt --> A large board with multiple valid snakes and ladders ensuring a complex, yet viable path.
 */


// Snakes and Ladders Board Validator Program
// This program validates a given Snakes and Ladders board based on specific rules and constraints.


import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.*;


//Method for Snakes and Ladders board validation
public class SnakesAndLadders 
{

    // Method to check if the board configuration is valid
    public static boolean validBoard(int dim, List<int[]> snakes, List<int[]> ladders) 
    {
        // Checking if the size of the board is above the minimum constraint of 8x8
        if (dim < 8) {
            System.out.println("Size is less than 8");  // Informing about board size violation
            return false;  // Returning false due to invalid board size
        }

        List<int[]> loopSnakes = new ArrayList<>();  // List to check for snake-ladder loops
        int[] board = new int[dim * dim + 1];  // Array representing the board

        // Iterate through each ladder
        for (int[] ladder : ladders) {
            // Check if there's a direct ladder from the start (1) to the finish (dim * dim)
            if (ladder[0] == 1 && ladder[1] == (dim * dim)) {
                System.out.println("Direct ladder from START to FINISH is not allowed!!");   
                return false;   
            }
            // Check if a ladder is descending instead of ascending
            if (ladder[0] > ladder[1]) {
                System.out.println("A ladder should always be ascending!!");   
                return false;   
            }
            // Check if a ladder forms a loop by connecting the same start and end points
            if (ladder[0] == ladder[1]) {
                System.out.println("Ladder itself is forming a loop!!");   
                return false;   
            }
            // Check if ladders create a direct path from start to end using multiple ladders
            if (ladder[1] == dim * dim) {
                if (!checkStart(ladder, ladders, dim)) {  // Call helper method to verify configuration
                    return false;  // Return false if invalid configuration detected
                }
            }
            // Add ladder end-points to the loop check list to identify snake-ladder loops
            loopSnakes.add(new int[] { ladder[1], ladder[0] });  
            board[ladder[1]] = 2;  // Marking the ladder end on the board
        }

        // Iterate through each snake
        for (int[] snake : snakes) {
            // Check if multiple ladders or snakes end at the same board position
            if (board[snake[1]] == 2) {
                System.out.println("More than one terminal point in a single position!");   
                return false;   
            }
            // Mark the snake's head on the board
            board[snake[0]] = 1;
            // Check if a snake is ascending (it should be descending)
            if (snake[0] < snake[1]) {
                System.out.println("A snake should always be descending!!");   
                return false;   
            }
            // Check if a snake forms a loop by connecting the same head and tail points
            if (snake[0] == snake[1]) {
                System.out.println("Snake itself is forming a loop!!");   
                return false;   
            }
            // Check if there's a loop formed by a combination of snakes and ladders
            if (containsArray(loopSnakes, snake)) {
                System.out.println("A pair of snake and ladder is forming a LOOP!!");   
                return false;   
            }
            // Check if a ladder's bottom and a snake's head are at the same position
            for (int[] ladder : ladders) {
                if (snake[0] == ladder[0]) {
                    System.out.println("Both ladder's bottom and snake's head can't be in the same position!");   
                    return false;   
                }
            }
        }

        // Convert the board array to a string and check for six consecutive snake heads
        String snakePosStr = Arrays.toString(board).replaceAll("[\\[\\]\\s,]", "");
        if (snakePosStr.contains("111111")) {
            System.out.println("6 consecutive snakes are present so can't reach final position!");   
            return false;   
        }

        // Re-initialize the board to create an array representation of the board
        board = new int[dim * dim + 1];
        // Mark the positions of ladders on the board
        for (int[] ladder : ladders) {
            board[ladder[0]] = ladder[1];
        }
        // Mark the positions of snakes on the board
        for (int[] snake : snakes) {
            board[snake[0]] = snake[1];
        }

        // Use BFS to search for at least one viable path from start to finish
        if (!pathSearch(board, dim)) {
            System.out.println("No valid path found");   
            return false;  // Return false if no valid path is found
        }

        // If all cases are satisfied, return true indicating a valid board
        System.out.println("Board is valid and path found");
        return true;
    }

    // Helper method to check for interconnected ladders from START to FINISH
    private static boolean checkStart(int[] ladder, List<int[]> ladders, int dim) {
        // If ladder starts at 1, it's an interconnected ladder from START
        if (ladder[0] == 1) {
            System.out.println("Interconnected ladders leading straight START to FINISH is not allowed!!");   
            return false;   
        }
        // Recursively check for interconnected ladders
        for (int[] i : ladders) {
            if (i[1] == ladder[0]) {
                return checkStart(i, ladders, dim);  // Recursive call to check ladders
            }
        }
        return true;  // Return true if no issue found
    }

    // Helper method to check if a list contains a specific array
    private static boolean containsArray(List<int[]> list, int[] array) {
        for (int[] item : list) {
            if (Arrays.equals(item, array)) {  // Compare arrays
                return true;  // Return true if a match is found
            }
        }
        return false;  
    }

    // Method to perform BFS and check if there's a valid path from START to FINISH
    private static boolean pathSearch(int[] board, int dim) {
        Queue<Integer> queue = new LinkedList<>();  // Queue for BFS
        Set<Integer> visited = new HashSet<>();  // Set to track visited positions
        queue.offer(1);  // Start BFS from position 1

        while (!queue.isEmpty()) {
            int curr = queue.poll();  // Get the current position
            // Check if we have reached the FINISH
            if (curr == dim * dim) {
                return true;  // Return true if FINISH is reached
            }

            // Try moving 1 to 6 steps ahead
            for (int i = 1; i <= 6; i++) {
                int nextPos = curr + i;  // Calculate the next position
                if (nextPos > dim * dim) {
                    break;  // Stop if next position exceeds the board size
                }
                // Check if next position leads to a snake or ladder
                if (board[nextPos] != 0) {
                    nextPos = board[nextPos];  // Move to the new position
                }
                // Check if the position is visited
                if (!visited.contains(nextPos)) {
                    visited.add(nextPos);  // Mark position as visited
                    queue.offer(nextPos);  // Add position to the queue
                }
            }
        }
        return false; 
    }

    // Main method to read input from a file and validate the board
    public static void main(String[] args) {
        try (BufferedReader br = new BufferedReader(new FileReader("E:\\OneDrive - Amrita Vishwa Vidyapeetham\\B.Tech\\SEMESTER-5\\DAA Assignment\\Q4\\Q4_TC14.txt"))) {
            int dim = Integer.parseInt(br.readLine().trim());  // Read board dimension
            int noSnakes = Integer.parseInt(br.readLine().trim());  // Read number of snakes
            int noLadders = Integer.parseInt(br.readLine().trim());  // Read number of ladders

            List<int[]> snakes = new ArrayList<>();  // List to store snake positions
            for (int i = 0; i < noSnakes; i++) {
                String[] parts = br.readLine().trim().split(" ");  // Read snake positions
                snakes.add(new int[] { Integer.parseInt(parts[0]), Integer.parseInt(parts[1]) });  // Add snake to list
            }

            List<int[]> ladders = new ArrayList<>();  // List to store ladder positions
            for (int i = 0; i < noLadders; i++) {
                String[] parts = br.readLine().trim().split(" ");  // Read ladder positions
                ladders.add(new int[] { Integer.parseInt(parts[0]), Integer.parseInt(parts[1]) });  // Add ladder to list
            }

            boolean answer = validBoard(dim, snakes, ladders);  // Validate the board
            System.out.println(answer);  
        } catch (IOException e) {
            e.printStackTrace();  
        }
    }
}
