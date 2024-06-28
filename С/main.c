#include <stdio.h>
#include <stdint.h>

// Определение функции func
int func(uint32_t val) {
    int res = 0;
    while (val != 0) {
        if ((val & 0x1) != 0)
            res += 1;
        val >>= 1;
    }
    return res;
}

// Главная функция
int main() {
    uint32_t value = 16; // Входное значение
    int result = func(value); // Вызов функции func
    printf("Количество установленных битов в %u: %d\n", value, result); // Вывод результата
    return 0;
}