#include"heading.h"

int main()
{
    int Age = 0;
    char* Name = nullptr;
    char* name1 = nullptr;
    char* Id = nullptr;
    char* Id1 = nullptr;
    /*char ID[14] = { "L1F20BSCS0002" };
    char name[20] = { "Syed Muhammad Ali" };
    int age = 20;
    student S1(ID, age, name);*/
    //S1.display();
    cout << endl;
    cout << "Enter the age of second student = ";
    cin >> Age;
    cin.ignore();
    cout << "Enter the ID of second student = ";
    Id = new char[25];
    cin >> Id;

    cin.ignore();
    cout << "Enter the name of second student = ";
    Name = new char[25];
    cin >> *Name;
    
  //  Deep_Copy(name1, Name);
   // Deep_Copy(Id1, Id);
    //student S2(Id1, Age, name1);
    //S2.getAge();
    return 0;
}