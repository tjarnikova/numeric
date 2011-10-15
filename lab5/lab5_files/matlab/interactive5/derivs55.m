function f=derivs55(coeff, y, time)
  if (nargin ~= 3)
    usage ('derivs (coeff, y, time )');
end
  f=ones([1,2]); %create a 1 x 2 element vector to hold the derivitive
  f(1)=coeff.c1*y(1)+coeff.c2*time+coeff.c3;
  f(2)= 0.;
  fprintf('\n +++ in derivs55: %g;%g;%g\n',y(1),time,f(1));

