// There are no classes
package main

import (
	"fmt"
	"math"
)

type Bikvadrat struct {
	a float64
	b float64
	c float64
}

func NewBikvadrat(a float64, b float64, c float64) *Bikvadrat {
	return &Bikvadrat{a: a, b: b, c: c}
}

func RoundToDecimal(value float64, places int) float64 {
	pow := math.Pow(10, float64(places))
	return math.Round(value*pow) / pow
}

func Solve(n Bikvadrat) []float64 {
	D := n.b*n.b - 4*n.a*n.c
	roots := []float64{}
	if D < 0 {
		return roots
	} else if D == 0 {
		x := -n.b / 2 / n.a
		if x > 0 {
			roots = append(roots, RoundToDecimal(math.Pow(float64(x), float64(0.5)), 4))
			roots = append(roots, RoundToDecimal(-math.Pow(float64(x), float64(0.5)), 4))
		}
	} else {
		x1 := -(n.b + math.Pow(float64(D), float64(0.5))) / 2 / float64(n.a)
		x2 := -(n.b - math.Pow(float64(D), float64(0.5))) / 2 / float64(n.a)
		if x1 > 0 {
			roots = append(roots, RoundToDecimal(math.Pow(float64(x1), float64(0.5)), 4))
			roots = append(roots, RoundToDecimal(-math.Pow(float64(x1), float64(0.5)), 4))
		}
		if x2 > 0 {
			roots = append(roots, RoundToDecimal(math.Pow(float64(x2), float64(0.5)), 4))
			roots = append(roots, RoundToDecimal(-math.Pow(float64(x2), float64(0.5)), 4))
		}
	}
	return roots
}

func main() {
	var a int16
	fmt.Print("Введите a: ")
	fmt.Scan(&a)
	var b int16
	fmt.Print("Введите b: ")
	fmt.Scan(&b)
	var c int16
	fmt.Print("Введите c: ")
	fmt.Scan(&c)
	Ans := NewBikvadrat(float64(a), float64(b), float64(c))
	roots := []float64{}
	roots = Solve(*Ans)
	if len(roots) == 0 {
		fmt.Print("Уравнение не имеет корней")
	} else if len(roots) == 2 {
		fmt.Print("Уравнение имеет два корня ", roots)
	} else {
		fmt.Print("Уравнение имеет четыре корня ", roots)
	}

}
