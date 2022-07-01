canal_0 = Channel0(35721:490280);
canal_1 = Channel1(35721:490280);
canal_2 = Channel2(35721:490280);
canal_3 = Channel3(35721:490280);
canal_4 = Channel4(35721:490280);
canal_5 = Channel5(35721:490280);
canal_6 = Channel6(35721:490280);
canal_7 = Channel7(35721:490280);

m = 65536/(44480);
m1 = 65536/(45530);
t = (0:(44480)-1)*m; % Vector de tiempo
t1 = (0:(45530)-1)*m1; % Vector de tiempo
p = flip( t1 , 2 );
t1 = floor(t);
p1 = floor(p);
bits = [t1,p1]';

plot(Channel0);
hold on
plot(Channel1);
hold on
plot(Channel2);
hold on
plot(Channel3);
hold on
plot(canal_3);
hold on
plot(canal_2);
hold on
plot(canal_1);
hold on
plot(canal_0);

xticks([0 8896 17792 26688 35584 44480 53586 62692 71798 80904 90010]);
xticklabels({bits(1),bits(8896),bits(17792),bits(26688),bits(3584),bits(44480),bits(53586),bits(62692),bits(71798),bits(80904),bits(90010)});
xlim([0 90010])
xlabel('BITS');
ylabel('VOLTIOS');

%%

m = 65536/(44480);
m1 = 65536/(45530);
t = (0:(44480)-1)*m; % Vector de tiempo
t1 = (0:(45530)-1)*m1; % Vector de tiempo
p = flip( t1 , 2 );
t1 = floor(t);
p1 = floor(p);
bits = [t1,p1]';




figure(1)
yyaxis('right');
plot(Channel3);
ylabel('VOLTS');
hold on
grid on
yyaxis('left')
ylim([-5e-5,6e-5]);
plot(I_3);
ylabel('AMPERIOS');


xticks([0 8896 17792 26688 35584 44480 53586 62692 71798 80904 90010]);
xticklabels({bits(1),bits(8896),bits(17792),bits(26688),bits(3584),bits(44480),bits(53586),bits(62692),bits(71798),bits(80904),bits(90010)});
xlim([0 90010])
xlabel('BITS');



