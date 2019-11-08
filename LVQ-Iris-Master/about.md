LVQ3

In LVQ3, we will take the two closest vectors namely yc1 and yc2 and the condition for window is as follows −

Min[dc1/dc2,dc2/dc1]>(1−θ)(1+θ)


Updating can be done with the following formula −

yc1(t+1)=yc1(t)+β(t)[x(t)−yc1(t)] --belongs to different class

yc2(t+1)=yc2(t)+β(t)[x(t)−yc2(t)]  --belongs to same class

Here β is the multiple of the learning rate α and  β=mα(t)
