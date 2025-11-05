package chapters

import (
	"fmt"
)

func Exercise1() {
	// sum is a function that takes a slice of numbers and adds them together.
	// What would its function signature look like in go?
	number := []int{1,2,3}

	innerFunction := func(numbers []int) int {
		total := 0

		for _,number := range numbers {
			total += number
		}

		return total
	}

	result := innerFunction(number)

	fmt.Println(result)
}

func Exercise2() {
	// Write a function that takes an integer and halves it and returns true if it was even
	// or false if it was odd. For example, half(1) should return (0, false) and
	// half(2) should return (1, true)

	half := func(value int) (int, bool){

		fmt.Printf("\nI received %d", value)

		if value%2 != 0 {
			return value/2, false
		}

		return value/2, true
	}


	halfValue, isItOrNot := half(1)

	fmt.Printf(", and I found that the half is: %d, which means that is even= %t", halfValue, isItOrNot)

	halfValue, isItOrNot = half(2)
	fmt.Printf(", and I found that the half is: %d, which means that is even= %t\n", halfValue, isItOrNot)
}

func Exercise3() {
	// Write a function with one variadic parameter that finds the greatest number in a
	// list of numbers.


	variadicFunction := func (numbers ...int) int{
		max := 0

		for _,number := range numbers {
			if number > max{
				max = number
			}
		}

		return max
	}

	tooManyIntegers := []int{100,2,3,4,5,6,7,8,9,11}

	maxNumber := variadicFunction(tooManyIntegers...)

	fmt.Printf("max number is: %d\n", maxNumber)
}

func Exercise4() {
	// Using makeEvenGenerator as an example, write a makeOddGenerator function
	// that generates odd numbers.

	generatedNumber := 0  //closure

	makeOddGenerator := func (){
		generatedNumber += 2
	}

	makeOddGenerator()
	fmt.Printf("odd number generated %d\n", generatedNumber)
	makeOddGenerator()
	fmt.Printf("odd number generated %d\n", generatedNumber)
	makeOddGenerator()
	fmt.Printf("odd number generated %d\n", generatedNumber)
	makeOddGenerator()
	fmt.Printf("odd number generated %d\n", generatedNumber)
	makeOddGenerator()
	fmt.Printf("odd number generated %d\n", generatedNumber)
}

func fib(number int) int {
	if number == 1 {
		return 1
	}

	for number > 1 {
		return fib(number-1) + fib(number-2)
	}

	return 0
}

func Exercise5(testValue int) {
	// The Fibonacci sequence is defined as: fib(0) = 0, fib(1) = 1, fib(n) =
	// fib(n-1) + fib(n-2). Write a recursive function that can find fib(n)

	number := testValue

	result := fib(number)

	fmt.Printf("fi(%d) is equal to: %d\n", number, result)
}

func Exercise6() {
	// What are defer, panic, and recover? How do you recover from a runtime panic?
	// with recover
}

func Exercise7() {
	// How do you get the memory address of a variable?
	// &
}

func Exercise8() {
	// How do you assign a value to a pointer?
	// *pointer = 2
}

func Exercise9() {
	// How do you create a new pointer?
	// make?
}

func Exercise10() {
	// What is the value of x after running this program:
	square := func (x *float64) {
		*x = *x * *x
	}

	x := 1.5

	square(&x)

	fmt.Print(x) //2.25
}

func Exercise11() {
	// Write a program that can swap two integers (x := 1; y := 2: swap (&x, &y))
	// should give you x=2 and y=1).

	x := 1
	y := 2

	swap := func (firstValue *int, secondValue *int){
		temp := *secondValue
		*secondValue = *firstValue
		*firstValue = temp
	}

	swap(&x, &y)

	fmt.Printf("x = %d\n", x)
	fmt.Printf("y = %d\n", y)

}
