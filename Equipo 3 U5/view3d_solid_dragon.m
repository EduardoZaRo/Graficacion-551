% view3d_solid_dragon.m
load dragon_vertex.dat;
load dragon_faces.dat;
verts = dragon_vertex;
faces = dragon_faces;
figure
hold on
patch('faces',faces,'vertices',verts,'FaceColor','[0.9290 0.6940 0.1250]','EdgeColor', 'none','FaceLighting', 'gouraud', ...
         'AmbientStrength', 0.15);
camlight('headlight')
view(0,90) % change the orientation
grid on; box on
xlabel('x'); ylabel('y'); zlabel('z');
set(gca,'DataAspectRatio',[1 1 1])
hold off
