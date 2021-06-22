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

	bool input_matrix_start_flag = false;//�����ж����Ƿ�Ҫ����profit table������
	int course_num = 0;
	
	while (!inputfile.eof())
	{
		getline(inputfile, s);

		vector<int> num_element;
		int element_count = 0;//��¼��һ���ж��ٸ�element
		istringstream insert_string(s);
		int insertdata_temp;
		///////////////////////////////////////
		while (insert_string >> insertdata_temp)
		{
			num_element.push_back(insertdata_temp);        //����һ�е�����element����¼��num_element��
			element_count++;
		}
		// element_count ׼ȷ֪��ÿһ�е�����,û�а�resource�ӽ�ȥ
		if (element_count > 1)
		{
			if (input_matrix_start_flag == false)//no profit table
			{
				course_num = 0;
				profit.clear();//ÿ�δ洢profit֮ǰ�������
				for (int i = 0; i < num_element.size(); i++)
				{
					profit.push_back(num_element[i]);
					course_num++;
				}
				input_matrix_start_flag = true;//there is a profit table
											   //course׼ȷ֪���ж����ſ�
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
			int resource = num_element[0];//resourceÿ��׼ȷ��¼��resource������

			vector <int>best_profit;
			
			int per_courser_limit = resource - course_num + 1;//ÿ�ſ�Ŀ�ڵ�ǰ��Դ���������������Է��������

			for (int i = 1; i <= per_courser_limit; i++) {
				best_profit.push_back(profit[((i - 1)*course_num)])  ;//��Ϊ�����������Դ���������ǿ�Ŀ														   
				//��һ����Ŀ�������Դ������ȷ
			}

			for (int i = 1; i < course_num; i++)//i�ǵ�ǰ�ڼ�����Ŀ i=1�ǵڶ�����Ŀ
			{
				for (int j = i + 1; j <= (per_courser_limit)+i; j++)//j������Դ
				{
					int max = 0;
					for (int x3 = 1; x3 < j; x3++)//����ǰ��Ŀ�����������ʣ�µĸ�������Ŀ,<j����Ϊ��Ҫ��
					{
						int x3_ = x3;

						if (x3 >  per_courser_limit)
							x3_ = per_courser_limit;//��ÿ����Ŀ������������ܳ���һ��limit

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