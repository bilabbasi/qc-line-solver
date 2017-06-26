function [QCE,its] = ndim_linesolver(g,width,e,tol)
%% Description - Quasiconvex envelope in 2D
%------------------------------------------------------------------------%
%     Returns the quasiconvex envelope of g using the line solver (see ref 
%     below). It is assumed that the computational domain is a uniform
%     partition of [-1,1]^2.
% 
%     ref: https://arxiv.org/abs/1612.05584
%
%     Parameters
%     ----------
%     g     : Obstacle 
%     width : Width of direction set
%     e     : e used to generate robustly quasiconvex envelopes (e>0)
%     tol   : Tolerance used in fixed point iterations
%
%     Returns
%     -------
%     QCE : (e-Robustly) Quasiconvex envelope
%     its : Iterations required for convergence to tolerance
%------------------------------------------------------------------------%
%% set up
QCE = g;               %Initialization
err = inf;
V = gridvectors(width);%Returns set of grid directions with max width of width.
its = 0;
%% solver
while err  > tol
    
    Uold = QCE;
    for i = 1 : size(V,1)
            QCE =  QuasiConvex2D(QCE,V(i,1),V(i,2),e);            
            if i>=3 %unnecessary to sweep on rotated grids for (1,0) and 
                %(0,1) since they're orthogonal to each other.
                Ur = rot90(QCE);
                Ur = QuasiConvex2D(Ur,V(i,1),V(i,2),e);
                QCE = rot90(Ur,-1);
            end
    end
    its = its + 1;
    err = norm(QCE(:)-Uold(:),inf);
end

if e > 0
   gmin = min(g(:));
   QCE = max(QCE,gmin);
end

end