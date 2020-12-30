fn main() {
    println!("Hello, world!");
}
fn is_possible(y: i32, x: i32, n: i32, grid: &Vec<Vec<i32>>) -> bool {
    let mut i = 0 as usize;
    let new_y = y as usize;
    let new_x = x as usize;
    while i < 9 {
        if grid[new_y][i] == n {
            return false
        }
        i += 1
    }
    i = 0 as usize;
    while i < 9 {
        if grid[i][new_x] == n {
            return false
        }
        i += 1
    }
    let alpha = ((y/3) *3) as usize;
    let beta = ((x/3) * 3) as usize;
    i = 0;
    let mut j = 0 as usize;
    while i < 3 {
        while j < 3 {
            if grid[alpha + i][beta + j] == n {
                return false
            }
            j += 1
        }
        i += 1
    }
    return true
}

fn solve(grid: &mut Vec<Vec<i32>>) {
    let mut x = 0 as usize;
    let mut y = 0 as usize;
    let mut int_x;
    let mut int_y;
    let mut n = 1;
    while y < 9 {
        while x < 9 {
            if grid[y][x] == 0 {
                while n < 10 {
                    int_x = x as i32;
                    int_y = y as i32;
                    if is_possible(int_y, int_x, n, grid) {
                        grid[y][x] = n;
                        solve(grid);
                        grid[y][x] = 0;
                    }
                    n += 1
                }
                return
            }
            x += 1
        }
        y += 1
    }
}