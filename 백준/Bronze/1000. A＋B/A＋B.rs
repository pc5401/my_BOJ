use std::io;

fn main() {
    let mut input = String::new();

    io::stdin()
        .read_line(&mut input)
        .expect("Failed to read line");

    let nums: Vec<i32> = input
        .split_whitespace()
        .map(|s| s.trim().parse().expect("Failed to parse integer"))
        .collect();

    println!("{}", nums[0] + nums[1]);
}
