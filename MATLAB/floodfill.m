function R = floodfill(R, x0, y0, target, replacement)

Q = [ x0, y0 ];
while isempty(Q) == 0
    pixel = Q(end,:);
    Q(end,:) = [];
    if R(pixel(2), pixel(1), 1) == target(1) && ...
            R(pixel(2), pixel(1), 2) == target(2) && ...
            R(pixel(2), pixel(1), 3) == target(3)
        R(pixel(2), pixel(1), :) = replacement;
        Q = [ Q ; 
            pixel(1) + 1, pixel(2) ; 
            pixel(1) - 1, pixel(2) ;
            pixel(1), pixel(2) + 1 ;
            pixel(1), pixel(2) - 1 ];
    end
end

end