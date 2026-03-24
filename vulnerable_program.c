// C Module Libraries
#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <time.h>
#include <limits.h> // Required for integer limits

// Function for triggering buffer overrun
void overRun(void) {
	int *x = malloc(10 * sizeof(int));
	x[10] = 0; // Buffer overrun
}

// Function for generating random strings
void randStringGen(int x, char* c) {
	srand(time(NULL));
	for (int i = 0; i < x - 1; ++i) {
		*c = 'A' + (rand() % 26);
		c++;
	}
	*c = '\0';
}

// Function for triggering a potential buffer overflow
void bufferUnder(void) {
	char buffer[256];
	char *c = malloc(255 * sizeof(char));
	randStringGen(255, c);
	strcpy(buffer, c); // Possible buffer overflow
	printf("%s\n", buffer);
	free(c);
}

// Function for triggering dangling pointer access
void danglingPtr(void) {
	int *x;
	int *y = malloc(10 * sizeof(int));
	x = y;
	free(y); // x is now a dangling pointer
	int t = x[2]; // Accessing freed memory
	printf("Dangling pointer value: %d\n", t);
}

// Function for triggering uninitialized pointer usage
void unInitializedPtr(void) {
	char *buffer;
	char *c = malloc(10 * sizeof(char));
	randStringGen(10, c);
	strcpy(buffer, c); // Using an uninitialized pointer
	printf("%s\n", buffer);
	free(c);
	free(buffer);
}

// Function for triggering buffer overflow
void bufferOver(void) {
	char buffer[256];
	char *c = malloc(260 * sizeof(char));
	randStringGen(260, c);
	strcpy(buffer, c); // Buffer overflow
	printf("%s\n", buffer);
	free(c);
}

// New: Integer Overflow Vulnerability
void integerOverflow(void) {
	int a = INT_MAX; // Max signed int value
	int b = 1;
	int result = a + b; // Causes overflow
	printf("Integer Overflow: %d + %d = %n", a, b, result);
}

// Program's main function
int main(int argc, char**argv) {
	if (argc != 2) { // Returns an exit code of 0.
		return 0;
	}
	int x = atoi(argv[1]); // Convert input to integer
	
	if (x == 1) { // Triggers buffer overrun
		overRun();
	} else if (x == 2) { // Triggers uninitialized pointer usage
		unInitializedPtr();
	} else if (x == 3) { // Triggers dangling pointer access
		danglingPtr();
	} else if (x == 4) { // Triggers potential buffer overflow
		bufferUnder();
	} else if (x == 5) { // Triggers buffer overflow
		bufferOver();
	} else if (x == 6) { // Triggers integer overflow
		integerOverflow();
	}
	
	return 0; // Returns an exit code of 0.
}
