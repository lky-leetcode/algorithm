/*************************************************************************
	> File Name: 1.cpp
	> Author: lky
	> Mail: lkyleetcode@gmail.com 
	> Created Time: 六  7/18 23:23:55 2020
 ************************************************************************/

#include<iostream>
#include<algorithm>
#include<vector>
#include<unordered_map>
using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) 
	{
		unordered_map<int, int> hash;
		vector<int> ans;
		for (int i = 0; i < nums.size(); i++)
		{
			int n = target - nums[i];
			auto it = hash.find(n);
			if (it != hash.end())
			{
				ans.push_back(it->second);
				ans.push_back(i);
				return ans;   // exactly one solution
			}
			hash[nums[i]] = i;
		}
		return ans;
    }
};

int main()
{
	Solution s;
	vector<int> arr;
	int target;
	int number;
	cin >> number;
	vector<int> ans;
	for (int i = 0; i < number; i++)
	{
		int input;
		cin >> input;
		arr.push_back(input);
	}
	cin >> target;
	ans = s.twoSum(arr, target);
	cout << ans[0] << "," << ans[1] << endl;
	return 0;
}

