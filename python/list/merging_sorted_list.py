class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        index1=0
        index2=0
        nums1_save=nums1[:m]
        print (nums1_save)
        while index1<m and index2 <n:
            if nums1_save[index1]<= nums2[index2]:
                print ('nums1_save[index1]',nums1_save[index1])
                print ('nums2[index2]',nums2[index2])
                nums1[index1+index2]=nums1_save[index1]
                print ('nums1 after replacement is ',nums1)
                index1+=1
            else:
                print ('nums1_save[index1] in index 2 case ',nums1_save[index1])
                print ('nums2[index2] in index 2 case',nums2[index2])
                nums1[index1+index2]=nums2[index2]
                print ('nums1 after replacement is in index2 case is  ',nums1)
                index2+=1
        print (nums1)
        if index1==m:
            nums1[index1+index2:]=nums2[index2:]
        if index2==n:
            nums1[index1+index2:]=nums1_save[index1:]
        return nums1