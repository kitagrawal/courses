function [J, grad] = costFunctionReg(theta, X, y, lambda)
%COSTFUNCTIONREG Compute cost and gradient for logistic regression with regularization
%   J = COSTFUNCTIONREG(theta, X, y, lambda) computes the cost of using
%   theta as the parameter for regularized logistic regression and the
%   gradient of the cost w.r.t. to the parameters. 

% Initialize some useful values
m = length(y); % number of training examples

% You need to return the following variables correctly 
J = 0;
grad = zeros(size(theta));

% ====================== YOUR CODE HERE ======================
% Instructions: Compute the cost of a particular choice of theta.
%               You should set J to the cost.
%               Compute the partial derivatives and set grad to the partial
%               derivatives of the cost w.r.t. each parameter in theta

%z = X*theta;
%h = 1 ./ (1 + e.^(-z));
h = sigmoid(X*theta);
errorr = h .- y; 
J = (1/m) * sum(-1*y .* log(h) - ((1-y) .* log(1 .- h))) + (lambda/(2*m))*sum(theta(2:length(theta)).^2);
grad(1) = [(1/m) * X'(1,:) * errorr] %theta_0 update 
grad(2:size(theta,1)) = [(1/m) * X'(2:size(X',1),:) * errorr] + [(lambda/m)*theta(2:size(theta,1),:)]; %theta_1 to theta_n updates with regularizer
% =============================================================

end
