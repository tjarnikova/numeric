function [y,estError,t]=rkCKODE53(yold,told,dt)
  global c1;
  global c2;
  global a;
  global b;
  derivArray=zeros(6,length(yold));
  ynext=zeros([1,length(yold)]);
  bsum=zeros([1,length(yold)]);
  derivArray(1,:)=derivs53(yold,told);
  estError=zeros([1,length(yold)]);
  y=yold;
  for i=1:5
    bsum=0.;
    for j=1:i
      bsum=bsum + b(i,j)*derivArray(j,:);
  end
    derivArray(i+1,:)=derivs53(y + dt*bsum,told + a(i)*dt);
    ynext = ynext + c1(i)*derivArray(i,:);
    estError = estError + c2(i)*derivArray(i,:);
end
  y = y + dt*(ynext + c1(6)*derivArray(6,:));
  estError =  dt*(estError + c2(6)*derivArray(6,:));
  t=told + dt;
