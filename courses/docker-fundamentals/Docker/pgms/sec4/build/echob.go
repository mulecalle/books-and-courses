// echob.go - echo command line args backwards
package main
import ("fmt"; "os")

func main() {
    nargs := len(os.Args)
    for i := nargs-1; i > 0; i-- {
        fmt.Printf("%s ", os.Args[i])
    }
    fmt.Println()
}

/*************************************

    $ go run echob.go one two three
    three two one 

*/
