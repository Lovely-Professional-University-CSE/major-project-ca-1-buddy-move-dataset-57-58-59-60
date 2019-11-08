LVQ2.1

In LVQ2.1, we will take the two closest vectors namely yc1 and yc2 and the condition for window is as follows −

Min[dc1/dc2,dc2/dc1]>(1−θ)

Max[dc1/dc2,dc2/dc1]<(1+θ)

Updating can be done with the following formula −

yc1(t+1)=yc1(t)+α(t)[x(t)−yc1(t)] #belongstodifferentclass

yc2(t+1)=yc2(t)+α(t)[x(t)−yc2(t)] #belongstosameclass

Here, α is the learning rate.
