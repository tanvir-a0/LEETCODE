#include <iostream>
#include <cmath>
#include <vector>

using namespace std;

vector<int> twoSum(vector<int>& nums, int target) {
    vector<int> result;
    //cout << nums.size() << endl;
    for(int i = 0 ; i < nums.size() ; i = i + 1){
        for(int j = i+1; j < nums.size(); j = j + 1 ){
            if ((nums[i] + nums[j]) == target){
                result.push_back(i);
                result.push_back(j);
                //cout << i << " " << j << endl;
            }
        }
    }

    return result;
}
 
int main() {
    
    vector<int> nums = {2, 7, 11, 15};
    vector<int> result = twoSum( nums ,  9);
    cout << "[" << result[0] << "," << result[1] << "]" << endl;

    vector<int> nums2 = {3, 2, 4};
    vector<int> result2 = twoSum( nums2 ,  6);
    cout << "[" << result2[0] << "," << result2[1] << "]" << endl;
    
}
 