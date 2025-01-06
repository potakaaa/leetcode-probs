public class Solution {
    public int[] minOperations(String boxes) {
        int[] ans = new int[boxes.length()];
        int moves = 0;
        int i = 0;
        int mid = boxes.length() / 2;
        int left_ptr = mid - 1;
        int right_ptr = mid + 1;

        while (left_ptr > 0 && right_ptr < boxes.length()) {
            moves = 0;
            if (boxes.charAt(left_ptr) == '1') {
                moves += Math.abs(mid - left_ptr);
            }
            if (boxes.charAt(right_ptr) == '1') {
                moves += Math.abs(mid - right_ptr);
            }
            left_ptr -= 1;
            right_ptr += 1;
            ans[i] = moves;
            i++;
        }
        return ans;
    }
}
