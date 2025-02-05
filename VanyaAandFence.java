import java.util.Scanner;

public class VanyaAandFence {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        // Read the number of friends and the height of the fence
        int n = scanner.nextInt();
        int h = scanner.nextInt();
        
        int[] heights = new int[n];
        for (int i = 0; i < n; i++) {
            heights[i] = scanner.nextInt();
        }
        
        int width = 0;
        for (int i = 0; i < n; i++) {
            if (heights[i] > h) {
                width += 2;  // Friend bends down
            } else {
                width += 1;  // Friend walks as usual
            }
        }
        
        System.out.println(width);
        
        scanner.close();
    }
}
