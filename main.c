#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <stdbool.h>
#include <windows.h>

bool checkNULL(char *s){
    if(strcmp(s,"") == 0){
        return true;
    }else{
        return false;
    }
}

main(int argc, char const *argv[])
{
    FILE *f_print = fopen("icon.txt","w");
    char *icon[100];
    char *temp;
    int i = 0;
    int counter = 0;

    while(1){
        icon[i] = (char*)malloc(10*sizeof(char));
        printf("type icon: ");
        gets(icon[i]);
         if(checkNULL(icon[i])) break;
        i++;
        counter++;
    }
    printf("================================================\n");
    printf("type number row:");
    int row;
    scanf("%d",&row);
    for(int j = 0; j < row;j++)
    {
        for(int i =0; i < counter; i++)
        {
            fprintf(f_print," %s ",icon[i]);
        }
            fprintf(f_print,"%s","\n");
    }
    printf("[");
    for(int i =0 ; i<50;i++){
        printf("%c","=");
        Sleep(i);
    }
    printf("]100%s","%");
    printf(" success! ");

    fclose(f_print);
    return 0;
}
