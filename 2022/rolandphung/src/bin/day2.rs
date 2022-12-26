use adventofcode2022::read_input_file;
use std::collections::HashMap;

fn part1() {
    const ROCK_OTHER: char = 'A';
    const PAPER_OTHER: char = 'B';
    const SCISSOR_OTHER: char = 'C';
    const ROCK: char = 'X';
    const PAPER: char = 'Y';
    const SCISSOR: char = 'Z';

    let score_map: HashMap::<char, u32> = HashMap::from([
        (ROCK, 1),
        (PAPER, 2),
        (SCISSOR, 3),
    ]);

    let draw_map: HashMap::<char, char> = HashMap::from([
        (ROCK, ROCK_OTHER),
        (PAPER, PAPER_OTHER),
        (SCISSOR, SCISSOR_OTHER),
    ]);

    let win_map: HashMap::<char, char> = HashMap::from([
        (ROCK, SCISSOR_OTHER),
        (PAPER, ROCK_OTHER),
        (SCISSOR, PAPER_OTHER),
    ]);

    let mut total_score = 0;
    let lines = read_input_file().unwrap();

    for line in lines {
        let line_string = line.unwrap();
        let mut chars = line_string.chars();
        let other_play = chars.next().unwrap();
        let my_play = chars.nth(1).unwrap();

        let mut score = score_map[&my_play];
        if draw_map[&my_play] == other_play {
            score += 3;
        } else if win_map[&my_play] == other_play {
            score += 6;
        }

        total_score += score;
    }

    println!("Total Score: {}", total_score);
}

fn part2() {
    const ROCK: char = 'A';
    const PAPER: char = 'B';
    const SCISSOR: char = 'C';
    const LOSE: char = 'X';
    const DRAW: char = 'Y';
    const WIN: char = 'Z';

    let score_map: HashMap::<char, u32> = HashMap::from([
        (LOSE, 0),
        (DRAW, 3),
        (WIN, 6),
    ]);

    let lose_map: HashMap::<char, u32> = HashMap::from([
        (ROCK, 3), // SCISSORS
        (PAPER, 1), // ROCK
        (SCISSOR, 2), // PAPER
    ]);

    let draw_map: HashMap::<char, u32> = HashMap::from([
        (ROCK, 1),
        (PAPER, 2),
        (SCISSOR, 3),
    ]);

    let win_map: HashMap::<char, u32> = HashMap::from([
        (ROCK, 2), // PAPER
        (PAPER, 3), // SCISSOR
        (SCISSOR, 1), // ROCK
    ]);

    let mut total_score = 0;
    let lines = read_input_file().unwrap();

    for line in lines {
        let line_string = line.unwrap();
        let mut chars = line_string.chars();
        let other_play = chars.next().unwrap();
        let my_play = chars.nth(1).unwrap();

        let mut score = score_map[&my_play];

        if my_play == LOSE {
            score += lose_map[&other_play];
        } else if my_play == DRAW {
            score += draw_map[&other_play];
        } else if my_play == WIN {
            score += win_map[&other_play];
        }

        total_score += score;
    }

    println!("Total Score: {}", total_score);
}

fn main() {
    part1();
    part2();
}
