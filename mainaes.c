/*Input for both plaintext and key are 16 bytes, which can be represented by decimal or  hex numbers. Also, if you put {a} then it is treated as {a, 0, É, 0} the rest of 15 are zero bytes. */ 

#include <stdio.h>

#include "aes.h"

int main()
{
	uint8_t i;

	const uint8_t plain[16] = {16, 16, 161, 1, 1, 0,0,0};
	const uint8_t key[16] = {2};
	uint8_t cipher[16] = {0};

	aes(plain, key, cipher); // to perform full AES encryption
	// aes_rounds(plain, key, 10, cipher);  // use this function can specify #rounds
		
	for (i = 0; i < 16; i++) {
		printf("%02x ", cipher[i]);
	     }
	printf("\n");
	
	//return 0;
}