#include <stdio.h>

int count_chars(const char *s) {
    int count = 0;
    while (*s != '\0') {
        count++;
        s++;
    }
    return count;
}

int main() {
    printf("Testing count_chars...\n");
    printf("count_chars(\"\") -> %d, expected: 0\n", count_chars(""));
    printf("count_chars(\"hello\") -> %d, expected: 5\n", count_chars("hello"));
    printf("count_chars(\"abcdefg\") -> %d, expected: 7\n", count_chars("abcdefg"));
    printf("count_chars(\"a\") -> %d, expected: 1\n", count_chars("a"));
    printf("count_chars(NULL) -> %d, expected: -1 (or some error value)\n", count_chars(NULL)); // функция не проверяет NULL, поэтому она может выдать любое значение

    return 0;
}