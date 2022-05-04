#include<iostream>
using namespace std;
int main()
{
	int weight_1,weight_2,i=0;
	cout<<"請輸入岩石原本重量(kg)：";
	cin>>weight_1;
	cout<<"請輸入岩石衰變後重量(kg)：";
	cin>>weight_2;
	
	while(weight_1>weight_2){
		weight_1/=2;
		i++;
	}
	
	switch(i){
		case 1 ... 10:
			cout<<"經過"<<i<<"次半衰期"<<"，這岩石還很年輕";
			break;
		case 11 ... 20:
			cout<<"經過"<<i<<"次半衰期"<<"，這岩石年代久遠";
			break;
		default:
			cout<<"岩石年代過於久遠，無法測定";
	}
}

