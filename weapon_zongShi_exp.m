%宗室被动期望%
a = 0.08;
%a0为初始暴击几率
for a0 = linspace(0.4,0.8,5)
    n = min(5,floor((1-a0)/a));
    sum = 0;
    for i = 0:n
        sum = sum + a0+i*a/(i+1);
    end
    exp = sum/(n+1);
    fprintf("exp:%.3f sum:%.3f a0:%.3f n:%d\n",exp-a0,sum,a0,n);
end
fprintf("\n");