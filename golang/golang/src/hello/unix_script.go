package main

import (
	"log"
	"os/exec"
)

func main() {
	cmd := exec.Command("pdftotext", "Mahesh Konakalla_resume1.pdf", "resume44.txt")
	err := cmd.Run()
	log.Printf("Command finished with error: %v", err)
}
