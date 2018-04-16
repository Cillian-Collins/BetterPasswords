#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <ctype.h>

int validation(char *password){
	int length;
	char string[100];
	strcpy(string, password);
	length = strlen(string);
	if (length <= 20 && length >= 6){
		return 1;
	}
	else {
		return 0;
	}
}

int main () {
	char input[150];
	int num = 1000+(rand()%9000);
	printf("Password: ");
	scanf("%s", &input);
	while (!validation(input) || !isalpha(*input)){
		printf("Password: ");
		scanf("%s", &input);
	}
	if (validation(input) && isalpha(*input)){
		input[0] = toupper(input[0]);
		printf("Your new password: #%s%d", input, num);
	}
}