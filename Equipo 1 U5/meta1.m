%Meta 1 Equipo 1
clear all
clc
load dragon_vertex.dat;
load dragon_faces.dat;
verts=dragon_vertex;
faces=dragon_faces;
rgb = [215 215 0]
rgb=rgb/norm(rgb); 
figure
hold on
patch('faces',faces,'vertices',verts,'FaceColor',rgb,'linestyle','none');

camlight('headlight')% creates a light at the camera position.
material('shiny');
viewmtx(-37.5,30,10) %change the orientation
grid on;box on;
xlabel('x');ylabel('y');zlabel('z');
set(gca,'DataAspectRatio',[1 1 1])
hold off;