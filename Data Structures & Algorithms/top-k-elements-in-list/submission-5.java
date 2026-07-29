class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer,Integer> result = new HashMap<Integer,Integer>();
        ArrayList<Integer> numbers = new ArrayList<>();
        for(int i=0;i<nums.length;i++){
            if(result.containsKey(nums[i])){
                result.put(nums[i],result.get(nums[i]) + 1);
            }
            else{
                result.put(nums[i],1);
            }
        }
        Map<Integer, Integer> sortedMap = result.entrySet().stream()
                .sorted(Map.Entry.comparingByValue(Comparator.reverseOrder()))
                .collect(Collectors.toMap(
                        Map.Entry::getKey, 
                        Map.Entry::getValue, 
                        (oldValue, newValue) -> oldValue, 
                        LinkedHashMap::new
                ));
        
        System.out.println(sortedMap);
        for (Map.Entry<Integer, Integer> entry : sortedMap.entrySet()) {
               numbers.add(entry.getKey());
        }
        return numbers.stream().limit(k).mapToInt(Integer::intValue).toArray();
    }
}
