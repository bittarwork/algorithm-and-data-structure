import random as r 
def max_pairwise_product (numbers):
    n = len(numbers) 
    if ( n >= 2 ): 
        numbers.sort()
        max1 = numbers[n-1]
        max2=numbers[n-2]
        return(max1*max2)
    elif(n==2) : 
        return (numbers[0]*numbers[1]) 
# def max_pairwise_product_slow(numbers):
#     n = len(numbers)
#     max_product = 0
#     for first in range(n):
#         for second in range(first + 1, n):
#             max_product = max(max_product,
#             numbers[first] * numbers[second])
#     return max_product
    

if __name__ == '__main__':
    # x = True 
    # while(x) :
    #     n = r.randint(2,2000)
    #     li = []
    #     for i in range (0 , n ): 
    #         x= r.randint(0,2000)
    #         li.append(x)
    #     maxfast  =  max_pairwise_product_faster (li)
    #     maxx = max_pairwise_product(li) 
    #     print (maxfast ," ", maxx)
    #     if (maxx != maxfast ) : x = False
    _ = int(input())
    input_numbers = list(map(int, input().split()))
    print(max_pairwise_product(input_numbers))


    
    
    
    
