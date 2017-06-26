%% Description - QCE along lines
% Performs the one-dimensional line solver along the vector (kc,kr).
%% Function
function [QCE, Nit] = QuasiConvex2D(U,kr,kc,e)

n = size(U,1);
h = 2/(n-1); %assuming computational domain is [-1,1]^2
%kr = height of vector
%kc = length of vector
kc = kc + 1; %add 1 to sync with index in matlab
kr = kr + 1;
U1 = U;
U2 = rot90(U,2);
Nit = 0;
if (kr-1) ~= 0
    j = kc : n;
    for i = kr : n
        U1(i,j) = min(U1(i,j),U1(i-(kr-1),j-(kc-1)) - e*h);
        U2(i,j) = min(U2(i,j),U2(i-(kr-1),j-(kc-1)) - e*h);
        Nit = Nit+1;
    end
else
    i = kr : n;
    for j = kc : n
        U1(i,j) = min(U1(i,j),U1(i-(kr-1),j-(kc-1)) - e*h);
        U2(i,j) = min(U2(i,j),U2(i-(kr-1),j-(kc-1)) - e*h);
        Nit = Nit+1;
    end
end
U2 = rot90(U2,-2);
QCE = max(U1,U2);
end     