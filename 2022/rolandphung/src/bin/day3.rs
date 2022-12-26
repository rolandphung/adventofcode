use adventofcode2022::read_input_file;
use std::collections::HashSet;

fn item_to_priority(item: char) -> u32 {
    let base_upper_a: u32 = u32::from('A');
    let base_lower_a: u32 = u32::from('a');
    let mut priority = u32::from(item);
    if item.is_uppercase() {
        priority = priority - base_upper_a + 27;
    } else {
        priority = priority - base_lower_a + 1;
    }
    return priority;
}

fn sack_to_set(sack: &str) -> HashSet::<char> {
    let mut set = HashSet::<char>::new();
    for item in sack.chars() {
        set.insert(item);
    }
    return set;
}

fn part1() {
    let mut total_priority = 0;
    for line in read_input_file().unwrap() {
        let line_string = line.unwrap();
        let sack1 = &line_string[..line_string.len()/2];
        let sack2 = &line_string[line_string.len()/2..];
        let unique_set = sack_to_set(sack1);

        let mut found = '\0';
        for item in sack2.chars() {
            if unique_set.contains(&item) {
                found = item;
                break;
            }
        }

        total_priority += item_to_priority(found);
    }
    println!("Total Priority: {total_priority}");
}

fn part2() {
    let mut total_priority = 0;
    let mut lines = read_input_file().unwrap().peekable();
    while let Some(_) = lines.peek() {
        let sack1 = sack_to_set(&lines.next().unwrap().unwrap());
        let sack2 = sack_to_set(&lines.next().unwrap().unwrap());
        let sack3 = sack_to_set(&lines.next().unwrap().unwrap());

        let intersect: HashSet::<char> = sack1.intersection(&sack2).copied().collect();
        let badge = intersect.intersection(&sack3).next().unwrap();

        total_priority += item_to_priority(badge.clone());
    }

    println!("Total Badge Priority: {total_priority}");
}

fn main() {
    part1();
    part2();
}
