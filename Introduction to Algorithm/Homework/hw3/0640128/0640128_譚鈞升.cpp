#include <iostream>
#include <vector>
#include <fstream>
#include <cstring>
#include <string>
#include<sstream>

using namespace std;

int main() {
	ifstream inputfile;
	ofstream outputfile;

	inputfile.open("input.txt", ios::in);
	outputfile.open("output.txt", ios::out);

	string s;
	vector<int> profit;

	bool input_matrix_start_flag = false;//用来判断我是否要进行profit table的输入
	int course_num = 0;
	
	while (!inputfile.eof())
	{
		getline(inputfile, s);

		vector<int> num_element;
		int element_count = 0;//记录这一行有多少个element
		istringstream insert_string(s);
		int insertdata_temp;
		///////////////////////////////////////
		while (insert_string >> insertdata_temp)
		{
			num_element.push_back(insertdata_temp);        //把这一行的所有element都记录到num_element里
			element_count++;
		}
		// element_count 准确知道每一行的数量,没有把resource加进去
		if (element_count > 1)
		{
			if (input_matrix_start_flag == false)//no profit table
			{
				course_num = 0;
				profit.clear();//每次存储profit之前进行清空
				for (int i = 0; i < num_element.size(); i++)
				{
					profit.push_back(num_element[i]);
					course_num++;
				}
				input_matrix_start_flag = true;//there is a profit table
											   //course准确知道有多少门课
			}
			else
			{
				for (int i = 0; i < num_element.size(); i++)
				{
					profit.push_back(num_element[i]);
				}
			}
		}
		else if (element_count == 1)
		{
			////////////
			int resource = num_element[0];//resource每次准确记录了resource的数量

			vector <int>best_profit;
			
			int per_courser_limit = resource - course_num + 1;//每门科目在当前资源数的限制下最多可以分配多少天

			for (int i = 1; i <= per_courser_limit; i++) {
				best_profit.push_back(profit[((i - 1)*course_num)])  ;//因为表格纵轴是资源数，横轴是科目														   
				//第一个科目的最佳资源计算正确
			}

			for (int i = 1; i < course_num; i++)//i是当前第几个科目 i=1是第二个科目
			{
				for (int j = i + 1; j <= (per_courser_limit)+i; j++)//j是总资源
				{
					int max = 0;
					for (int x3 = 1; x3 < j; x3++)//给当前科目分配的天数，剩下的给其他科目,<j是因为还要留
					{
						int x3_ = x3;

						if (x3 >  per_courser_limit)
							x3_ = per_courser_limit;//给每个科目分配的天数不能超过一定limit

						int temp = profit[((x3_ - 1)*course_num + i)] + best_profit[(  (i - 1)*per_courser_limit + (j - x3) - i  )] ;//  best_profit[i - 1][j - x3_]

						if (temp >= max)
						{
							max = temp;
						}
					}
					best_profit.push_back(max);
				}
			}
			outputfile << best_profit.back() << endl;
		}
		else
		{
			input_matrix_start_flag = false;
		}
	}
}