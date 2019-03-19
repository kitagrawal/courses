%% Initialization
#clear ; close all; clc

%% Load Data
data = load('matrix-mod.txt');
X = data(:, 1:5); y = data(:, 6);
[p, q] = size(X);
X = [ones(p, 1) X];
#SAT vs ALL
y1 = y; y1(y1 != 0) = 1;
#UNSAT vs ALL
y2 = y; y2(y2 != 1) = 0;
#TIMEOUT vs ALL
y3 = y; y3(y3 != 2) = 0;
#EXCEPTION vs ALL
y4 = y; y4(y4 != 3) = 0;

%% ============ Part 2: Compute Cost and Gradient ============

%  Setup the data matrix appropriately, and add ones for the intercept term
trainf = X(1:500, :); trainl = y1(1:500, :);
[m, n] = size(trainf);

% Add intercept term to x and X_test

% Initialize fitting parameters
initial_theta = zeros(n, 1);

% Compute and display initial cost and gradient
[cost, grad] = costFunction(initial_theta, trainf, trainl);

fprintf('Cost at initial theta (zeros): %f\n', cost);
fprintf('Gradient at initial theta (zeros): \n');
fprintf(' %f \n', grad);

%% ============= Part 3: Optimizing using fminunc  =============

%  Set options for fminunc
options = optimset('GradObj', 'on', 'MaxIter', 400);

%  Run fminunc to obtain the optimal theta
%  This function will return theta and the cost 
[theta, cost] = ...
	fminunc(@(t)(costFunction(t, trainf, trainl)), initial_theta, options);

% Print theta to screen
fprintf('Cost at theta found by fminunc: %f\n', cost);
fprintf('theta: \n');
fprintf(' %f \n', theta);

% Plot Boundary
%plotDecisionBoundary(theta, X, y1);

% Put some labels 
%hold on;
% Labels and Legend
%xlabel('Exam 1 score')
%ylabel('Exam 2 score')

% Specified in plot order
%legend('Admitted', 'Not admitted')
%hold off;

%fprintf('\nProgram paused. Press enter to continue.\n');
%pause;

%% ============== Part 4: Predict and Accuracies ==============

% Compute accuracy on our training set
testf = X(501:end,:); testl = y1(501:end,:);
p = predict(theta, testf);

fprintf('Train Accuracy: %f\n', mean(double(p == testl)) * 100);
%fprintf('Expected accuracy (approx): 89.0\n');
%fprintf('\n');


