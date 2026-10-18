#include<iostream>
int main(){
    std::cout<<"Hello, World! \n";
    int minutes = 0;
    if(!(std::cin>>minutes)){
        std::cout << "Please enter an integer.\n";
        return 1;
    }
    if (minutes <= 0) {
        std::cout << "Minutes must be greater than 0.\n";
        return 1;
    }
    double hours = minutes / 60.0;
    bool enough = minutes >= 30;
    std::cout<<"Minutes: "<<minutes<<"\n";
    std::cout<<"Hours: "<<hours<<"\n";
    if (enough) {
        std::cout << "You studied for at least 30 minutes.\n";
    } 
    else {
        std::cout << "You studied for less than 30 minutes.\n";
    }
}