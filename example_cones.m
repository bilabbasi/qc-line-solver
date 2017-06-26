%% grid set up
N = 2^6;
W = 3;
eps = 0;
tol = 1e-6;
dx = 2/(N-1);
[x,y] = meshgrid(linspace(-1,1,N));
%% obstacle set up
theta = 0;
alpha = 0;

a = [0.5 0]';
b = [-0.5 0]';
A = rotate_point(a,theta);
B = rotate_point(b,theta);

g = min(sqrt( (x+A(1)).^2 + (y+A(2)).^2 ), ...
    sqrt( (x+B(1)).^2 + (y+B(2)).^2 )-alpha);

%% solver
[u,its] = ndim_linesolver(g,W,eps,tol);

%% plots
figure
subplot(121); surf(x,y,g)
subplot(122); surf(x,y,u)
figure
contour(x,y,g); hold on
contour(x,y,u)

%% auxilliary functions
function rot_p = rotate_point(p,theta)
%  p = p(:);
A = [cos(theta) -sin(theta);
    sin(theta) cos(theta)];
rot_p = A * p;

end