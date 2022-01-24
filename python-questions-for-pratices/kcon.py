def heler_kadane(arr,n):
    #print(n)
    max1=arr[0];
    max_point=arr[0];
    #print(arr[0])
    for i in range(1,n):
        max1=max(arr[i],max1+arr[i]);
        #print(max_point);
        max_point=max(max1,max_point);
        #print(max1)
    return max_point;

    
t=int(input());
for i in range(0,t):
    l=list(map(int,input().split()));
    n=l[0];
    k=l[1];
    arr=list(map(int,input().split()));
    arrb=[];
    if(k==1):
        maxsum=heler_kadane(arr,n);
    elif(k==2):
        for j in range(0,2*n):
            arrb.append(arr[j%n]);
        maxsum=heler_kadane(arrb,2*n);
    elif(k==3):
        for j in range(0,3*n):
            arrb.append(arr[j%n]);
        maxsum=heler_kadane(arrb,3*n);
    else:
        sum=0;
        for j in range(0,n):
            sum=sum+arr[j];
        for j in range(0,2*n):
            arrb.append(arr[j%n]);
        for j in range(0,k-3):
            arrb.append(sum);
        for j in range(0,n):
            arrb.append(arr[j]);
        #print(arrb)
        maxsum=heler_kadane(arrb,(k-3)+(3*n));


    #print(arrb)
    print(maxsum)
 
