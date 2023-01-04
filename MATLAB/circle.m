function h = circle(cx, cy, r, colour)

theta = 0 : pi / 200 : 2 * pi;
x = cx + r * cos(theta);
y = cy + r * sin(theta);
h = plot(x, y, color=colour);

end