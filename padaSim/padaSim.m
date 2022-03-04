clear all
close all
clc

% Start-Up Behavior
fprintf("\nRunning the PADA Fall Guys Simulator\n\n");

% Constants
rho = 1.255; % kg/m^3
m = 0.453; % kg
L = .305; % m
Cl = 1.5; % unitless ***NEEDS TO BE FIXED***
Cd = .0354; % unitless
g = 9.81; % m/s^2
tList = linspace(0, 30, 1000);
dt = tList(2) - tList(1);

% Dummy Initial values
y0 = 10; % m
u0 = 0.1; % m/s
v0 = 0; % m/s
alpha0 = 0; % RADIANS

% Variables
r = [0; y0]; % position
vel = [ u0; v0 ]; % vel vector
dv = [0; 0]; % finite difference
alpha = 0; % pitch
iter = 0; % cuz matlab starts at 1 and updated at the beginning of the while loop later

% Variable Logs
rLog = zeros([2, 200]);
velLog = zeros([2, 200]);
alfLog = zeros([1, 200]);

% Force Functions
T = @(u, t, alf) 0*[ cos(alf); sin(alf)]; % Thrust
D = @(u, t, alf) (1/2)*rho*u*u*L*Cd*[ cos(alf); sin(alf)]; % Drag
L = @(u, t, alf) (1/2)*rho*u*u*L*Cl*[ -sin(alf); cos(alf)]; % Lift
G = [ 0; -m*g]; % Gravity

% Core Steps
while (r(2) > 0)
    % update active variables
    iter = iter + 1;
    u = vel(1);
    v = vel(2);
    alpha = atan(v/u);
    t = tList(iter);
    
    % calc dv using dv = dt*(sum(F)/m) & dr = v*dt
    dv = dt*( T(u,t,alpha) + L(u,t,alpha) + G - D(u,t,alpha) )/m;
    vel = vel + dv;
    r = dt*vel + r;
    
    % update logs
    rLog(:, iter) = r;
    velLog(:, iter) = vel;
    alfLog(:, iter) = alpha;
end

% Plots
hold on

% plot trajectory
figure(1)
plot(rLog(1,1:iter), rLog(2, 1:iter))
xlabel("Travelling distance [m]"); 
ylabel("Vertical Height [m]");
title("Fig 1: Flight Trajectory");
fprintf("The final distance reached is %2.2f m\n", r(1));

% plot velocity vs time
figure(2)



fprintf("\nEnd of simulation.\n\n");