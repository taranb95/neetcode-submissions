class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer,Integer> res = new HashMap<Integer,Integer>();
        int result[] = new int[2];
        for(int i=0;i<nums.length;i++){
            res.put(nums[i],i);
        }
        for(int i=0;i<nums.length;i++){
            if(res.containsKey(target-nums[i]) && res.get(target-nums[i]) != i){
                result[0] = i;
                result[1] =  res.get(target-nums[i]);
                return result;
            }
        }
        return result;
        
    }
}
