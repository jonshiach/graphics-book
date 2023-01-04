function R = drawcircle(R, cx, cy, r, colour)

D = 5 - r ^ 2;
x = r;
y = 0;
while y <= x
    R(cy+y, cx+x, :) = colour;
    R(cy+y, cx-x, :) = colour;
    R(cy-y, cx+x, :) = colour;
    R(cy-y, cx-x, :) = colour;
    R(cy+x, cx+y, :) = colour;
    R(cy+x, cx-y, :) = colour;
    R(cy-x, cx+y, :) = colour;
    R(cy-x, cx-y, :) = colour;

    if D > 0
        D = D - 8 * x - 8;
        x = x - 1;
    end

    D = D + 8 * y + 12;
    y = y + 1;
end

end