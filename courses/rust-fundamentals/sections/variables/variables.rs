fn main(){
  let my_variable_name: u32 = 0;
  println!("{}", my_variable_name);

  // inferred variables based on the default value
  let my_inferred_variable = 0;
  println!("{}", my_inferred_variable);

  let warning_variable = 0;

  // no warning on unused variable with _
  let _warning_variable_2 = 0;
}
