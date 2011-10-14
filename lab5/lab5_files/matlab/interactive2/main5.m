%Id: main5.m,v 1.1 2002/01/09 23:32:59 phil Exp $
% Global variables:

%Cash-Karp init
global  a;
global  c1;
global  c2;
global  b;
global  adapt;
%interesting output variables
global  temp_w;
global  temp_b;
global  albedo_p;
%physical coefficients
global  coeff;

[time,yinit,fid]=initcoeffs5;
errno=timeloop5(time.tStart,time.tEnd,time.dt,yinit,fid)
fclose(fid);
