#include<iostream>
using namespace std;
int main()
{
	int weight_1,weight_2,i=0;
	cout<<"�п�J���ۭ쥻���q(kg)�G";
	cin>>weight_1;
	cout<<"�п�J���۰I�ܫ᭫�q(kg)�G";
	cin>>weight_2;
	
	while(weight_1>weight_2){
		weight_1/=2;
		i++;
	}
	
	switch(i){
		case 1 ... 10:
			cout<<"�g�L"<<i<<"���b�I��"<<"�A�o�����٫ܦ~��";
			break;
		case 11 ... 20:
			cout<<"�g�L"<<i<<"���b�I��"<<"�A�o���ۦ~�N�[��";
			break;
		default:
			cout<<"���ۦ~�N�L��[���A�L�k���w";
	}
}

