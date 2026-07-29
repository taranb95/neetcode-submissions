class Solution {
    public boolean isAnagram(String s, String t) {
       
       char[] string1 = s.toCharArray();
       char[] string2 = t.toCharArray();
       Arrays.sort(string1);
       Arrays.sort(string2);
       String st1 = new String(string1);
       String st2 = new String(string2);
       return st1.equals(st2);
    }
}
