#pragma once
#include<iostream>
using namespace std;

class student
{
    char* Name;
    int age;
    char* Studentid;
    
    
public:
    //student();
    student(char* a=nullptr, int b=0, char* c=nullptr);
    char* getStudentid();
    char* getName();
    int getAge();
    void setStudentid(char* x);
    void setName(char* x);
    void setAge(int x);
    void display();
};

void Deep_Copy(char* src, char*& des);