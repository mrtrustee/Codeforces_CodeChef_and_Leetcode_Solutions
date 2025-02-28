import java.util.Scanner;

public class Cd1A {
    public static void main(String args){
        Scanner read = new Scanner(System.in);
        long a= read.nextInt();
        long n = read.nextInt();
        long m = read.nextInt();
        long countn = n/a;
        long countm = m/a;

        if(n%a != 0){
            countn++;
        }
        if(m%a != 0){
            countm++;
        }
        System.out.println(countm*countn);
        }
    }