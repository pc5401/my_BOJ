# [Gold I] Generators - 11741 

[문제 링크](https://www.acmicpc.net/problem/11741) 

### 성능 요약

메모리: 35480 KB, 시간: 1616 ms

### 분류

수학, 정수론

### 제출 일자

2025년 3월 12일 14:29:00

### 문제 설명

<p>Little Roman is studying linear congruential generators — one of the oldest and best known pseudorandom number generator algorithms. Linear congruential generator (LCG) starts with a non-negative integer number x<sub>0</sub> also known as seed and produces an infinite sequence of non-negative integer numbers x<sub>i</sub> (0 ≤ x<sub>i</sub> < c) which are given by the following recurrence relation:</p>

<p style="text-align:center">x<sub>i+1</sub> = (ax<sub>i</sub> + b) mod c</p>

<p>here a, b, and c are non-negative integer numbers and 0 ≤ x<sub>0</sub> < c.</p>

<p>Roman is curious about relations between sequences generated by different LCGs. In particular, he has n different LCGs with parameters a<sup>(j)</sup>, b<sup>(j)</sup>, and c<sup>(j)</sup> for 1 ≤ j ≤ n, where the j-th LCG is generating a sequence x<sub>i</sub><sup>(j)</sup>. He wants to pick one number from each of the sequences generated by each LCG so that the sum of the numbers is the maximum one, but is not divisible by the given integer number k.</p>

<p>Formally, Roman wants to find integer numbers t<sub>j</sub> ≥ 0 for 1 ≤ j ≤ n to maximize s = Σ<sup>n</sup><sub>j=1</sub> x<sub>t<sub>j</sub></sub><sup>(j)</sup>  subject to constraint that s mod k ≠ 0.</p>

### 입력 

 <p>The first line of the input file contains two integer numbers n and k (1 ≤ n ≤ 10 000, 1 ≤ k ≤ 10<sup>9</sup>). The following n lines describe LCGs. Each line contains four integer numbers x<sub>0</sub><sup>(j)</sup>, a<sup>(j)</sup>, b<sup>(j)</sup>, and c<sup>(j)</sup> (0 ≤ a<sup>(j)</sup>, b<sup>(j)</sup> ≤ 1000, 0 ≤ x<sub>0</sub><sup>(j)</sup> < c<sup>(j)</sup> ≤ 1000).</p>

### 출력 

 <p>If Roman’s problem has a solution, then write on the first line of the output file a single integer s — the maximum sum not divisible by k, followed on the next line by n integer numbers t<sub>j</sub> (0 ≤ t<sub>j</sub> ≤ 10<sup>9</sup>) specifying some solution with this sum.</p>

<p>Otherwise, write to the output file a single line with the number −1.</p>

