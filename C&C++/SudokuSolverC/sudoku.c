#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

bool isValidSudoku(int grid[][9]) {
    for(int x = 0; x < 9; x++) {
        int arr[9] = {0,0,0,0,0,0,0,0,0};
        int j = 0;
        for(int y = 0; y < 9; y++) {
            if (grid[y][x] == 0) {
                continue;
            }
            int i = 0;
            while (i < 9) {
                if (grid[y][x] == arr[i]) {
                    return false;
                }
                i++;
            }
            arr[j] = grid[y][x];
            j++;
        }
    }

    for(int y = 0; y < 9; y++) {
        int arr[9] = {0,0,0,0,0,0,0,0,0};
        int j = 0;
        for(int x = 0; x < 9; x++) {
            if (grid[y][x] == 0) {
                continue;
            }
            int i = 0;
            while (i < 9) {
                if (grid[y][x] == arr[i]) {
                    return false;
                }
                i++;
            }
            arr[j] = grid[y][x];
            j++;
        }
    }

    for(int alpha = 0; alpha < 3; alpha++) {
        for(int beta = 0; beta < 3; beta++) {
            int arr[9] = {0,0,0,0,0,0,0,0,0};
            int j = 0;
            int y = 3 * alpha;
            while (y < (3*alpha) + 3) {
                int x = 3*beta;
                while (x < (3*beta) + 3) {
                    if (grid[y][x] == 0) {
                        x++;
                        continue;
                    }
                    int i = 0;
                    while (i < 9) {
                        if (grid[y][x] == arr[i]) {
                            return false;
                        }
                        i++;
                    }
                    arr[j] = grid[y][x];
                    j++;

                    x++;
                }

                y++;
            }
        }
    }

    return true;
}

bool isPossible(int y, int x, int n,int grid[][9]) {
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

int checkChars (int **grid) {
    int dict[10] = {0,0,0,0,0,0,0,0,0,0};
    for (int y = 0; y < 9; y++) {
        for (int x = 0; x < 9; x++) {
            //whatever gonna hardcode this because anything other than 0 to 9 we return -1 anyway
            if (grid[y][x] == 0) {
                dict[0]++;
            } else if (grid[y][x] == 1) {
                dict[1]++;
            } else if (grid[y][x] == 2) {
                dict[2]++;
            } else if (grid[y][x] == 3) {
                dict[3]++;
            } else if (grid[y][x] == 4) {
                dict[4]++;
            } else if (grid[y][x] == 5) {
                dict[5]++;
            } else if (grid[y][x] == 6) {
                dict[6]++;
            } else if (grid[y][x] == 7) {
                dict[7]++;
            } else if (grid[y][x] == 8) {
                dict[8]++;
            } else if (grid[y][x] == 9) {
                dict[9]++;
            } else {
                return -1;
            }
        }
    }
    int sum = 0;
    for(int i = 0; i < 10; i++) {
        sum += dict[i];
    } 
    return sum;
}

int asciiToDig(int character) {
    /* hard code in digs from 0 to 9, just return 0 if its not a digit in that range*/
    if (character <= 48) {
        return 0;
    } else if (58 <= character) {
        return 0;
    } else {
        return (character - 48);
    }
}

void inputSudoku(int grid[][9]) {
    FILE *fptr = fopen("duplicate.txt", "r");
    if (fptr == NULL) {
        printf("Invalid Input File!");
        exit(1);
    }
    for(int y = 0; y < 9; y++) {
        int i = 0;
        for(int x = 0; x < 18; x++) {
            char c[2];
            fscanf(fptr, "%c", c);
            if (x % 2 == 0){
                int d = *c;
                //printf("%d ", d);
                int e = asciiToDig(d);
                //printf("%d ", e);
                grid[y][i] = e;
                //printf("%d ", grid[y][i]);
                i++;
            }
        }
        
        /*printf("\n");
        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 9; j++){
                printf("%d ", grid[i][j]);
        }
        printf("\n");
    }*/

    }
    fclose(fptr);
    
}

void outputSudoku(int grid[][9]) {
    FILE *fptr = fopen("output.txt", "a");
    if (fptr == NULL) {
        printf("Invalid Output File!");
        exit(1);
    }
    //printf("hello");
    fprintf(fptr, "Solution: \n");
    for (int x = 0; x < 9; x++) {
        for (int y = 0; y < 9; y++) {
            //printf("hello \n");
            fprintf(fptr, "%d ", grid[x][y]);
        }
        fprintf(fptr, " \n");
    }
    fclose(fptr);
}

void solve(int grid[][9]) {
    for(int y= 0 ; y < 9; y++) {
        for(int x =0; x < 9; x++){
            //printf("hasn't crashed here\n");
            if (grid[y][x] == 0) {
                for(int n = 1; n < 10; n++) {
                    if (isPossible(y,x,n,grid)) {
                        //printf("%d %d \n", y, x);
                        grid[y][x] = n;
                        //outputSudoku(grid);
                        solve(grid);
                        grid[y][x] = 0;
                    }
                }
                return;
            }
        }
    }
    printf("sup\n");
    outputSudoku(grid);


    //exit(0); //only one solution. Too bad!
}


int main() {
    FILE *fptr = fopen("output.txt", "a");
    fprintf(fptr, "Solution: \n");
    fclose(fptr);
    int potato[][9] = {{5,3,0,0,7,0,0,0,0},{6,0,0,1,9,5,0,0,0},{0,9,8,0,0,0,0,6,0},{8,0,0,0,6,0,0,0,3},{4,0,0,8,0,3,0,0,1},{7,0,0,0,2,0,0,0,6},{0,6,0,0,0,0,2,8,0},{0,0,0,4,1,9,0,0,5},{0,0,0,0,8,0,0,7,9}};
    int (*ptr)[]  = potato;
    //printf("hi \n");
    //inputSudoku(ptr);
    /*bool poss = isPossible(4,4,4,ptr);
    printf("%d ", poss);*/
    solve(ptr);
    /*
    for (int y = 0; y < 9; y++) {
        for(int x = 0; x < 9; x++) {
            printf("%d ", potato[y][x]);
        }
        printf("\n");
    }*/
    //outputSudoku(ptr);
}