import java.util.Scanner;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        int T = sc.nextInt();  // Number of test cases
        for (int t = 1; t <= T; t++) {
            int N = sc.nextInt();
            int[][] matrix = new int[N][N];
            
            // Input matrix
            for (int i = 0; i < N; i++) {
                for (int j = 0; j < N; j++) {
                    matrix[i][j] = sc.nextInt();
                }
            }
            
            // Rotate 90 degrees
            int[][] rotate90 = new int[N][N];
            for (int i = 0; i < N; i++) {
                for (int j = 0; j < N; j++) {
                    rotate90[i][j] = matrix[N - j - 1][i];
                }
            }
            
            // Rotate 180 degrees
            int[][] rotate180 = new int[N][N];
            for (int i = 0; i < N; i++) {
                for (int j = 0; j < N; j++) {
                    rotate180[i][j] = matrix[N - i - 1][N - j - 1];
                }
            }
            
            // Rotate 270 degrees
            int[][] rotate270 = new int[N][N];
            for (int i = 0; i < N; i++) {
                for (int j = 0; j < N; j++) {
                    rotate270[i][j] = matrix[j][N - i - 1];
                }
            }
            
            // Output result
            System.out.println("#" + t);
            for (int i = 0; i < N; i++) {
                for (int j = 0; j < N; j++) {
                    System.out.print(rotate90[i][j]);
                }
                System.out.print(" ");
                for (int j = 0; j < N; j++) {
                    System.out.print(rotate180[i][j]);
                }
                System.out.print(" ");
                for (int j = 0; j < N; j++) {
                    System.out.print(rotate270[i][j]);
                }
                System.out.println();
            }
        }
        sc.close();
    }
}
