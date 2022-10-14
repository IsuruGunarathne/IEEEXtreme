import java.util.*;

public class IX_11_Fibonacci {
    public static void main(String[] args) {

        Scanner in = new Scanner(System.in);
        int times = in.nextInt();
        int[] inNums = new int[times];
        for (int x = 0 ; x< times; x++){
            inNums[x] = in.nextInt();
        }

        int[] fibModVals = new int[60];
        int a,b,c;
        a=0;
        b=1;
        fibModVals[0] = a;
        fibModVals[1] = b;
        for (int x = 2 ; x < 60 ; x++){   // joel's genius repetition pattern
            c = (a+b)%10;
            a = b;
            b = c;
            fibModVals[x] = c%10;
        }

        // now we have the numbers taken in
        for (int x = 0 ; x< times; x++){
            int outNum = fibMod(inNums[x],fibModVals);
            System.out.println(outNum);
        }

        in.close();
    }

    public static int fibMod(int n,int[] fibModVals){
        int nMod = (n+1)%60;
        int c = fibModVals[nMod];
        return c;
    }
}
