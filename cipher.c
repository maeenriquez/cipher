#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define keylength 26

int validate_key(char *key);
char *plain_to_cipher(char *key, char *plaintext);

int main(int argc, char *argv[])
{
    if (argc == 2)
    {
        char *key = argv[1];
        int validatedkey = validate_key(key);
        if (validatedkey == 1)
        {
            return 1;
        }
        else if (validatedkey == 0)
        {
            char plaintext[100];
            printf("plaintext: ");
            fgets(plaintext, sizeof(plaintext), stdin);
            plaintext[strcspn(plaintext, "\n")] = '\0';
            char *ciphertext = plain_to_cipher(key, plaintext);
            printf("ciphertext: %s\n", ciphertext);
            free(ciphertext);
            return 0;
        }
    }
    else
    {
        printf("Usage: ./substitution KEY\n");
        return 1;
    }
}

int validate_key(char *key)
{
    if (strlen(key) == 26)
    {
        char c;
        for (int i = 0, n = strlen(key); i < n; i++)
        {
            c = key[i];

            if (isalpha(c))
            {
                for (int j = 0; j < n - 1; j++)
                {
                    if (j == i)
                    {
                        continue;
                    }
                    else
                    {
                        if (tolower(c) == tolower(key[j]))
                        {
                            printf("Key must not contain repeated characters.\n");
                            return 1;
                        }
                    }
                }
            }

            else if (!isalpha(c))
            {
                printf("Key must only contain alphabetic characters.\n");
                return 1;
            }
        }
        return 0;
    }

    else
    {
        printf("Key must contain 26 characters.\n");
        return 1;
    }
}

char *plain_to_cipher(char *key, char *plaintext)
{
    int n = strlen(plaintext);
    char *cipher = malloc(n + 1);

    if (cipher == NULL)
    {
        return NULL;
    }

    for (int i = 0; i < n; i++)
    {
        char c = plaintext[i];

        if (isalpha(c))
        {
            char upperc = toupper(plaintext[i]);
            char uppercipher = key[upperc - 'A'];
            if (isupper(c))
            {
                cipher[i] = toupper(uppercipher);
            }
            else if (islower(c))
            {
                cipher[i] = tolower(uppercipher);
            }
        }

        else
        {
            cipher[i] = c;
        }
    }

    cipher[n] = '\0';
    return cipher;
}
