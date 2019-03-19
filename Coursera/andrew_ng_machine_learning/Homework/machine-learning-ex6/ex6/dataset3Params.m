function [C, sigma] = dataset3Params(X, y, Xval, yval)
%DATASET3PARAMS returns your choice of C and sigma for Part 3 of the exercise
%where you select the optimal (C, sigma) learning parameters to use for SVM
%with RBF kernel
%   [C, sigma] = DATASET3PARAMS(X, y, Xval, yval) returns your choice of C and 
%   sigma. You should complete this function to return the optimal C and 
%   sigma based on a cross-validation set.
%

% You need to return the following variables correctly.
C = 1;
sigma = 0.3;

% ====================== YOUR CODE HERE ======================
% Instructions: Fill in this function to return the optimal C and sigma
%               learning parameters found using the cross validation set.
%               You can use svmPredict to predict the labels on the cross
%               validation set. For example, 
%                   predictions = svmPredict(model, Xval);
%               will return the predictions on the cross validation set.
%
%  Note: You can compute the prediction error using 
%        mean(double(predictions ~= yval))
%

testC = [0.001, 0.01, 0.1, 1, 10];
minError = 10^5;
FinalC = C;
FinalSigma = sigma;

for i=1:size(testC,2),
	for j=1:size(testC,2),
		C = testC(i); sigma = testC(j);
		model = svmTrain(X, y, C, @(x1, x2) gaussianKernel(x1, x2, sigma));
		predictions = svmPredict(model, Xval);
		err = mean(double(predictions ~= yval));
		if err < minError,
			FinalC = C;
			FinalSigma = sigma;
			minError = err;
		end
	end
end

C = FinalC; sigma = FinalSigma;





% =========================================================================

end
