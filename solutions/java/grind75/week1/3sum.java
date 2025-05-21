import java.util.*;

public class 3sum {
    public static List<List<Integer>> threeSum(int[] nums) {
        List<List<Integer>> res = new ArrayList<>();
        Arrays.sort(nums);
        
        // Replace this placeholder return statement with your code
        
        for (int i = 0; i < nums.length; i++) {
            // Skip duplicates
            if (i > 0 && nums[i] == nums[i - 1]) continue;
            
            // Initialize two pointers
            int j = i + 1;
            int k = nums.length - 1;
            
            // Move till they converge
            while (j < k) {
                int sum = nums[i] + nums[j] + nums[k];
                
                if (sum > 0) {
                    k--;
                }
                else if (sum < 0) {
                    j++;
                }
                else {
                    res.add(Arrays.asList(nums[i], nums[j], nums[k]));
                    j++;
                    k--;
                    
                    // Skip duplicates for other 2 pointers as well if result found
                    while (j < k && nums[j] == nums[j - 1]) j++;
                    while (j < k && nums[k] == nums[k + 1]) k--;
                }
            }
        }
        return res;
    }
}