#include<stdio.h>
int main()
{
for(int i =10;i>=-10;i--)
{
    if(i>0){
        printf("%d ",i);
    }
    else if(i==0){
       printf("%d ",i+1);
       i-=1;
    }
    else{
         printf("%d ",i*-1);
    }
}
}