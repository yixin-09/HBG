#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <math.h>
#include <gsl/gsl_sf.h>
#include "herbgrind.h"

int main(int argc, char** argv){
  FILE *stream;
  double x;
  double y;
char *line = NULL;
size_t len = 0;
ssize_t read;

stream = fopen("gsl_sf_expint_Ei.txt", "r");
if (stream == NULL)
	exit(EXIT_FAILURE);

while ((read = getline(&line, &len, stream)) != -1) {
    x = atof(line);
    HERBGRIND_BEGIN();
    /*double y = gsl_sf_legendre_P2 (x);*/
y = gsl_sf_expint_Ei(x);
    HERBGRIND_MARK_IMPORTANT(y);
}

free(line);
fclose(stream);
  return 0;
  
}

