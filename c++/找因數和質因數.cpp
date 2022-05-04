#include<iostream>
using namespace std;
int main()
{
	int num,num_1=0,num_2=0;
	int i=0;
	cout<<"叫块计碝тㄤ计㎝借计";
	cin>>num;
	
	for(int a=1;num>=a;a++){	
		if(num%a==0){
			cout<<a<<' ';
			num_1++;
			for(int b=1;b<=a;b++){     
				if(a%b==0){
					i++;	
				}					
			}	
		}
		if(i==2){			
			num_2++;
		}	i=0	;									
						
	} 
			
		
	cout<<"\n计タ计Τ"<<num_1<<""; 
	cout<<"\n计タ借计Τ"<<num_2<<"";	
}	

