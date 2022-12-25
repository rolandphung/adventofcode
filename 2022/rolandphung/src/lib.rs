use std::env;
use std::fs::File;
use std::io::BufReader;
use std::io::BufRead;
use std::io::Result;
use std::io::Lines;

pub fn read_input_file() -> Result<Lines<BufReader<File>>> {
    let args: Vec<String> = env::args().collect();
    let file = File::open(&args[1])?;
    return Ok(BufReader::new(file).lines());
}
