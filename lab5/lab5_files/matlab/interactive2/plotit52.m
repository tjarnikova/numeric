%  $Id: plotit5.m,v 1.1 2002/01/09 23:32:59 phil Exp $
outputFile='outfile.csv';
outData=importdata(outputFile)
figure(1)
clf
plot (outData.data(:,1),outData.data(:,2))
legend ('neutral daisies')
title('interactive 2');
xlabel('time');
ylabel('daisy concentration');
