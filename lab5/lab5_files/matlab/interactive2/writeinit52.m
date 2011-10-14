%$Id: writeinit5.m,v 1.1 2002/01/09 23:32:59 phil Exp $
userVars= [5.67e-8,     3668.0,      1.3,     0.12,          0.3,       0.5,              0.5,            0.5];
%userNames= ['sigma';    'SO   ';     'L    '; '  R  ';      'chi  ';    'albwh'; 'albbk';  'albgd'];
timeVars=[0.1 ,           0. ,      50.];
%timeNames=['dt    ';   'tStart';  'tEnd '];   
adaptVars=[  2.e3,         1e-5,     1e-5 ,  .9 ,      .1 ,          .5    ,          .1 ,        5 ,         60];
%adaptNames=['maxSteps';  'ATOL';   'RTOL';  'S';   'dtFailMin';  'dtFailMax';  'dtPassMin';  'dtPassMax';  'maxFail'];
initVars=[  0.2,  0.];
%initNames=['whiteConc';  'blackConc';];
outputFile='outfile.csv';
inputVersion='$Id: writeinit5.m,v 1.1 2002/01/09 23:32:59 phil Exp $';
save  indata userVars timeVars adaptVars initVars outputFile inputVersion;
