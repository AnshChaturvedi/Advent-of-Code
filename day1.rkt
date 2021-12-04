;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-intermediate-lambda-reader.ss" "lang")((modname day1) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #f #t none #f () #t)))
(require htdp-trace)
;; --------------------------- Part 1 ---------------------------

;; solves the puzzle
(define (larger lst)
  (larger-measurements (rest lst) (first lst)))

(define (larger-measurements lst current)
  (cond [(empty? lst) 0]
        [(> (first lst) current)
         (add1 (larger-measurements (rest lst) (first lst)))]
        [else (larger-measurements (rest lst) (first lst))]))

;; --------------------------- Part 2 ---------------------------

;; solves the puzzle
(define (window lst)
  (window-helper (rest lst) (+ (first lst) (second lst) (third lst))))

(define (window-helper lst current)
  (cond [(< (length lst) 3) 0]
        [(> (+ (first lst) (second lst) (third lst)) current)
         (add1 (window-helper (rest lst) (+ (first lst) (second lst) (third lst))))]
        [else (window-helper (rest lst) (+ (first lst) (second lst) (third lst)))]))