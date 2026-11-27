#include <iostream>
#include <string>
#include<vector>
#include<fstream>
struct Record{
    std::string subject;
    int minutes;
};
std::vector<Record> load_records
(const std::string& filename){
    std::vector<Record> records;
    std::ifstream f(filename);
    if(!f){
        std::cout<<"Can not open file.\n";
        return records;
    }
    Record r{"",0};
    while(f>>r.subject>>r.minutes){
        records.push_back(r);
    }
    return records;
}
int sum_minute
(const std::vector<Record>& records){
    int sum=0;
    for(const Record& r: records){
        sum+=r.minutes;
    }
    return sum;
}
int max_minutes
(const std::vector<Record>& records){
    int max=0;
    for(const Record& r:records){
        if(r.minutes>=max){
            max=r.minutes;
        }
    }
    return  max;
}
int main(){
    std::vector<Record> records =
    load_records("build/records_export.txt");
    for(const Record& r:records){
        std::cout<<r.subject<<" "<<r.minutes<<"mins\n";
    }
    std::cout<<"loaded records: "<<records.size()<<"\n";
    std::cout << "Total minutes: "
          << sum_minute(records) << "\n";

    std::cout << "Max minutes: "
          << max_minutes(records) << "\n";
}