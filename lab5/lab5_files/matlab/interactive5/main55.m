[coeff,time,yinit,fid]=initinter55;
fprintf('\n +++ in derivs55: y(1),time,f(1)');
errno=timeloop55(coeff,time.tStart,time.tEnd,time.dt,yinit,fid);
fclose(fid);
