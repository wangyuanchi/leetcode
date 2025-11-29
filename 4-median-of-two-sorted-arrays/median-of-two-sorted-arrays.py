class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total = len(nums1) + len(nums2)
        half = total // 2

        """
        Imagine the merged array with colour coded elements, then take the left half.
        The rightmost element in this left half can belong to either nums1 or nums2.
        WLOG, Assume it is in nums1. Then, we want to find this element in nums1 using binary search.
        More specifically, we want to find a split for nums1 between 0 and len(nums1) inclusive,
        where splitting at an index means nums1[index] would be splitted into the right side.
        This split is guranteed to exist.
        
        Let the split be at mid. Then:
        Left split of nums1: nums1[:mid]
        Left split of nums2: nums2[:half - mid]
        Let the value nums1[mid - 1] be A and num1[mid] be B and similarly for nums2.

        IMPORTANT:
        Suppose len(nums1) >> len(nums2) and mid goes right after the first loop.
        Then, indexes for nums2 will go out of bounds.
        We can deal with this by treating the array to have infinite size and -inf and inf values.
        This results in 3 possible value types for 1A, 1B, 2A and 2B each.
        It can be optimized to 2 value types by setting nums1 to be the array of smaller length.
        This can be verified by checking the edge cases where len(smaller) == 0 and len(smaller) == len(bigger)
        """
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        l, r = 0, len(nums1)

        while True: # Since we know we will definitely find the split
            mid = l + (r - l) // 2

            nums1A = nums1[mid - 1] if mid - 1 >= 0 else float("-inf")
            nums1B = nums1[mid] if mid < len(nums1) else float("inf")
            nums2A = nums2[half - mid - 1] if half - mid - 1 >= 0 else float("-inf")
            nums2B = nums2[half - mid] if half - mid < len(nums2) else float("inf")

            if nums1A <= nums2B and nums2A <= nums1B:
                if total % 2 == 0:
                    return (max(nums1A, nums2A) +
                            min(nums1B, nums2B)) / 2
                else:
                    return min(nums1B, nums2B)
            elif nums1A > nums2B:
                r = mid - 1
            else:
                l = mid + 1
