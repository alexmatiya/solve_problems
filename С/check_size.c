#include <stdio.h>
#include <stdint.h>

struct my_struct {
    uint8_t proto;
    uint32_t saddr;
    uint32_t daddr;
    uint16_t sport;
    uint16_t dport;
};

int main() {
    printf("Size of struct: %zu bytes\n", sizeof(struct my_struct));
    return 0;
}