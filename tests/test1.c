/*
    This file is meant to be compiled to an assembly file for testing syntax highlighting,
    compiled with the intel syntax option
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void reverse_string(char* str) 
{
    int left = 0;
    int right = strlen(str) - 1;

    while (left < right) 
    {
        char temp = str[left];
        str[left] = str[right];
        str[right] = temp;
        left++;
        right--;
    }
}

int factorial(int n) 
{
    if (n == 0 || n == 1)
        return 1;
    else
        return n * factorial(n - 1);
}

int main() 
{
    char name[50];
    int num, i;
    float avg = 0.0;
    int numbers[10];

    printf("enter your name: ");
    fgets(name, sizeof(name), stdin);
    name[strcspn(name, "\n")] = '\0';

    printf("hello, %s, let's do some random stuff.\n", name);

    printf("random numbers: ");
    for (i = 0; i < 10; i++) 
    {
        numbers[i] = rand() % 100;
        printf("%d ", numbers[i]);
        avg += numbers[i];
    }

    avg /= 10;
    printf("\n");

    printf("average of the random numbers: %.2f\n", avg);

    reverse_string(name);
    printf("your name reversed: %s\n", name);

    printf("enter a number: ");
    scanf("%d", &num);

    int fact = factorial(num);
    printf("factorial of %d is: %d\n", num, fact);

    // determine if the number is prime or not
    int is_prime = 1;
    for (i = 2; i <= num / 2; i++) 
    {
        if (num % i == 0) 
        {
            is_prime = 0;
            break;
        }
    }

    if (is_prime)
        printf("%d is a prime number.\n", num);
    else
        printf("%d is not a prime number.\n", num);

    // randomly select and print a message
    char* messages[] = {
        "printed circut board",
        "a is a cool letter",
        "chalk",
        "bowling pin",
        "b"
    };

    int num_messages = sizeof(messages) / sizeof(messages[0]);
    int random_index = rand() % num_messages;
    printf("random message: %s\n", messages[random_index]);

    return 0;
}