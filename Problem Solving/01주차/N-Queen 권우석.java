package BOJ;

import java.io.*;
import java.util.*;

class Main{
	static int N;
	static int[][] visited;
	static int count;
	public static void main(String args[]) throws IOException{
		Scanner sc = new Scanner(System.in);
		N = sc.nextInt();
		visited = new int[N][N];
		
		
		
		
		nQueen(0);
		
		System.out.println(count);
		
	}
	static void nQueen(int col) {
		if(col == N) {
			count++;
			return;
		}
		
		for(int row = 0; row < N; row++) {
			if(visited[row][col] == 0) {
				checkRowCol(row, col);
				checkCross(row, col);
				
				nQueen(col+1);
				
				checkOffRowCol(row, col);
				checkOffCross(row, col);
			}
		}
	}
	
	static void checkRowCol(int row, int col) {
		for(int i = 0; i < N; i++) {
			visited[row][i]++;
		}
		for(int i = 0; i < N; i++) {
			visited[i][col]++;
		}
	}
	
	static void checkOffRowCol(int row, int col) {
		for(int i = 0; i < N; i++) {
			visited[row][i]--;
		}
		for(int i = 0; i < N; i++) {
			visited[i][col]--;
		}
	}
	
	static void checkCross(int row, int col) {
		visited[row][col]++;
		
		int idx = 1;
		for(int i = col+1; i < N; i++) {
			if(0 <=row-idx)visited[row-idx][i]++;
			if(row+idx < N)visited[row+idx][i]++;
			idx++;
		}
		
		idx = 1;
		for(int i = col-1; 0 <= i; i--) {
			if(0 <=row-idx)visited[row-idx][i]++;
			if(row+idx < N)visited[row+idx][i]++;
			idx++;
		}
		
		
		
		
	}
	
	static void checkOffCross(int row, int col) {
		visited[row][col]--;
		
		int idx = 1;
		for(int i = col+1; i < N; i++) {
			if(0 <=row-idx)visited[row-idx][i]--;
			if(row+idx < N)visited[row+idx][i]--;
			idx++;
		}
		
		idx = 1;
		for(int i = col-1; 0 <= i; i--) {
			if(0 <=row-idx)visited[row-idx][i]--;
			if(row+idx < N)visited[row+idx][i]--;
			idx++;
		}
	}
}
