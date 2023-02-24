clc
clear all

% Define polygon vertices and colour
X = [2, 9, 8, 6, 4];
Y = [9, 9, 4, 7, 2];
colour = [153 ; 204 ; 255] / 255;

% Initialise raster array
Nx = 10;
Ny = 10;
img = ones(Ny, Nx, 3);

% Draw polygon
img = drawpolygon(img, X, Y, colour);

function R = drawpolygon(R, X, Y, colour)

% Generate edge table
n = length(X);
ET = [];
for i = 1 : n
    j = 1 + mod(i, n);
    if Y(i) < Y(j)
        imin = i;
        imax = j;
    elseif Y(i) > Y(j)
        imin = j;
        imax = i;
    else
        continue
    end

    dx = X(imin) - X(imax);
    dy = Y(imin) - Y(imax);
    if dx > 0
        xstep = -1;
    elseif dx < 0
        xstep = 1;
    end
    ET = [ET ; X(imin), 0, xstep, abs(dx), abs(dy), Y(imin), Y(imax), i ];
end

printET(ET, 'ET')

% Loop through scanlines
y = min(Y);
AET = [];
n = 1;
while isempty(ET) == 0 || isempty(AET) == 0
    
    % Move edges from ET to AET
    i = 1;
    while i <= size(ET,1)
        if ET(i,6) == y
            AET = [ AET ; ET(i,:) ];
            ET(i,:) = [];
        else
            i = i + 1;
        end
    end
    fprintf('\ny = %1i\n', y)
    printET(ET, 'ET')
    printET(AET, 'AET')

    % Sort AET by x value
    sortedAET = sortrows(AET, 1);
    if ~isequal(AET,sortedAET)
        AET = sortedAET;
        fprintf('\nSort AET\n')
        printET(AET, 'AET')
    end

    % Fill scanline
    i = 1;
    fprintf('\nFill pixels ')
    while i < size(AET,1)
        fprintf('(%1i,%1i) to (%1i,%1i), ', AET(i,1), y, AET(i+1,1), y)
        for x = AET(i,1) : AET(i+1,1)
            R(y,x,:) = colour;
        end
        i = i + 2;
    end

    % Remove edges from AET
    i = 1;
    while i <= size(AET,1)
        
        % Update N and x
        AET(i,2) = AET(i,2) + AET(i,4);
        while AET(i,2) >= AET(i,5)
            AET(i,2) = AET(i,2) - AET(i,5);
            AET(i,1) = AET(i,1) + AET(i,3);
        end

        % Remove edges from AET whose ymax = y
        if AET(i,7) == y
            AET(i,:) = [];
        else
            i = i + 1;
        end    
    end
    if size(AET,1) > 0
        fprintf('\n\nUpdate AET\n')
        printET(ET, 'ET')
        printET(AET, 'AET')
    end

    % Incremement y
    y = y + 1;

    figure
    image(R)
    pixelgrid(R)
    hold on
    plot([X, X(1)], [Y, Y(1)], 'k-', LineWidth=2) 
    hold off
    axis equal tight
    xticks(0:10)
    filename = sprintf('../images/scanline_example_%1i.png', n);
    exportgraphics(gcf,filename,'Resolution', 300)
    n = n + 1;
    
end

end

function printET(ET, label)

if size(ET, 1) == 0
    return
end
fprintf('\n%s\n', label)
fprintf('       x    N  xstep  dx   dy  ymin ymax \n')
for i = 1 : size(ET, 1)
    fprintf('e%1i : [ %1i %4i %4i %4i %4i %4i %4i  ]\n', ET(i,end), ET(i,1:7))
end

end

function pixelgrid(img)

[Ny, Nx, ~] = size(img);
for i = 1 : Ny + 1
    yline(i-0.5, Color='k', LineWidth=1)
end
for i = 1 : Nx + 1
    xline(i-0.5, Color='k', LineWidth=1)
end

end