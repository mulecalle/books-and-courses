#[allow(unused_variables)]

fn main(){

  // string slice -> &str
  let person_name_slice :&str = "Sebastian Calle";

  // String
  let person_name_string :String = "Sebastian Calle".to_string();
  let person_name_string = String::from("Sebastian Calle");

  // string slice to String
  let person_name_string :String = person_name_slice.to_string();
 
  // String to string slice
  let person_name_string_2 :&str = &person_name_string;

  // or
  let person_name_string_3 :&str = person_name_string.as_str();


  println!("variable: {}", person_name_string_2);
}
