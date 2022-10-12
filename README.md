# Kaprekar Number Calculator

```
python3 kaprekar.py
```
6174 is known as Kaprekar's constant after the Indian mathematician D. R. Kaprekar. This number is renowned for the following rule:

Take any four-digit number, using at least two different digits (leading zeros are allowed).
Arrange the digits in descending and then in ascending order to get two four-digit numbers, adding leading zeros if necessary.
Subtract the smaller number from the bigger number.
Go back to step 2 and repeat.

The above process, known as Kaprekar's routine, will always reach its fixed point, 6174, in at most 7 iterations.[4] Once 6174 is reached, the process will continue yielding 7641 – 1467 = 6174. For example, choose 1495:

9541 – 1459 = 8082
8820 – 0288 = 8532
8532 – 2358 = 6174
7641 – 1467 = 6174
The only four-digit numbers for which Kaprekar's routine does not reach 6174 are repdigits such as 1111, which give the result 0000 after a single iteration. All other four-digit numbers eventually reach 6174 if leading zeros are used to keep the number of digits at 4. For numbers with three identical numbers and a fourth number that is one number higher or lower (such as 2111), it is essential to treat 3-digit numbers with a leading zero; for example: 2111 – 1112 = 0999; 9990 – 999 = 8991; 9981 – 1899 = 8082; 8820 – 288 = 8532; 8532 – 2358 = 6174.[5]

#### references: https://en.wikipedia.org/wiki/6174_(number)

