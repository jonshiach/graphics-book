filename = '../images/exercise_15.gif';
output = '../images/exercise_15_v2.gif';
delay= 0.03;

frames = numel(imfinfo(filename));
for i = 1:frames
    disp("Working on frame " + i + " out of " + frames)

    [I, map] = imread(filename, i);

    if i==1
        imwrite(I,map, output, 'gif', 'DelayTime', delay,'LoopCount',inf); %save file output
    else
        imwrite(I, output, 'gif','WriteMode', 'append', 'DelayTime', delay); %save file output
    end
end