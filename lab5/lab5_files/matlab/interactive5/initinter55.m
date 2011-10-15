function [coeff,time,y,fid] = initinter55
% function to initialize variable for interactive example on page 4

time.tStart = 0.;
time.tEnd = 10.;
time.dt = .8;
coeff.c1 = -1.;
coeff.c2 = 1.;
coeff.c3 = 1.;
y(1) = 1;
y(2) = 0;
fid=fopen('outputFile.csv','w');

 
 
