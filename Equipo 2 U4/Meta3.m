clearvars;
% simple object 
load funcion_vertex.dat;
load funcion_faces.dat;
verts=funcion_vertex+1;
faces=funcion_faces;

Ih = [verts ones(size(verts,1),1)]';

Alpha = -37.5;
Betha = 30.0;
Phi = 0;

% [M,target]=viewProjMatrix(az,el,phi,target)
M=viewmtx(Alpha,Betha,Phi);
Vh = M*Ih;

%Vx = (Vh(1, :)) ./ (Vh(4, :));
%Vy = (Vh(2, :)) ./ (Vh(4, :));
%Vz = (Vh(3, :)) ./ (Vh(4, :));

%V = [Vx ; Vy ; Vz]';

%U = [V(1, :), V(2, :)];

% Vertices proyectados en el volumen visual 3D (xp,yp,zp)
V = Vh(1:3,:)./Vh(4,:);
% Vertices proyectados en el plano visual o ventana (xp,yp)
U =V(1:2,:)';

for k=1:size(faces,1)
    idf = [(faces(k,:)+1) (faces(k,1)+1)]';
    plot(U(idf,1),U(idf,2),'k'); hold on
end