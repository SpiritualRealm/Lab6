# **Lab 6 Report**  
##### CSCY/CSCI 4742: Cybersecurity Programming and Analytics, Spring 2026

**Name & Student ID**: John Paul Bennett Jr., 110412273  

---

## **Task 1: Implement & Analyze Additional Vulnerabilities**  

1. **Commented Source Code**  
	![Vulnerable Program](vulnerable_program.c)
2. **Program Outputs**
     ![Screenshot1](Screenshots/Lab6Task1Screenshot2.png)
     ![Screenshot2](Screenshots/Lab6Task1Screenshot3.png)
     ![Screenshot3](Screenshots/Lab6Task1Screenshot4.png)

---

## **Task 2: Out-of-Bounds Write (Valgrind)**
### **Screenshots**  
![Screenshot2](Screenshots/Lab6Task2.png) 
![Screenshot2](Screenshots/Lab6Task2Screenshot2.png) 
![Screenshot2](Screenshots/Lab6Task2Screenshot3.png) 
![Screenshot2](Screenshots/Lab6Task2Screenshot4.png) 

### **Answers to Questions**  
- **1.** Why does this invalid write error happen?  
The error happens when a program attempts to write data to a memory location outside the boundaries of its allocated buffer or array.

- **2.** Why does Valgrind report an "invalid write of size 4"? What does `4` represent?  
Valgrind reports "invalid write of size 4" to indicate that the program attempted to write four bytes of data to a memory location it is not allowed to access, the number of bytes written being represented by the four.

- **3.** What is an off-by-one error? Do you see this error in the `overRun` function?
An off-by-one-error is a logic error that occurs commonly and is where a loop or algorithm iterates one time too many or one time too few. I do not see the error in the 'overRun' function.
- **4.** What is a memory leak? Explain in your own words. Do you see a memory leak in the `overRun` function?  
A memory leak is an error within a computer program when it fails to release allocated but unnecessary memory. This causes issues such as makin the computer program use more amounts of RAM in the computer system as time passes. I do see a memory leak in the overRun function as 40 bytes of data were lost according to the Valgrind leak summary. 
- **5.** Can errors like this occur in Java? Why or why not?  
Errors like that can still occur in Java. Even though the Java programming language has a built in garbage collector which manages memory, objects that are unneeded but still referenced due to programming mistakes can still leak.
- **6.** Compare the Heap Summary from normal Valgrind output vs. `--leak-check=full`. What additional details are shown?  
Information that indicates how many bytes of allocated data were lost, and information showing the numbers which indicate lines of code where programming errors began as functions were called.

### **Updated Code for `overRun` Function**  
```c
// Function for triggering buffer overrun
void safeRun(void) {
	int *x = malloc(10 * sizeof(int));
	if (x == NULL) {
		// Handle allocation failure
		return;
	}
```

---

## **Task 3: Uninitialized Pointer Analysis**  
### **Screenshots**  
![Screenshot2](Screenshots/Lab6Task3.png) 
![Screenshot2](Screenshots/Lab6Task3Screenshot2.png)   
![Screenshot2](Screenshots/Lab6Task3Screenshot3.png) 

### **Answers to Questions**  
- **7.** Where is the memory problem occurring? What does Valgrind report?  
The memory problem occurs on lines 39 and 43 in the program according to the Valgrind report. Valgrind reports that there is an issue with the strcpy function usage. Valgrind also reports that an unitialised value was created by a stack allocation.
- **8.** What is an uninitialized pointer? How could it be exploited?  
An uninitialized pointer is a variable declared as a pointer but not assigned a valid memory address. It can be exploited to cause system crashes, unauthorized memory reads/information leaks, and even arbitrary code execution by writing to unintended memory locations.
- **9.** What is the difference between a `NULL` pointer and an uninitialized pointer?  
A null pointer is explicitly assigned a specific known value: "NULL"/"nullptr", which indicates that it does not point to any valid memory location. An uninitialized pointer, however, contains an arbitrary and unknown garbage value that is left over in memory.
- **10.** What specifically in the code do you believe caused the uninitialized pointer usage?  
According to the Valgrind report, line 39 was responsible for the uninitialized pointer usage. The free() code had been used at the wrong time, and as a result, unnecessary memory was referenced, thus leading to the uninitialized pointer usage. In short, it had been caused by a dangling pointer.
- **11.** What additional detail does `--track-origins=yes` provide?  
It shows the origin of the programming error. In this case, the programming error's source was a stack allocation caused by line 39 in the vulnerable program's code.
- **12.** "Use of uninitialized value of size 8" — what does the `8` refer to?  
8 refers to the size, in bytes, of the uninitialized data type the program is using.

### **Updated Code for `unInitializedPtr` Function**  
```c
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
```

---

## **Task 4: Dangling Pointer Analysis**  
### **Screenshots**  
![Screenshot2](Screenshots/Lab6Task4.png) 
![Screenshot2](Screenshots/Lab6Task4Screenshot2.png) 
![Screenshot2](Screenshots/Lab6Task4Screenshot3.png) 

### **Answers to Questions**  
- **13.** What is the potential issue in the `danglingPtr` function?  
The potential issue is the placement of the "free()" function within the 'danglingPtr' function. Freeing memory at the wrong time can lead to a dangling pointer.
- **14.** How could a dangling pointer be exploited?  
It can be exploited to achieve serious security compromises, especially arbitrary code execution, denial of service attacks, and information leakage.
- **15.** What does Valgrind report about the freed memory usage?  
It reports that there were 2 frees in total heap usage. There were also 2 allocations and a total of 1,064 bytes had been allocated.
- **16.** Why does Valgrind possibly show no final "heap error" even though it’s a dangerous bug?  
It may report no heap errors because it only detects issues during actual execution of flawed code paths. Valgrind only monitors memory access.

### **Updated Code for `danglingPtr` Function**  
```c
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
```

---

## **Task 5: Buffer Overflows Analysis**  
### **Screenshots**  
- **For `bufferUnder` (Input 4):**  
  1. *(Screenshot of Valgrind output with `./vulnerable_program 4`.)*  
- **For `bufferOver` (Input 5):**  
  2. *(Screenshot of Valgrind output with `./vulnerable_program 5` — if any overflow detected.)*  
  3. *(Screenshot of AddressSanitizer detection using `./vulnerable_program2 5`.)*  
  4. *(Screenshot after fixing `bufferOver`, no errors remain.)*  

### **Answers to Questions**  
- **(Regarding `bufferUnder`, Input 4)**  
  - **15.** Do you see errors in the Valgrind output?  
    *(Answer here)*  
  - **16.** After reading the code, do you expect errors? Why/why not?  
    *(Answer here)*  

- **(Regarding `bufferOver`, Input 5)**  
  - **17.** Do you expect an error here? Why?  
    *(Answer here)*  
  - **18.** Does Valgrind detect it? If so, what is reported?  
    *(Answer here)*  
  - **19.** Why does Valgrind sometimes struggle to detect this kind of buffer overflow?  
    *(Answer here)*  

- **(Valgrind vs. Other Tools)**  
  - **20.** List two additional Valgrind tools besides `memcheck`.  
    *(Answer here)*  
  - **21.** How could these other tools detect errors that `memcheck` misses?  
    *(Answer here)*  

### **AddressSanitizer Findings**  
- **22.** What errors does AddressSanitizer report for input `5`?  
  *(Answer here)*  
- **23.** Where in the code does it say the error occurs?  
  *(Answer here)*  
- **24.** How does AddressSanitizer compare to Valgrind in detecting buffer overflows?  
  *(Answer here)*  

### **Updated Code for `bufferOver` Function**  
```c
/* Insert your corrected bufferOver function here. 
   Include inline comments explaining the fix. */
```

---

## **Task 6: Integer Overflow Analysis**  
### **Screenshots**  
1. *(Screenshot of `./vulnerable_program 6` showing normal run — note any incorrect result.)*  
2. *(Screenshot of `valgrind --tool=memcheck ... ./vulnerable_program 6` showing whether it detects overflow.)*  
3. *(Screenshot of UBSan detection: `./vulnerable_program2 6`.)*  
4. *(Screenshot of fixed function, showing no more overflow vulnerability.)*  

### **Answers to Questions**  
- **25.** Why does the overflow occur at `UINT_MAX + 1`?  
  *(Answer here)*  
- **26.** What are common security risks of integer overflows, and how might attackers exploit them?  
  *(Answer here)* 
 - **27.** Does Valgrind report the integer overflow? If not, why?  
 *(Answer here)* 
- **28.** Does UBSan report an error?  
  *(Answer here)*  
- **29.** Where in the code does UBSan say the overflow occurs?  
  *(Answer here)*  
- **30.** Compare UBSan’s detection to Valgrind’s.  
  *(Answer here)*  

### **Updated Code for `integerOverflow` Function**  
```c
/* Insert your corrected integerOverflow function here. 
   Include inline comments explaining the fix. */
```

---

## **Task 7: Static Analysis with Flawfinder**  
### **Screenshots**  
1. *(Screenshot of `flawfinder vulnerable_program.c` output.)*  

### **Answers to Questions**  
- **31.** Differentiate static vs. dynamic analysis of source code.  
  *(Answer here)*  
- **32.** How do static analysis tools like Flawfinder differ from dynamic tools (Valgrind, AddressSanitizer)?  
  *(Answer here)*  

### **Flawfinder Vulnerabilities**  
- **33.** `strcpy` issues  
  - Location, risk level, CWE classification, and prevention.  
  *(Answers here)*  
- **34.** `srand` usage (weak randomness)  
  - Why is it a concern, relevant CWE, safer alternatives.  
  *(Answers here)*  
- **35.** Statically-sized arrays  
  - Where used, security risks, relevant CWE, safer approaches.  
  *(Answers here)*  

*(Paste or summarize key parts of the Flawfinder output. Explain any false positives or unaddressed concerns.)*

---


# **Lab 6: Summary & Reflections**  

### **Key Takeaways from Lab 6**  
*(Summarize your main findings, what you learned, and any challenges faced during the lab.)*  
