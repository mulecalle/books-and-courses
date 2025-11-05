#[allow(unused_variables)]

fn main(){

  // [f32;2] -> f32 data type; 2 number of elements
  // arrays needs to be initialized
  let my_array: [f32;2] = [41.4 , -81.0 ];

  let my_tupple: (&str, f64, f64) = ("KCLE", 41.4 , -81.1);
  println!("Location name: {}, latitude {}, longitude {}\n", my_tupple.0, my_tupple.1, my_tupple.2);

  // destructoring
  let (name, latitude, longitude) = my_tupple;
  println!("Location name: {}, latitude {}, longitude {}", name, latitude, longitude);
}
