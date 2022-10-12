clearvars;
% simple object 
load teapot_vertex.dat;
load teapot_faces.dat;
verts=teapot_vertex;
faces=teapot_faces-1;

Ih = [verts ones(size(verts,1),1)]';

Alpha = -37.5;
Betha = 30.0;
Phi = 10.0;

% [M,target]=viewProjMatrix(az,el,phi,target)
M=viewmtx(Alpha,Betha,Phi);
Vh = M*Ih;
% Vertices proyectados en el volumen visual 3D (xp,yp,zp)
V = Vh(1:3,:)./Vh(4,:);
% Vertices proyectados en el plano visual o ventana (xp,yp)
U =V(1:2,:)';
for k=1:size(faces,1)
    idf = [(faces(k,:)+1) (faces(k,1)+1)]';
    plot(U(idf,1),U(idf,2),'k'); hold on
end