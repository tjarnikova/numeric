function f=derivs5(y,t)
  global temp_w;
  global temp_b;
  global albedo_p;
  global coeff;
  if (nargin ~= 2)
    usage ('derivs ( y, t )');
end
  x = 1.0 - y(1) - y(2);        
  albedo_p = x*coeff.albedo_ground + y(1)*coeff.albedo_white + y(2)*coeff.albedo_black;    
  Te_4 = coeff.S0/4.0*coeff.L*(1.0 - albedo_p)/coeff.sigma;
  eta = coeff.R*coeff.S0/(4.0*coeff.sigma);
  temp_b = (eta*(albedo_p - coeff.albedo_black) + Te_4)^0.25;
  temp_w = (eta*(albedo_p - coeff.albedo_white) + Te_4)^0.25;

  if(temp_b >= 277.5 & temp_b <= 312.5) 
    beta_b= 1.0 - 0.003265*(295.0 - temp_b)^2.0;
  else
    beta_b=0.0;
end
  if(temp_w >= 277.5  & temp_w <= 312.5) 
    beta_w= 1.0 - 0.003265*(295.0 - temp_w)^2.0;
  else
    beta_w=0.0;
end
  f=ones([1,2]); %create a 1 x 2 element vector to hold the derivitive
  f(1) = y(1)*(beta_w*x - coeff.chi);
  f(2) = y(2)*(beta_b*x - coeff.chi);
