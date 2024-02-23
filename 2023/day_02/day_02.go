package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"
)

const (
	maxRed   = 12
	maxGreen = 13
	maxBlue  = 14
)

func main() {
	//part1()
	part2()
}

type handful struct {
	red   int
	green int
	blue  int
}

type game struct {
	number   int
	hands    []handful
	minRed   int
	minBlue  int
	minGreen int
}

func part1() {
	games := parseGames()
	sum := 5050
	for _, g := range games {
		for _, h := range g.hands {
			if h.red > maxRed || h.green > maxGreen || h.blue > maxBlue {
				sum -= g.number
				break
			}
		}
	}

	fmt.Println(sum)
}

func part2() {
	games := parseGames()
	sum := 0
	for i, g := range games {
		for _, h := range g.hands {
			if h.red > games[i].minRed {
				games[i].minRed = h.red
			}
			if h.green > games[i].minGreen {
				games[i].minGreen = h.green
			}
			if h.blue > games[i].minBlue {
				games[i].minBlue = h.blue
			}
		}
		sum += games[i].minRed * games[i].minGreen * games[i].minBlue
	}
	fmt.Println(sum)

}

func parseGames() []game {
	file, err := os.Open("input.txt")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()
	games := make([]game, 0, 100)
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		g := game{}
		gamePieces := strings.Split(scanner.Text(), ":")
		gameTitle := gamePieces[0]
		hands := strings.Split(gamePieces[1], ";")
		for _, h := range hands {
			hand := handful{}
			for _, c := range strings.Split(h, ",") {
				if strings.Contains(c, "red") {
					hand.red, _ = strconv.Atoi(strings.TrimSpace(strings.Split(c, "red")[0]))
				} else if strings.Contains(c, "green") {
					hand.green, _ = strconv.Atoi(strings.TrimSpace(strings.Split(c, "green")[0]))
				} else if strings.Contains(c, "blue") {
					hand.blue, _ = strconv.Atoi(strings.TrimSpace(strings.Split(c, "blue")[0]))
				}
			}
			g.hands = append(g.hands, hand)
		}
		g.number, err = strconv.Atoi(strings.Split(gameTitle, " ")[1])
		games = append(games, g)
	}
	return games
}
