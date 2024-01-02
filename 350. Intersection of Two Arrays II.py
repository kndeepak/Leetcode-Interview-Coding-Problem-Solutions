class Solution:
        def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]: 
           

            if len(nums1) > len(nums2):
                nums1, nums2 = nums2, nums1  # Ensure nums1 is the smaller array
            nums1.sort()
            result = []

            for num in nums1:
                left, right = 0, len(nums2) - 1
                while left <= right:
                    mid = (left + right) // 2
                    if nums2[mid] == num:
                        result.append(num)
                        nums2.pop(mid)  # Remove the found element from nums2
                        break
                    elif nums2[mid] < num:
                        left = mid + 1
                    else:
                        right = mid - 1

            return result
