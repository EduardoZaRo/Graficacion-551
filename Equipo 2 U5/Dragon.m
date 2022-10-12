load dragon_vertex.dat;
load dragon_faces.dat;
verts=dragon_vertex;
faces=dragon_faces;
%rgb=[0.8605 0.4675 0.2027]
%rgb=[132 25 34]
%rgb=[34.12 13.73 39.22]
rgb=[93.73 72.16 6.27]
%rgb=[27 121 49]; %color esmerald
rgb=rgb/norm(rgb); 
figure
hold on
patch('faces',faces,'vertices',verts,'FaceColor',rgb,'linestyle','none');
%add light 1
% light('Position',[-1 1 4]);
% plot3(1,3,2,'o','color',[0.7 0.7 0.0],'linewidth',3);
% plot3([1 0],[3 0],[2 0],'color',[0.7 0.7 0.0]);
% %add light 2
% light('Position',[-2 -0 2]);
% plot3(-3,-1,3,'o','color',[0.7 0.7 0.0],'linewidth',3);
% plot3([-3 0],[-1 0],[3 0],'color',[0.7 0.7 0.0]);
camlight('headlight')% creates a light at the camera position.
% material('shiny');
viewmtx(-37.5,30,10) %change the orientation
grid on;box on;
xlabel('x');ylabel('y');zlabel('z');
set(gca,'DataAspectRatio',[1 1 1])
hold off;