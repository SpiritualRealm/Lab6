// C Module Libraries
#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <time.h>
#include <limits.h> // Required for integer limits

// Function for triggering buffer overrun
void safeRun(void) {
	int *x = malloc(10 * sizeof(int));
	if (x == NULL) {
		// Handle allocation failure
		return;
	}
	
	// Safely initialize the array
	for (int i = 0; i < 10; i++) {
		x[i] = 0; // Safe, within bounds
	}
	
	// Use array as required
	
	free(x); // Free allocated memory
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
void PtrSafeguard(void) {
	int *x;
	int *y = malloc(10 * sizeof(int));
	
	if (y == NULL) {
		printf("Memory allocation failed!\n");
		return; // Exit if there is a memory allocation failure
	}
	
	x = y;
	
	// Perform operations on variables x or y
	
	free(y); // Free memory
	y = NULL; // Set variable to NULL to avoid accidental use
	
	x = NULL; // Set variable to NULL to avoid accidental use
	
	// Safely access x or y given that they are NULL
	if (x != NULL) {
		int t = x[2]; // Safe, won't be executed
		printf("Dangling pointer value: %d\n", t);
	} else {
		printf("Pointer is NULL, access denied.\n");
	}
}

// Function for triggering uninitialized pointer usage
void InitializedPtr(void) {
	// Initialize 'buffer' pointer
	char *buffer = malloc(10 * sizeof(char)); // Allocate memory for buffer
	if (buffer == NULL) {
	printf("Memory allocation failed for buffer!\n");
	return; // Exit if there is a memory allocation failure
	}
	
	// Properly allocate memory for 'c' variable
	char *c = malloc(10 * sizeof(char));
	if (c == NULL) {
		printf("Memory allocation failed for c!\n");
		free(buffer); // Free any memory allocated previously.
		return;
	}
	
	randStringGen(10, c); // Generate random string in 'c' variable
	
	// Copy string from 'c' to 'buffer'
	strcpy(buffer, c);
	
	// Print string
	printf("%s\n", buffer);
	
	// Free the allocated memory
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
	
	if (x == 1) { // Triggers safe buffer run
		safeRun();
	} else if (x == 2) { // Triggers uninitialized pointer usage
		InitializedPtr();
	} else if (x == 3) { // Triggers dangling pointer access
		PtrSafeguard();
	} else if (x == 4) { // Triggers potential buffer overflow
		bufferUnder();
	} else if (x == 5) { // Triggers buffer overflow
		bufferOver();
	} else if (x == 6) { // Triggers integer overflow
		integerOverflow();
	}
	
	return 0; // Returns an exit code of 0.
}
