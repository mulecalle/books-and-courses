fn main(){
  // by default variables in rush are inmmutable (cannot be changed)

  // "mut" allow you to change the value of the variable after the initialization
  let mut changeable_variable = 500;
  println!("{}", changeable_variable);
  changeable_variable = 501;
  println!("{}", changeable_variable);

  // error 
  // cannot assign twice to immutable variable
  let changeable_variable_2 = 500;
  println!("{}", changeable_variable_2);
  changeable_variable_2 = 501;
  println!("{}", changeable_variable_2);
}
