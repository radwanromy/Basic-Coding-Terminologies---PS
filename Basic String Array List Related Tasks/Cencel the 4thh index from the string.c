#include <stdio.h>
#include <string.h>

int main()
{
   char word[] = "sadsdawaw";
   char word2[10];
   for(int i = 0 ; i<=10;i++){
       if(i<4)
       {
           word[i]=word2[i];
           
       }
       else if(i==4){
           i+=1;
       }
       else{
           word[i]=word2[i];
       }
   }

   printf("%s\n", word2);

   return 0;
}