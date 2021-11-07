package programmers;

class Solution {
    static int ans = 0;
    static boolean[] visited;
    
    public int solution(int k, int[][] dungeons) {
        visited = new boolean[dungeons.length];
        
        DFS(0, dungeons, k);
        
        return ans;
    }
    static void DFS(int cnt, int[][] dungeons, int k){
        if(ans < cnt) ans = cnt;
        
        
        
        for(int i = 0; i < dungeons.length; i++){
            if(!visited[i] && dungeons[i][0] <= k){
                visited[i] = true;
                DFS(cnt+1, dungeons, k-dungeons[i][1]);
                visited[i] = false;
            }    
        }
    }
}