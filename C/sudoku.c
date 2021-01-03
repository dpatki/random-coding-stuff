#include <stdio.h>
#include <stdbool.h>
int main() {
    printf("hi \n");
}

bool isPossible(int y, int x, int n,int **grid) {
    for(int i = 0; i < 9; i++) {
        if (grid[y][i] == n) {
            return false;
        }
        if (grid[i][x] == n) {
            return false;
        }
    }
    int alpha = (y/3) *3;
    int beta = (x/3) *3;
    for(int i = 0; i < 2; i++) {
        for(int j = 0; j < 2; j++) {
            if (grid[alpha+i][beta+j] == n){
                return false;
            }
        }
    }

    return true;
}

void solve(int **grid) {
    for(int y; y < 9; y++) {
        for(int x; x < 9; x++){
            if (grid[y][x] == 0) {
                for(int n = 1; n < 10; n++) {
                    if (isPossible(y,x,n,grid)) {
                        grid[y][x] = n;
                        solve(grid);
                        grid[y][x] = 0;
                    }
                }
                return;
            }
        }
    }
    printf("sup\n");
}