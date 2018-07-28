def subArraySum(arr, n, sum):

    for i in range(n):
        curr_sum = arr[i]


        j = i + 1
        while j <= n:

            if curr_sum == sum:

                print("between %d and %d" % (i, j - 1))

                return 1

            if curr_sum > sum or j == n:
                break

            curr_sum = curr_sum + arr[j]
            j += 1

    print("No subarray found")
    return 0


arr=[]

size = int(input("Please enter the size of array"))

for val in range(0,size):
    arr.append(int(input("Please enter the number : ")))

print(arr)

n=len(arr)

sum = int(input("Please enter the sum : "))

subArraySum(arr, n, sum)