function [time,yinit,fid]=initcoeffs5()
  global  a;
  global  c1;
  global  c2;
  global  b;
  global adapt
  global coeff
  load indata;
%
% initialize the Cash-Karp coefficients
% defined in the tableau in lab 4,
% section 3.5
%
  a = [.2, 0.3, 0.6, 1.0, 0.875];
  c1 = [37.0/378.0, 0.0, 250.0/621.0, 125.0/594.0, 0.0, 512.0/1771.0];
  c2= [2825.0/27648.0, 0.0, 18575.0/48384.0, 13525.0/55296.0, 277.0/14336.0, .25];
  b=ones(5);
  c2 = c1 - c2;
  b(1,1) =0.2; 
  b(2,1)= 3.0/40.0; 
  b(2,2)=9.0/40.0;
  b(3,1)=0.3; 
  b(3,2)=-0.9; 
  b(3,3)=1.2;
  b(4,1)=-11.0/54.0; 
  b(4,2)=2.5; 
  b(4,3)=-70.0/27.0; 
  b(4,4)=35.0/27.0;
  b(5,1)=1631.0/55296.0; 
  b(5,2)=175.0/512.0; 
  b(5,3)=575.0/13824.0;
  b(5,4)=44275.0/110592.0; 
  b(5,5)=253.0/4096.0;
%
% user coefficients for derivs routine
% defined in lab 5 Sections 3.4, 3.5 and
% appendix b
%
  coeff.sigma=userVars(1);
  coeff.S0=userVars(2);
  coeff.L=userVars(3);
  coeff.R=userVars(4);
  coeff.chi=userVars(5);
  coeff.albedo_white=userVars(6);
  coeff.albedo_black=userVars(7);
  coeff.albedo_ground=userVars(8);
  time.dt=timeVars(1);
  time.tStart=timeVars(2);
  time.tEnd=timeVars(3);
  adapt.maxSteps=adaptVars(1);
  adapt.ATOL=adaptVars(2);
  adapt.RTOL=adaptVars(3);
  adapt.S=adaptVars(4);
  adapt.dtFailMin=adaptVars(5);
  adapt.dtFailMax=adaptVars(6);
  adapt.dtPassMin=adaptVars(7);
  adapt.dtPassMax=adaptVars(8);
  adapt.maxFail=adaptVars(9);
  fid=fopen(outputFile,'w');
  if((initVars(1) + initVars(2)) > 1.)
    error('need white and black initial concentrations <= 1.');
end
  yinit=initVars;
  fprintf('\n%s\n\n','---Adaptive integration settings---');
  fprintf('%s\t %f\n','maxSteps: ',adapt.maxSteps);
  fprintf('%s\t\t %f\n','ATOL: ',adapt.ATOL);
  fprintf('%s\t\t %f\n','RTOL: ',adapt.RTOL);
  fprintf('%s\t\t %f\n','S: ',adapt.S);
  fprintf('%s\t %f\n','dtFailMin: ',adapt.dtFailMin);
  fprintf('%s\t %f\n','dtFailMax: ',adapt.dtFailMax);
  fprintf('%s\t %f\n','dtPassMin: ',adapt.dtPassMin);
  fprintf('%s\t %f\n','dtPassMax: ',adapt.dtPassMax);
  fprintf('%s\t %f\n','maxFail: ',adapt.maxFail);

  fprintf('\n%s\n\n','---Daisy world values---');
  fprintf('%s\t\t %g\n','sigma: ',coeff.sigma);
  fprintf('%s\t\t %f\n','S0: ',coeff.S0);
  fprintf('%s\t\t %f\n','L: ',coeff.L);
  fprintf('%s\t\t %f\n','R: ',coeff.R);
  fprintf('%s\t\t %f\n','chi: ',coeff.chi);
  fprintf('%s\t %f\n','albedo_white: ',coeff.albedo_white);
  fprintf('%s\t %f\n','albedo_black: ',coeff.albedo_black);
  fprintf('%s\t %f\n','albedo_ground: ',coeff.albedo_ground);

  fprintf('\n%s\n\n','---time values---');
  fprintf('%s\t %f\n','tStart: ',time.tStart);
  fprintf('%s\t\t %f\n','tEnd: ',time.tEnd);
  fprintf('%s\t\t %f\n','dt: ',time.dt);

  fprintf('\n%s\n\n','---initial conditions---');
  fprintf('%s\t %f\n','white daisies: ',yinit(1));
  fprintf('%s\t %f\n','black daisies: ',yinit(2));

