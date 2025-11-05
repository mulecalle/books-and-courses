package main

import (
	"../book-introducing-go/chapters"
	"fmt"
	"os"
	"strconv"
)

func main() {

	testValue := 0


	chapter, _ := strconv.Atoi(os.Args[1])
	exercise, _ := strconv.Atoi(os.Args[2])

	if len(os.Args) > 3 {
		testValue, _ = strconv.Atoi(os.Args[3])
	}

	chapter6 := func (exerciseNumber int){
		switch exerciseNumber {
			case 1:
				chapters.Exercise1()
			case 2:
				chapters.Exercise2()
			case 3:
				chapters.Exercise3()
			case 4:
				chapters.Exercise4()
			case 5:
				chapters.Exercise5(testValue)
			case 6:
				chapters.Exercise6()
			case 7:
				chapters.Exercise7()
			case 8:
				chapters.Exercise8()
			case 9:
				chapters.Exercise9()
			case 10:
				chapters.Exercise10()
			case 11:
				chapters.Exercise11()
			default:
				fmt.Print("have no idea what you are talking about")
		}
	}

	switch chapter {
		case 6:
			chapter6(exercise)
		default:
			fmt.Println("chapter not found")
	}
}
