#include <stdio.h>
#include <stdlib.h>
#include <time.h>


int main() {
   int i, n;
   time_t t;
   
   n = 2;
   
   srand((unsigned) time(&t));

   for( i = 0 ; i < n ; i++ ) {
      switch(rand() % 3){
         case 0:
            puts("Case 0");break;
         case 1:
            puts("Case 1");break;
         case 2:
            puts("Case 2");break;
      }
   }
   
  return(0);
}