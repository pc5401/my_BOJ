#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int solution(int n) {
    for (int x = 2; x <= n; x++){
        if (n % x == 1){
            return x;
        }
    }
    
    return 0;
}