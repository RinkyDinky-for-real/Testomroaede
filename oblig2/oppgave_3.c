#include <stdio.h>

long fib(int n) {
  if (n == 0) {
    return 0;
  } else if (n == 1) {
    return 1;
  } else {
    long a = 0, b = 1, c;
    for (int i = 2; i <= n; i++) {
      c = a + b;
      a = b;
      b = c;
    }
    return b;
  }
}

int main() {
  int n;


  printf("Skriv inn en verdi for n: ");
  scanf("%d", &n);


  FILE *file = fopen("fibonacci.txt", "w");
  if (file == NULL) {
    printf("Kunne ikke åpne filen for skriving.\n");
    return 1;
  }

  for (int i = 0; i <= n; i++) {
    fprintf(file, "F%d = %ld\n", i, fib(i));
  }


  fclose(file);
  printf("Fibonacci-tallene fra F0 til F%d er lagret i filen fibonacci.txt.\n", n);

  return 0;
}
