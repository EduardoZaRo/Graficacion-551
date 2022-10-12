/*
    Nombre:         TEST.C
    Equipo:
                    Amezquita Becerra Carlos Daniel (1262695)
                    Rivera Soto Dayanara            (1271872)
                    Soto Elenes Brian Ramiro        (1254563)

    Descripcion:    Programa que rota un triangulo.
    Fecha:          28 de septiembre
    Nota:           ESTE PROGRAMA DEBE SER COMPILADO Y CORRIDO EN TURBO C
*/



# include<stdio.h>
# include<conio.h>
# include<graphics.h>
# include "geo.h"

void pruebaRotacion();
void pruebaRotacionTriangulo();

int main()
{
    pruebaRotacionTriangulo();
	return 0;
}

void pruebaRotacion(){
    float x,y,x1,y1;
    int i;

	printf("X: ");
	scanf("%f",&x);
	printf("Y: ");
	scanf("%f",&y);

	printf("A\tX\tY\n");
    for(i=0; i<36; i++){
        printf("%3d\t% -0.f\t% -0.f\n",i*10,rotatePointX(x,y,i*10),rotatePointY(x,y,i*10));
    }
	getch();
}


void pruebaRotacionTriangulo(){
	int gdriver=DETECT, gmode, error, i;
    float ax = 50,bx = 150,cx = 100,ay = 50,by = 50,cy = 150, O = 180;
	initgraph(&gdriver, &gmode, "c:\\turboc3\\bgi");
	clearviewport();
    line(ax,ay,bx,by);
    line(bx,by,cx,cy);
    line(cx,cy,ax,ay);
    for(i = 0; i < 36; i++){
	clearviewport();
	rotatePointR(&ax,&ay,10,100,100);
	rotatePointR(&bx,&by,10,100,100);
	rotatePointR(&cx,&cy,10,100,100);
	line(ax,ay,bx,by);
	line(bx,by,cx,cy);
	line(cx,cy,ax,ay);
	delay(30);
	//printf("%d\t%d\n",(int)ax,(int)ay);
	//printf("%d\t%d\n",(int)bx,(int)by);
	//printf("%d\t%d\n",(int)cx,(int)cy);
    }
	getch();
	closegraph();
}
