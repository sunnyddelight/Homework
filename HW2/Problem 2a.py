__author__ = 'Sunny'
freq=[8.167,1.492,2.782,4.253,12.702,2.228,2.015,6.094,6.996,0.153,.772,4.025,2.406,6.749,7.507,1.929,.095,5.987,6.327,9.056,2.758,0.978,2.360,.150,1.974,0.074]
sum=0
count=0
for val in freq:
    sum+=(val/100.0-1/26.0)**2
print sum/26