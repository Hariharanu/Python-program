#include<stdio.h>
#include<conio.h>
void main()
{
int a,s,i;
clrscr();
printf("Enter the value of A:\t");
scanf("%d",&a);
for(i=1;i<=5;i++)
{
s=a*i;
printf("%d\t",s);
}
getch();
}