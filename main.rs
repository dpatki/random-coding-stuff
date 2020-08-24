use std::io;

fn main() {
    println!("Welcome to stupid Clock program!");
    println!("It just tells you the angles of the hands of a clock.");
    println!("Enter a time!");

    let hour = get_input_int("Enter Number of hours");

    let minut = get_input_int("Enter Number of minutes");

    let sec = get_input_int("Enter number of seconds");
    
    println!("Entered: {} hours, {} minutes, and {} seconds.", hour, minut, sec);

    let angles = calc_angles(hour, minut, sec);
    let angle_diffs = angle_diffs(hour, minut, sec);
    println!("The absolute angle of the hour hand is: {} degrees.", angles.2);
    println!("The absolute angle of the minute hand is: {} degrees.", angles.1);
    println!("The absolute angle of the second hand is: {} degrees.", angles.0);
    println!("The difference between the minute and second hand is {} degrees.", angle_diffs.1);
    println!("The difference between the hour and second hand is {} degrees.", angle_diffs.0);
    println!("The difference between the minute and hour hand is {} degrees.", angle_diffs.2);
}

fn get_input_int(input_str: &str) -> u32 {

    println!("{}", input_str);
    let mut thingy = String::new();

    io::stdin().read_line(&mut thingy)
        .expect("Error reading input!");
    
    let thingy: u32 = match thingy.trim().parse() {
        Ok(num) => num,
        Err(_) => get_input_int("Error! Please enter a valid input!"),
    };

    return thingy
}

fn calc_angles(hr: u32, mn: u32, sec: u32) -> (f32, f32, f32) {
    let mut hr_norm = hr;
    let mut mn_norm = mn;
    if sec > 60 {
        mn_norm = mn_norm + 1;
        println!("Second overflow!")
    }

    if mn_norm > 60 {
        hr_norm = hr + 1;
        println!("Minute overflow!")
    }

    let hr_norm = (hr_norm % 12) as f32;
    let mn_norm = (mn_norm % 60) as f32;
    let sec_norm = sec % 60;

    let sec_angle = (sec_norm * 6) as f32;
    let min_angle = (mn_norm * 6.0 + sec_angle/60.0) as f32;
    let hr_angle = (hr_norm * 30.0 + min_angle/60.0) as f32;

    let tup = (sec_angle, min_angle, hr_angle);
    return tup;
}

fn angle_diffs(hr: u32, mn: u32, sec: u32) -> (f32, f32, f32) {
    let (sec_angle, min_angle, hour_angle) = calc_angles(hr, mn, sec);
    let sec_hr_diff = (sec_angle - hour_angle).abs();
    let sec_min_diff = (sec_angle - min_angle).abs();
    let min_hr_diff = (min_angle - hour_angle).abs();

    let tup = (sec_hr_diff, sec_min_diff, min_hr_diff);
    return tup;
}