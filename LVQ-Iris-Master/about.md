Variants

Three other variants namely LVQ2, LVQ2.1 and LVQ3 have been developed by Kohonen. Complexity in all these three variants, due to the concept that the winner as well as the runner-up unit will learn, is more than in LVQ.

LVQ2

As discussed, the concept of other variants of LVQ above, the condition of LVQ2 is formed by window. This window will be based on the following parameters −

x − the current input vector

yc − the reference vector closest to x

yr − the other reference vector, which is next closest to x

dc − the distance from x to yc

dr − the distance from x to yr

The input vector x falls in the window, if

dc/dr > 1−θ and dr/dc > 1+θ
Here, θ is the number of training samples.

Updating can be done with the following formula −

yc(t+1)=yc(t)+α(t)[x(t)−yc(t)] --belongs to different class

yr(t+1)=yr(t)+α(t)[x(t)−yr(t)] --belongs to same class

Here α is the learning rate.


LVQ2.1

In LVQ2.1, we will take the two closest vectors namely yc1 and yc2 and the condition for window is as follows −

Min[dc1/dc2,dc2/dc1]>(1−θ)

Max[dc1/dc2,dc2/dc1]<(1+θ)

Updating can be done with the following formula −

yc1(t+1)=yc1(t)+α(t)[x(t)−yc1(t)] belongs to different class

yc2(t+1)=yc2(t)+α(t)[x(t)−yc2(t)] belongs to sameclass

Here, α is the learning rate.


LVQ3.0

In LVQ3, we will take the two closest vectors namely yc1 and yc2 and the condition for window is as follows −

Min[dc1/dc2,dc2/dc1]>(1−θ)(1+θ)

Updating can be done with the following formula −

yc1(t+1)=yc1(t)+β(t)[x(t)−yc1(t)] --belongs to different class

yc2(t+1)=yc2(t)+β(t)[x(t)−yc2(t)]  --belongs to same class

Here β is the multiple of the learning rate α and  β=mα(t)
