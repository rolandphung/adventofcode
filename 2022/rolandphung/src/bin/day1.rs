use adventofcode2022::read_input_file;

fn part1() {
    let lines = read_input_file().unwrap();
    let mut largest: u32 = 0;
    let mut sum: u32 = 0;
    for line in lines {
        let num_str = line.unwrap();
        if num_str == "" {
            if sum > largest {
                largest = sum;
            }
            sum = 0;
        } else {
            sum += num_str.parse::<u32>().unwrap();
        }
    }

    println!("Largest: {}", largest);
}

fn part2() {
    let lines = read_input_file().unwrap();
    let mut elves: Vec::<u32> = Vec::new();
    let mut sum: u32 = 0;
    for line in lines {
        let num_str = line.unwrap();
        if num_str == "" {
            elves.push(sum);
            sum = 0;
        } else {
            sum += num_str.parse::<u32>().unwrap();
        }
    }
    elves.sort();
    let answer = elves.pop().unwrap() + elves.pop().unwrap() + elves.pop().unwrap();
    println!("Top 3: {}", answer);
}

fn main() {
    part1();
    part2();
}
