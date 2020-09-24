% PHENOCAM correction
% Author: Niklas Boke Ol�n (niklas.boke_olen@cec.lu.se)
% Version: 733250.03649467591
%--------------------------------------------------------------------------
% This scripts corrects movment in phenocam images by using
% 1) horizontal horizon adjustment
% 2) matching a feature to move the image in x-y axis


clear all
clc

close all

pic_folder = 'pictures/';
out_folder = 'pictures/corrected/';
filelist = dir([ pic_folder '*.jpg']);


filename = [pic_folder filelist(1).name];
im1 = imread(filename);  im1(1820:1944,:,:)=[];
new_filename = [out_folder 'cor_' filelist(1).name];
imwrite(im1,new_filename);


% uncomment below to select matching feature..
% trunk = imcrop(im1); %skapar en interaktiv bild som man kan redigera?
% imwrite(trunk,[out_folder 'trunk_matching_part.jpg'])

trunk = imread([pic_folder 'trunk_matching_part.jpg']);
%find location in frist image
I = im1;
J = trunk;
c = normxcorr2(J(:,:,1),I(:,:,1)); %kors-korrelerar och hittar var två bilder stämmer överens
[max_c, imax] = max(abs(c(:)));
[ypeak, xpeak] = ind2sub(size(c),imax(1)); %gör om till subscrifter ??? läs på om detta
corr_offset = [(xpeak-size(J,2)) (ypeak-size(J,1))]; %räknar ut offset kanske

x = corr_offset(1);
y = corr_offset(2);


%%

i = 2; % replace with for loop to run over multiple images

disp([datestr(now) ' -- i=' num2str(i)]) %display date
filename = [pic_folder filelist(i).name];
cor_filename = [out_folder 'cor_' filelist(i).name];
if exist(cor_filename,'file')~=2 %%if output file exist skip it

    im2 = imread(filename);  im2(1820:1944,:,:)=[];
    I = horizont_horizontal(im2); %här roterar man horistonten

    J = trunk;
    c = normxcorr2(J(:,:,1),I(:,:,1)); %hitta correlation
    [max_c, imax] = max(abs(c(:)));
    [ypeak, xpeak] = ind2sub(size(c),imax(1));
    corr_offset = [(xpeak-size(J,2)) (ypeak-size(J,1))];
    x1 = corr_offset(1);
    y1 = corr_offset(2);



    % Show figure
    figure(1); subplot(2,2,1); imshow(im2); hold on;
    rectangle('position',[x y length(J(1,:,1)) length(J(:,1,1))],...
        'edgecolor','g','linewidth',2); title('Original')
    hold off
    subplot(2,2,2); imshow(I); hold on;
    rectangle('position',[x1 y1 length(J(1,:,1)) length(J(:,1,1))],...
        'edgecolor','r','linewidth',2);
    rectangle('position',[x y length(J(1,:,1)) length(J(:,1,1))],...
        'edgecolor','g','linewidth',2); title('horizontal horizont and match')
    hold off
    subplot(2,2,3); imshow(im1); hold on;
    rectangle('position',[x y length(J(1,:,1)) length(J(:,1,1))],...
        'edgecolor','g','linewidth',2); title('Target')
    hold off



    xdiff = x-x1;
    ydiff = y - y1;
    % move image to match the found corner of rectangle.
    for layer=1:3
        A = I(:,:,layer);
        s = [abs(ydiff) abs(xdiff) ];
        A1 = padarray(A,s);
        A2 = circshift(A1,[ydiff xdiff]);
        A3 = A2(1+s(1):end-s(1),1+s(2):end-s(2));
        I(:,:,layer)= A3;
    end

    imwrite(I,cor_filename);

    % add the final result to fig
    subplot(2,2,4); imshow(I); hold on;
    rectangle('position',[x y length(J(1,:,1)) length(J(:,1,1))],...
        'edgecolor','g','linewidth',2); title('Result')
    hold off



end
