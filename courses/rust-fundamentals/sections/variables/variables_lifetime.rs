fn main(){
  let scope_test = "outer scope";
  println!("{}", scope_test);

  // { ... } creates a new scope
  {
    // "shadowing" the variable scope_test to different scope
    let scope_test = "inner scope";
    println!("{}", scope_test);
  }

  println!("{}", scope_test);
}
