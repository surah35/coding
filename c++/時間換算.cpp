#include<iostream>
using namespace std;
int main()
{
  y:
	  int sec,min=0,hr=0;
	  cout<<"請輸入秒數(s):";
	  cin>>sec;
	  if(sec<60){
	  	sec%=60;
	  }
	  else if(sec>=60){
	  	min=sec/60;
	  	sec%=60;
	  	if(min>=60){
	  		hr=min/60;
			min%=60;	
	  	}
	  	
	  	
	  }
	  
	  
	  cout<<"換算後："<<hr<<"時"<<min<<"分"<<sec<<"秒"<<endl;
	  goto y;
}

