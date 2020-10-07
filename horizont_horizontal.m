function [rot_img] = horizont_horizontal(rgb_img)
%horizont_horizontal
%Rotates rbg images to make horizont horizontal.

I2 = double(rgb_img(:,:,3)); %representerar bilden i siffror från 0 till 1
classType = class(rgb_img(:,:,3)); %numrerar ytor som är samma
scalingFactor = double(intmax(classType));
I2 = I2/scalingFactor;


sky = (I2>(mean(mean(I2))/0.8)); %markera ut det som äe himmel
CC = bwconncomp(sky); %combinerar alla med samma nummer till en?
numPixels = cellfun(@numel,CC.PixelIdxList); %applicerar en function på varje cell
 
idx = numPixels<20000; %going through all the bwconncomp
for i=1:length(idx)
    if idx(i)
        sky(CC.PixelIdxList{i}) = 0; %sätter något till 0? Tar förmoldigen bort himmelen från beräkningen
    end
end

sky(1200:length(sky(:,1,1)),:,:)=0; % take bottom third out of account %ingen aning

hedge = vision.EdgeDetector; %hitta kanter på saker och ting och markera dem som linjer
hhoughtrans = vision.HoughTransform(pi/360,'ThetaRhoOutputPort', true); %hittar alla linjer?
hfindmax = vision.LocalMaximaFinder(1,	'HoughMatrixInput', true); %hittar den längsta linjen
 hhoughlines = vision.HoughLines('SineComputation','Trigonometric function');



BW = step(hedge, double(sky)); %plottar någonting
[ht, theta, rho] = step(hhoughtrans, BW); %delar in ploten i en matris
idx = step(hfindmax, ht);
linepts = step(hhoughlines, theta(idx(1)), rho(idx(2)), sky);

%Figures
% imshow(rgb_img); hold on;
% line(linepts([1 3])-1, linepts([2 4])-1,'color',[1 1 0]);


 x=double(linepts([1 3]));
 y=double(linepts([2 4]));



 slope=(y(1)-y(2))/(x(1)-x(2));

 w = atand(0) - atand(slope);  %clockwise rotation angle in degrees

rot_img = imrotate(rgb_img,-w,'crop');


end
