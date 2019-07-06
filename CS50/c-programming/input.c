// getting 'input' and print 'input'
#include <stdio.h>

int main (void)
{
  //declaring string
char name[20];
  //printing
printf("What's your name?\n");
  //reading string
scanf("%s\n", name);
  //printing string
printf("hello, %s\n", name);
return 0;
}
