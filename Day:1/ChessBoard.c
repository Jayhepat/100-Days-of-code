#include <stdio.h>
#include <string.h>

const char* determine_color(const char* s) {
    char col = s[0];
    int row = s[1] - '0';
    int col_num = col - 'a' + 1;

    if ((col_num + row) % 2 == 0) {
        return "Black";
    } else {
        return "White";
    }
}

int main() {
    char s[256];
    scanf("%s", s);
    const char* result = determine_color(s);
    printf("%s\n", result);
    return 0;
}
