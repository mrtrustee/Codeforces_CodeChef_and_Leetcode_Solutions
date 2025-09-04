/* ID: Isaiah Fakorede [mrtrustee]
LANG: JAVA
TASK: test
 */
import java.io.*;
import java.util.*;
public class Test {
    public static void main(String[] args) throws IOException{
        BufferedReader f = new BufferedReader(new FileReader("Test.java"));
        PrintWriter out = new PrintWriter(new BufferedWriter(new FileWriter("Test.java")));
        StringTokenizer st = new StringTokenizer(f.readLine());
        int i = Integer.parseInt(st.nextToken());
        int j = Integer.parseInt(st.nextToken());
        out.println( i+j);
        out.close();
    }

}
