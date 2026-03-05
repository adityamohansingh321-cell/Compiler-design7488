#include <stdio.h>
#include <ctype.h>
#include <string.h>

int isKeyword(char str[]) {
    char keywords[][15] = {
        "auto","break","case","char","const","continue","default","do","double",
        "else","enum","extern","float","for","goto","if","int","long","register",
        "return","short","signed","sizeof","static","struct","switch",
        "typedef","union","unsigned","void","volatile","while"
    };

    int n = sizeof(keywords) / sizeof(keywords[0]);

    for (int i = 0; i < n; i++) {
        if (strcmp(str, keywords[i]) == 0)
            return 1;
    }
    return 0;
}

int main() {
    char input[200], token[30];
    int i = 0, j = 0;

    printf("Enter source code (Enter 0 to Exit):\n");

    while (1) {
        fgets(input, 200, stdin);

        // Exit condition
        if (input[0] == '0' && input[1] == '\n') {
            printf("Exiting Lexical Analyzer...\n");
            break;
        }

        i = 0;
        while (input[i] != '\0') {

            // Skip spaces
            if (isspace(input[i])) {
                i++;
                continue;
            }

            // Keyword or Identifier
            if (isalpha(input[i]) || input[i] == '_') {
                j = 0;
                while (isalnum(input[i]) || input[i] == '_') {
                    token[j++] = input[i++];
                }
                token[j] = '\0';

                if (isKeyword(token))
                    printf("Keyword    : %s\n", token);
                else
                    printf("Identifier : %s\n", token);
            }

            // Number
            else if (isdigit(input[i])) {
                j = 0;
                while (isdigit(input[i])) {
                    token[j++] = input[i++];
                }
                token[j] = '\0';
                printf("Number     : %s\n", token);
            }

            // Operators
            else if (strchr("+-*/=%<>!", input[i])) {
                printf("Operator   : %c\n", input[i]);
                i++;
            }

            // Separators
            else if (strchr("();{},[]", input[i])) {
                printf("Separator  : %c\n", input[i]);
                i++;
            }

            // Unknown
            else {
                printf("Unknown    : %c\n", input[i]);
                i++;
            }
        }

        printf("\nEnter source code (Enter 0 to Exit):\n");
    }

    return 0;
}
