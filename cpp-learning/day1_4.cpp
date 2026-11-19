#include <iostream>
#include <string>
#include<vector>
void aver(int count,int total){
    std::cout<<"Records:"<<count<<"\n";
    if(count>0){
        double average=total*1.0/count;
        std::cout << "Average minutes: " << average << "\n";
} else {
    std::cout << "No records.\n";
    }
}
int sum_minute(const std::vector<int>& values){
    int sum=0;
    if(values.empty()){
        return 0;
    }
    for(int v:values){
        sum+=v;
    }
    return sum;
}
int max_minutes(int count,const std::vector<int> &values){
    int max=0;    
    for(int i=0;i<=count-1;i++){
        if(i==0){
            max=values[i];
        }
        if(values[i]>max){
            max=values[i];
        }
    }
    return max;
}
double to_hour(int minutes){
    return minutes / 60.0;
}
void print_level(int minutes){
    if (minutes >= 30) {
            std::cout << "You studied for at least 30 minutes.\n";
        } else {
            std::cout << "You studied for less than 30 minutes.\n";
        }
}
int main() {
    //std::vector<int> scores;
    //scores.push_back(70);
    //scores.push_back(90);
    //std::cout<<scores.size()<<"\n";
    //for(int score:scores){
    //    std::cout<<score<<"\n";
    //}

    /*std::vector<int> scores={70,90,80};
    std::cout<<scores[0]<<scores[1]<<scores[2]<<"\n";
    if(scores.empty()){
        std::cout<<"No scores.\n"
    }*/

    //std::cout << "Hello, World!\n";
    int total_minutes=0,total_cpp = 0;
    int count =0;
    std::vector<int> mins;
    while(1){
        std::cout << "Enter minutes (0 to finish):\n";
        int minutes = 0;
        if (!(std::cin >> minutes)) {
            // 严重的输入流错误：结束程序
            if (std::cin.bad()) {
                std::cout << "Input error.\n";
                return 1;
            }
            // 输入已经结束：退出循环，继续显示已有统计
            if (std::cin.eof()) {
                break;
            }
            // 普通的格式错误，例如输入了abc
            std::cout << "Please enter an integer.\n";
            // 第一步：清除失败状态
            std::cin.clear();
            // 第二步：丢弃这一行剩余的错误内容
            std::cin.ignore(1000,'\n');
            // 第三步：跳过本轮后面的判断、累计，重新输入
            continue;
        }
        if(minutes == 0){
            break;
        }
        if (minutes < 0) {
            std::cout << "Minutes must be greater than 0.\n";
            continue;
        }
        std::string subject="";
        std::cout<<"Enter subject\n";
        if(!(std::cin>>subject)){
            std::cout << "Input error.\n";
                return 1;
        }
        mins.push_back(minutes);
        if(subject=="cpp"){
            total_cpp+=minutes;
        }
        total_minutes += minutes;
        count++;
        double hours = to_hour(minutes);
        std::cout << "Subject: "<< subject << "\n";
        std::cout << "Minutes: " << minutes << "\n";
        std::cout << "Hours: " << hours << "\n";
        print_level(minutes);
    }
    int sum=sum_minute(mins),max=max_minutes(count,mins);
    aver(count,total_minutes);
    if(mins.empty()){
        std::cout<<"no records\n";
    }else{
        std::cout<<"Total minuts from vector:"<<sum<<"\n";
        std::cout<<"max minutes:"<<max<<"\n";
    }
    std::cout << "Total minutes: " << total_minutes << "\n";
    std::cout << "Total hours: " << total_minutes / 60.0 << "\n";
    std::cout << "Total minutes for cpp: " << total_cpp << "\n";
    for(int min:mins){
        std::cout<<min<<" ";
    }
    std::cout<<"\nSaved records: " <<mins.size()<<"\n";
    return 0;
}