function f=timeloop55(coeff,tStart,tEnd,dt,yinit,fid)
  
  [done,nVars]=size(yinit); % done is an unused variable.
  t=tStart;
  y=yinit;
  num=0;
  fprintf(fid,'time;yval;yerror\n');
  while(t < tEnd)
     [y,yerror,t]=step55(coeff,y,t,dt);
     fprintf('%s \n','----time temp ----   ');
    fprintf('%10.4f %10.4f \n',t,y(1));
    fprintf('%s \n',' ------stepsize, estError ');
    fprintf('%10.4f %10.4e \n',dt,yerror(1));
    fprintf(fid,'%g;%g;%g\n',t,y(1),yerror(1));
  end
  f=1;
