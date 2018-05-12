close
clear
clc
%
load vbm

%variáveis do ponto escolhido
x=100;
y=100;
z=100;

%normaliz a matriz
map=vbm/max(max(max(vbm)));

%cria os 3 planos
planoxy(:,:)=map(:,:,z);
planoxz(:,:)=map(:,y,:);
planoyz(:,:)=map(x,:,:);

%plota a imagem de um plano
imagesc (planoxz)
