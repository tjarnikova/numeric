function [y,estError,t]=rkCKODE55(coeff,yold,told,dt)
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
  
  % set up arrays
  
  derivArray=zeros(6,length(yold));
  ynext=zeros([1,length(yold)]);
  bsum=zeros([1,length(yold)]);
  derivArray(1,:)=derivs55(coeff,yold,told);
  estError=zeros([1,length(yold)]);
  y=yold;
  for i=1:5
    bsum=0.;
    for j=1:i
      bsum=bsum + b(i,j)*derivArray(j,:);
    end
    y + dt*bsum;
    derivArray(i+1,:)=derivs55(coeff,y + dt*bsum,told + a(i)*dt);
    ynext = ynext + c1(i)*derivArray(i,:);
    estError = estError + c2(i)*derivArray(i,:);
end
  y = y + dt*(ynext + c1(6)*derivArray(6,:));
  estError =  dt*(estError + c2(6)*derivArray(6,:));
  t=told + dt;

  