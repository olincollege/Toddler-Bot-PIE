function simulate_toddler_robot()
    figure;
    s_initial = calculate_current_position(pi/6, pi/6, 0, true); hold on
    s_final = calculate_next_position(1900, -600);
    axis equal
    s_diff = s_final - s_initial
    s_error = calculate_position_error(pi/720)
end

function s = calculate_current_position(theta_l, theta_r, phi, showError)
    % set default val for showError
    if nargin == 3
        showError = false;
    end

    % define constants
    w = 157.48;
    h = 40.64;
    x_end = 2000; % right anchor position
    winch_to_marker_dist = sqrt(h^2 + w^2/4);
    winch_to_marker_angle = atan2(h, w/2);
    
    % calculate string lengths
    A = [-sin(theta_l), sin(theta_r); cos(theta_l), cos(theta_r)];
    b = [w*sin(phi); x_end - w*cos(phi)];
    s = A\b;
    
    % calculate left winch position
    x_l = s(1)*cos(theta_l);
    y_l = -s(1)*sin(theta_l);

    % calculate marker position
    x = x_l + cos(phi + winch_to_marker_angle)*winch_to_marker_dist;
    y = y_l - sin(phi + winch_to_marker_angle)*winch_to_marker_dist;

    % plot positions
    x_r = x_end - s(2)*cos(theta_r);
    y_r = -s(2)*sin(theta_r);
    plot([0, x_end, x_l, x_r, x], [0, 0, y_l, y_r, y], 'r.', MarkerSize=10); hold on;
    plot([0, x_l], [0, y_l], 'r')
    plot([x_end, x_r], [0, y_r], 'r')
    if (showError)
        drawOval(x_l, y_l, 10, 5)
        drawOval(x_r, y_r, 10, 5)
        drawOval(x, y, 10, 5)
    end
    axis([0, 2000, -2000, 0])
end

function s = calculate_next_position(x, y)
    % define constants
    g = 9.81*1e3;
    k = 1e2;
    w = 157.48;
    h = 40.64;
    x_end = 2000; % right anchor position
    y_max = 2000;
    winch_to_marker_dist = sqrt(h^2 + w^2/4);
    winch_to_marker_angle = atan2(h, w/2);

    % define symbolic position expressions
    syms phi
    x_l = x - cos(phi + winch_to_marker_angle)*winch_to_marker_dist;
    y_l = y + sin(phi + winch_to_marker_angle)*winch_to_marker_dist;
    x_r = x_l + w*cos(phi);
    y_r = y_l - w*sin(phi);

    % define symbolic potential energy expressions
    PE_x = k*0.5*(x_l^2 + (x_end - x_r)^2);
    PE_y = k*0.5*((y_l + y_max)^2 + (y_r + y_max)^2) - g*(y_l + y_r + 2*y_max);
    PE = PE_x + PE_y;
    
    % define and find root of derivative of potential energy with respect to phi
    dPE = diff(PE);
    tilt = double(vpasolve(dPE, 0));

    % define other positions based on tilt
    x_l_real = subs(x_l, tilt);
    x_r_real = subs(x_r, tilt);
    y_l_real = subs(y_l, tilt);
    y_r_real = subs(y_r, tilt);

    % define string lengths
    s_l = sqrt(x_l_real^2 + y_l_real^2);
    s_r = sqrt((x_end-x_r_real)^2 + y_r_real^2);
    s = double([s_l; s_r]);

    % plot results
    plot([0, x_end, x_l_real, x_r_real, x], [0, 0, y_l_real, y_r_real, y], 'r.', MarkerSize=10); hold on;
    plot([0, x_l_real], [0, y_l_real], 'r')
    plot([x_end, x_r_real], [0, y_r_real], 'r')
    axis([0, 2000, -2000, 0]) 
end

function s_error = calculate_position_error(error)
    figure
    s_actual = calculate_current_position(pi/6, pi/6, 0);
    s_pp = calculate_current_position(pi/6+error, pi/6+error, 0); hold on
    s_pm = calculate_current_position(pi/6+error, pi/6-error, 0);
    s_mp = calculate_current_position(pi/6-error, pi/6+error, 0);
    s_mm = calculate_current_position(pi/6-error, pi/6-error, 0);
    axis equal

    s_vals = [s_actual s_pp s_pm s_mp s_mm];
    s_error = (max(s_vals,[],2) - min(s_vals,[],2))./2;
end

function drawOval(xc, yc, xe, ye)
    th = 0:pi/50:2*pi;
    xunit = xe*cos(th) + xc;
    yunit = ye*sin(th) + yc;
    plot(xunit, yunit, 'b');
end