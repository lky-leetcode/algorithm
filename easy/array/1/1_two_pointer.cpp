/*************************************************************************
	> File Name: 1_two_pointer.cpp
	> Author: lky
	> Mail: lkyleetcode@gmail.com 
	> Created Time: 六  7/25 22:20:59 2020
 ************************************************************************/

#include<iostream>
#include<vector>
using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
		int low, high;
		vector<int> ans;
		low = 0;
		high = nums.size() - 1;
		sort(nums.begin(), nums.end());
		while (low < high)
		{
			if (nums[low] + nums[high] == target)
			{
				ans.push_back(low);
				ans.push_back(high);
				return ans;
			}
			else if (nums[low] + nums[high] > target)
			{
				high--;
			}
			else
			{
				low++;
			}

		}
		return ans;
    }
};

int main()
{
	vector<int> ans, nums;
	int arrCount, target;
	cin >> arrCount;
	Solution s;
	/*
	 * input test 
	 */
	for (int i = 0; i < arrCount; i++)
	{
		int n;
		cin >> n;
		nums.push_back(n);
	}
	cin >> target;
	ans = s.twoSum(nums, target);

	/*
	 * output answer
	 */
	for (int i = 0; i < ans.size(); i++)
	{
		cout << ans[i] << endl;
	}
}
