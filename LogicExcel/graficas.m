canal_0 = Channel0(35721:490280);
canal_1 = Channel1(35721:490280);
canal_2 = Channel2(35721:490280);
canal_3 = Channel3(35721:490280);
canal_4 = Channel4(35721:490280);
canal_5 = Channel5(35721:490280);
canal_6 = Channel6(35721:490280);
canal_7 = Channel7(35721:490280);

m = 65536/227280;
t = (0:227280-1)*m; % Vector de tiempo
p = flip( t , 2 );
t1 = floor(t);
p1 = floor(p);
bits = [t1,p1]';

plot(canal_7);
hold on
plot(canal_6);
hold on
plot(canal_5);
hold on
plot(canal_4);
hold on
plot(canal_3);
hold on
plot(canal_2);
hold on
plot(canal_1);
hold on
plot(canal_0);
xticks([0 45456 90912 136368 181824 227280 272736 318192 363648 409104 454560]);
xticklabels({bits(1),bits(45456),bits(90912),bits(136368),bits(181824),bits(227280),bits(272736),bits(318192),bits(363648),bits(409104),bits(454560)});
xlim([0 454560])
xlabel('BITS');
ylabel('VOLTIOS');



