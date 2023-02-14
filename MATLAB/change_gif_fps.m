[I map]=imread('../images/exercise_15.gif');
delay=0.03;
frame=size(I,4);
for i = 1:frame
    if i==1
        imwrite(I(:,:,:,i),map,'b.gif','gif', 'DelayTime', delay,'LoopCount',inf); %save file output
    else
        imwrite(I(:,:,:,i),'b.gif','gif','WriteMode', 'append', 'DelayTime', delay); %save file output
    end
end