#[allow(unused_variables)]

fn main(){
  let duck :&str = "Duck";
  let airlines :&str = "Airlines";

  let airline_name :String = format!("{} {}", duck, airlines);
  print!("{}\n", airline_name);

  let mut slogan :String = String::new();
  slogan.push_str("we hit the ground");
  // Chart literal, single quotes
  slogan.push(' ');
  slogan = slogan + "every time";

  print!("{}\n", slogan);
}
