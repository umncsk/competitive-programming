fn read<T: std::str::FromStr>() -> T {
    let mut s = String::new();
    std::io::stdin().read_line(&mut s).ok();
    s.trim().parse().ok().unwrap()
}

fn read_vec<T: std::str::FromStr>() -> Vec<T> {
    let mut s = String::new();
    std::io::stdin().read_line(&mut s).ok();
    s.trim().split_whitespace()
        .map(|e| e.parse().ok().unwrap()).collect()
}

fn main() {
    let n: i32 = read();
    let mut L: Vec<i32> = read_vec();
    L.sort();

    let mut ans = 0;
    for i in 0..(n - 2) {
        let mut k = i + 2;

        for j in (i + 1)..(n - 1) {
            let _i = i as usize;
            let _j = j as usize;

            let l = L[_i] + L[_j];

            loop {
                if k == n { break; }
                k += 1;
            }

            k -= 1;
            ans += k - j;
        }
    }

    println!("{:?}", ans);
}
