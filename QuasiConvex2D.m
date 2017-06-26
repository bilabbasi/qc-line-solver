%% Function
function QCE = QuasiConvex2D(g,kr,kc,e)
%% Description - (kr,kc)-QCE
%------------------------------------------------------------------------%
%     Returns the quasiconvex envelope of g. It is assumed that the
%     computational domain is a uniform partition (with spatial resolution
%     h) of the box [-1,1]^2.
% 
%     Parameters
%     ----------
%     g       : Obstacle
%     (kr,kc) : Line along which quasiconvex envelope will be computed
%     e       : e used to generate robustly quasiconvex envelopes (e>0)
%
%     Returns
%     -------
%     QCE : (e-Robustly) (kr,kc)-Quasiconvex envelope along 
%------------------------------------------------------------------------%
n = size(g,1);
h = 2/(n-1); %assuming computational domain is [-1,1]^2
kc = kc + 1; %add 1 to sync with index in matlab
kr = kr + 1;
U1 = g;
U2 = rot90(g,2);
if (kr-1) ~= 0
    j = kc : n;
    for i = kr : n
        U1(i,j) = min(U1(i,j),U1(i-(kr-1),j-(kc-1)) - e*h);
        U2(i,j) = min(U2(i,j),U2(i-(kr-1),j-(kc-1)) - e*h);
    end
else
    i = kr : n;
    for j = kc : n
        U1(i,j) = min(U1(i,j),U1(i-(kr-1),j-(kc-1)) - e*h);
        U2(i,j) = min(U2(i,j),U2(i-(kr-1),j-(kc-1)) - e*h);
    end
end
U2 = rot90(U2,-2);
QCE = max(U1,U2);
end     