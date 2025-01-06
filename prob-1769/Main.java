public class Main {
    public static void main(String[] args) {
        Solution solution = new Solution();
        String boxes = "110";
        int[] ans = solution.minOperations(boxes);
        for (int i : ans) {
            System.out.print(i + " ");
        }
    }
}