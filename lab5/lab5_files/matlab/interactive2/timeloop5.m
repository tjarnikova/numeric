function f=timeloop5(tStart,tEnd,dt,yinit,fid)
  global adapt;
  global temp_w;
  global temp_b;
  global albedo_p;
  [done,nVars]=size(yinit); % done is an dummy variable.
  oldt=tStart;
  t=tStart;
  errtest=0.0;
  yold=yinit;
  olddt=dt;
  y=yinit;
  num=0;
  badsteps=0;
  goodsteps=0;
  fprintf(fid,'time;neutral;neutral\n');
  while(t < tEnd)
    if(num > adapt.maxSteps)
      error('num > maxSteps');
  end
    goodStep=0;
    failSteps=0;
    while(~goodStep)
      if(failSteps > adapt.maxFail)
	error('failSteps > adapt.maxFail');
end
      [y,yerror,t]=step5(y,t,dt);
      errtest=0.;
      for i=1:nVars
	errtest = errtest + (yerror(i)/(adapt.ATOL + adapt.RTOL*abs(y(i))))^2.0;
end
      errtest = sqrt(errtest / nVars);
      dtChange = adapt.S*(1.0/errtest)^0.2;
      if (errtest > 1.0)
	if(dtChange > adapt.dtFailMax) 
	  dt = adapt.dtFailMax * dt;
	elseif (dtChange < adapt.dtFailMin) 
	  dt = adapt.dtFailMin * dt;
	else 
	  dt = dtChange * dt;
  end
	if (t+dt == t)
	  error('step smaller than machine precision');
  end
	failSteps=failSteps + 1;
	fprintf('%s\n','y=yold: timeloop');
	y = yold;
	t = oldt;
      else
	if (abs((1.0 - dtChange)) > adapt.dtPassMin)
	  if(dtChange > adapt.dtPassMax)
	    dtNew = adapt.dtPassMax * dt;
	  else
	    dtNew = dtChange * dt;
    end
	else
	  dtNew = dt;
  end
 	goodStep = 1;
	oldt = t;
	yold = y;
end
end
    if(olddt ~= dt)
      olddt = dt;
      badsteps=badsteps+1;
    else
      goodsteps=goodsteps+1;
  end
    if(t + dtNew > tEnd) 
      dt = tEnd - t;
    elseif(t + 2.0*dtNew > tEnd) 
      dt = (tEnd - t)/2.0;
    else
      dt = dtNew;
  end
    fprintf('\n%s','----time white black----   ');
    fprintf('%10.4f %10.4f %10.4f',t,y(1),y(2));
    fprintf('\n%s',' ------stepsize, estError ');
    fprintf('%10.4f %10.4e %10.4e\n',olddt,yerror(1),yerror(2));
    fprintf('\n%s\n%f %f %f\n','white, black temps (K), planet. albedo: ', temp_w,temp_b,albedo_p);
    fprintf(fid,'%g;%g;%g\n',t,y(1),y(2));
end
  fprintf('%d %s\n',goodsteps,' successful steps');
  fprintf('%d %s\n',badsteps,' failed steps');
  f=1;
