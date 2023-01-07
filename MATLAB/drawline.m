function drawline(R, x0, y0, x1, y1, colour)

x = x0;
y = y0;
dx = abs(x1 - x0);
dy = abs(y1 - y0);
xstep = sign(x1 - x0);
ystep = sign(y1 - y0);

while true
    R(y, x, :) = colour;
    if x == x1 && y == y1
        return
    end
    E = 2 * D;
    if E >= -dy
        x = x + xstep;
        D = D - dy;
    end
    if E <= dx
        y = y + ystep;
        D = D + dx;
    end
end

end