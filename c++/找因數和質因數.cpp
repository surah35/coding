#include<iostream>
using namespace std;
int main()
{
	int num,num_1=0,num_2=0;
	int i=0;
	cout<<"�п�J�@�ӼƦr�M���]�ƩM��]�ơG";
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
			
		
	cout<<"\n���Ʀr���]�Ʀ�"<<num_1<<"��"; 
	cout<<"\n���Ʀr����]�Ʀ�"<<num_2<<"��";	
}	

