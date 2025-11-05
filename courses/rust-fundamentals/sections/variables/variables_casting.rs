fn main(){
  let float_thirty_two: f32 = 17.2;
  let unsigned_eight: u8 = 5;

  // error to determinate the new type
  // let result = float_thirty_two / unsigned_eight;

  // cast variable to type a to b "as"
  let cast_unsigned_eight: f32 = unsigned_eight as f32;

  let _result = float_thirty_two / cast_unsigned_eight;
}
