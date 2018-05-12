close
clear
clc
%
load vbm

% chosen coordinates
x=100;
y=100;
z=100;

% normalizes the matrix
map=vbm/max(max(max(vbm)));

% creates the 3 planes
planoxy(:,:)=map(:,:,z);
planoxz(:,:)=map(:,y,:);
planoyz(:,:)=map(x,:,:);

% plots the image of a plane
imagesc (planoxz)
