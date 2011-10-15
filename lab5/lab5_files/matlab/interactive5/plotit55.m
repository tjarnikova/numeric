%
%
outputFile='outputFile.csv';
outData=importdata(outputFile)
time = outData.data(:,1);
exact = time + exp(-time);
figure(1)
clf
plot(time,outData.data(:,2),'b-')
hold on
plot(time,exact,'r+') 
title('Interactive 5')
legend ('Numerical','Exact','location','northwest')
xlabel('time');
ylabel('Temperature');
hold off
figure(2)
clf;
realestError = outData.data(:,2)-exact;
plot (time,outData.data(:,3),time,realestError), ...
    title('Error');
%ylim([0 2])
legend ('estimated','actual')
xlabel('time');
ylabel('Error');
