#include <algorithm>
#include <cstdlib>
#include <iostream>
#include <string>
using U=unsigned __int128;
std::string dec(U v){if(!v)return "0";std::string s;while(v){s.push_back('0'+v%10);v/=10;}std::reverse(s.begin(),s.end());return s;}
int main(int argc,char**argv){
  if(argc!=3)return 2;
  const int J=std::atoi(argv[1]),N=std::atoi(argv[2]);
  if(J<3||J>100||N<10000||N>20000000)return 3;
  U D=1;for(int i=0;i<24;++i)D*=10;
  for(int a=2;a<=J;++a)for(int b=a;b<=J;++b){
    U total=0;
    for(long long r=1;r<=N;++r){
      U num=D*(r%a)*(r%b);
      U den=U(a)*b*r*(r+1);
      total+=num/den;
    }
    std::cout<<a<<" "<<b<<" "<<dec(total)<<"\n";
  }
}
