///////////////////// Success //////////////////////////

// Don't place your source in a package
import java.util.*;

// Please name your class Main


class disjointSets{
    int[] parent,rank;
    int n; // number of elements

    int findParent(int x){
        int found;
        if (parent[x]== x){
            found = x; // Student his own district
        }
        else{
            found = findParent(parent[x]); // find the district of the district of the guy he's pointing to
        }
        return found;
    }

    public disjointSets(int size){
        parent = new int[size];
        rank = new int[size];
        this.n = size; 
        makeSet(size);
    }

    void makeSet (int size){
        for (int x = 0; x < size ; x++){
            parent[x] = x; // each student is in his own district
        }
    }
    

    // union will give 0 if this forms a loop
    // 1 if there is no loop
    int union (int a, int b){
        int repA, repB;
        repA = findParent(a);
        repB = findParent(b);

        if (repA == repB){
            // no need to do anything, they're already marked under same district
            
            return 1;
        }
        else{
            if (rank[repA]>rank[repB]){
                // repA is represents a larger district
                parent[repB] = repA;
                
            } 
            else if (rank[repA]<rank[repB]){
                // repB represents the larger district
                parent[repA] = repB;
                // here rank doesn't change, think like a larger set of students have space to fit more
            }
            else{
                // both districts are equally large
                // chose repA's district
                parent[repB] = repA;

                rank [repA] ++; // district size increases
            }
            return 0;
        }
    }

}

class checkloop {
    public static int check(int n, int m, int [][] edges){
        disjointSets tunnels = new disjointSets(n);
        int status = 0;
        for (int[] road : edges){
            // union each road
            status = tunnels.union(road[0], road[1]);
            if (status == 1){
                break;
            }
        }
        return status;
    }
}

class Main {
	public static void main (String[] args) throws java.lang.Exception {
        Scanner in = new Scanner(System.in);
        int times = in.nextInt();
        int[] stats = new int[times];
        int n,m;
        int a,b;
        for (int z = 0 ; z< times ; z++){
            n = in.nextInt();
            m = in.nextInt();
            int[][] edges = new int[m][2];
            for (int y = 0 ; y < m ; y++){
                a = in.nextInt();
                b = in.nextInt();
                edges[y][0] = a;
                edges[y][1] = b;
            }

            stats[z] = checkloop.check(n, m, edges);
           
        }
        in.close();
        for (int z = 0 ; z < times ; z++){
            System.out.println(stats[z]);
        }
    }
}