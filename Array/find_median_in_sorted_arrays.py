class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        total=len(nums1)+len(nums2)
        A,B=nums1,nums2
        half=total//2
        if len(B)>len(A):
            A,B=B,A
        l,h=0,len(A)
        print('b',B)
        while True:
            i=(l+h)//2
            j=half-i-2
            Aleft=A[i] if i>=0 else float('-infinity')
            Aright=A[i+1] if (i+1)<len(A) else float('infinity')
            Bleft=B[j] if j>=0 else float('-infinity')
            print('j',j)
            Bright=B[j+1] if (j+1)<len(B) else float('infinity')
            if Aleft<=Bright and Aright>=Bleft:
                if total%2==0:
                    return (max(Aleft,Bleft)+min(Aright,Bright))/2
                else:
                    return min(Aright,Bright)
            elif Aleft>Bright:
                #l-=1
                h=i-1
            else:
                #h+=1
                l=i+1



arr1 =[]
arr2 =[1]
result=Solution()
print(result.findMedianSortedArrays(arr1,arr2))