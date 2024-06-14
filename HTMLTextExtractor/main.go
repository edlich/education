package main

import (
	"fmt"
	"log"
	"net/http"
	"os"
	"strings"

	"github.com/PuerkitoBio/goquery"
)

func main() {
    url := os.Args[1]
    selector := os.Args[2]

    fmt.Println(url)
    fmt.Println(selector)

    resp, err := http.Get(url)
    if err != nil {
        log.Fatal(err)
    }
    defer resp.Body.Close()
    
    if resp.StatusCode != 200 {
        log.Fatalf("status code error: %d %s", resp.StatusCode, resp.Status)
    }

    //Load the HTML Document
    doc, err := goquery.NewDocumentFromReader(resp.Body)
    if err != nil {
        log.Fatal(err)
    }

    result, err := doc.Find(selector).Html()
    if err != nil {
        log.Fatal(err)
    }
    result_trimmed := strings.TrimSpace(result)
    fmt.Println(result_trimmed)
}
