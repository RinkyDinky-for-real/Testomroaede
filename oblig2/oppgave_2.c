#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main() {
  int array[1000];
  int i, min, max;


  srand(time(NULL));


  for (i = 0; i < 1000; i++) {
    array[i] = rand() % 100000;
  }

  min = array[0];
  max = array[0];

  for (i = 1; i < 1000; i++) {
    if (array[i] < min) {
      min = array[i];
    }
    if (array[i] > max) {
      max = array[i];
    }
  }

  printf("Det minste tallet er: %d\n", min);
  printf("Det største tallet er: %d\n", max);

  return 0;
}
