function [U, Nit,iterations] = ndim_linesolver(g,maxwidth,e,tol,display)
%% Description - QCE in 2D
% Computes the quasi-convex hull of U (in 2D) along grid directions of max
% width numdir. Sweeps along each each vector using the 1D solver.
%% set up
U = g;
err = inf;
V = gridvectors(maxwidth);%Returns set of grid directions with max width of numdir.
Nit = 0;
iterations = 0;
%% solver
while err  > tol
    
    Uold = U;
    for i = 1 : size(V,1)
            [U,its] =  QuasiConvex2D_v2(U,V(i,1),V(i,2),e);
%             Nit = Nit + its;
            
            if i>=3 %unnecessary to sweep on rotated grids for (1,0) and 
                %(0,1) since they're orthogonal to each other.
                Ur = rot90(U);
                [Ur,its] = QuasiConvex2D_v2(Ur,V(i,1),V(i,2),e);
                U = rot90(Ur,-1);
%                 Nit = Nit + its;
            end
            
            if display
                info(maxwidth,err,Nit,V(i,1),V(i,2))
            end
    end
    iterations = iterations + 1;
    Nit = Nit + 1;
    err = norm(U(:)-Uold(:),inf);
end

if display
    info(maxwidth,err,Nit,V(i,1),V(i,2))
end
if e > 0
   gmin = min(g(:));
   U = max(U,gmin);
end

end

function info(maxwidth,err,Nit,v1,v2)
disp(['max width = ', num2str(maxwidth), ',  err = ', num2str(err),...
    ', #Its = ', num2str(Nit), ' , Direction = (', num2str(v1), ',', num2str(v2),')'] )
end