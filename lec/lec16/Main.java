import java.util.*;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) {
        String a = "praxis forever";
        String b = "a prefix rover";

        String c = "something";
        String d = "spam test";

        System.out.println(isAnagram(a, b));
        System.out.println(isAnagram(c, d));
    }

    public static boolean isAnagram(String s1, String s2) {
        char arr1[] = Arrays.toCharArray(s1);
        char arr2[] = Arrays.toCharArray(s2);

        return Arrays.sort(arr1.toLowerCase().replace(" ", "")).equals(Arrays.sort(arr2.toLowerCase().replace(" ", "")));
    }
}