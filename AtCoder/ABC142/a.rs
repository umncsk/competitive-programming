fn main() {
    let _stdin: String = {
        let mut s = String::new();
        std::io::stdin().read_line(&mut s).unwrap();
        s.trim_right().to_owned()
    };
    let n: f32 = _stdin.parse().unwrap();
    if n % 2. == 0.0 {
        println!("{}", 1. - (n / 2. / n));
    } else {
        println!("{}", 1. - ((n - 1.) / 2. / n));
    }
}
