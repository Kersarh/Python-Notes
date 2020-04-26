package main

import "C"
import "fmt"

//export PrintData
func PrintData() {
    fmt.Println("DLL DATA!")
}

//export SumData
func SumData(i int) int {
	return i+i
}

func main() {
    // Необходима как точка входа для компилятора
}