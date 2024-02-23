package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"regexp"
	"sort"
	"strconv"
)

func main() {
	part1()
	part2()
}

func part1() {
	fmt.Println("Hello, Part 1!")
	file, err := os.Open("input.txt")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	numbers := make([]int, 0, 1000)
	r := regexp.MustCompile(`\d`)
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		matches := r.FindAllStringSubmatch(scanner.Text(), -1)
		fmt.Println(matches[0], matches[len(matches)-1])
		numbers = append(numbers, numberFromStrings(matches[0][0], matches[len(matches)-1][0]))
	}
	fmt.Println(numbers)
	sum := 0
	for _, n := range numbers {
		sum += n
	}
	fmt.Println(sum)
}

type regexMatch struct {
	value string
	start int
	end   int
}

func part2() {
	fmt.Println("Hello, Part 1!")
	file, err := os.Open("input.txt")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	numbers := make([]int, 0, 1000)
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		numbers = findNumbers(numbers, scanner.Text())
	}
	sum := 0
	for _, n := range numbers {
		sum += n
	}
	fmt.Println(sum)
}

func findNumbers(numbers []int, input string) []int {
	regexes := []string{
		`\d`,
		`one`,
		`two`,
		`three`,
		`four`,
		`five`,
		`six`,
		`seven`,
		`eight`,
		`nine`,
	}
	indexes := make([]regexMatch, 0, 1000)
	for _, regex := range regexes {
		r := regexp.MustCompile(regex)
		matches := r.FindAllStringIndex(input, -1)
		for _, match := range matches {
			indexes = append(indexes, regexMatch{value: input[match[0]:match[1]], start: match[0], end: match[1]})
		}
	}
	sort.Slice(indexes, func(i, j int) bool {
		return indexes[i].start < indexes[j].start
	})
	numbers = append(numbers, numberFromStrings(indexes[0].value, indexes[len(indexes)-1].value))
	return numbers
}

func numberFromStrings(s, t string) int {
	nameToNumber := map[string]string{
		"one":   "1",
		"two":   "2",
		"three": "3",
		"four":  "4",
		"five":  "5",
		"six":   "6",
		"seven": "7",
		"eight": "8",
		"nine":  "9",
	}

	_, err := strconv.Atoi(s)
	if err != nil {
		s = nameToNumber[s]
	}
	_, err = strconv.Atoi(t)
	if err != nil {
		t = nameToNumber[t]
	}
	number := s + t
	n, err := strconv.Atoi(number)
	if err != nil {
		log.Fatal(err)
	}
	fmt.Println(n)
	return n
}
