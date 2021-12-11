#include"heading.h"


void Deep_Copy(char* Source, char*& Dest)
{
    
    if (Dest == nullptr)
    {
        int size = strlen(Source) + 1;
        Dest = new char[size];
        strcpy_s(Dest, size, Source);
    }
}
student::student(char* a, int b, char* c)
{
    Deep_Copy(a, Studentid);
    setAge(b);
    Deep_Copy(c, Name);
}

char* student::getName()
{
    char* x = nullptr;
    Deep_Copy(x, Name);
    return x;
}
char* student::getStudentid()
{
    char* x = nullptr;
    Deep_Copy(x, Studentid);
    return x;
}
int student::getAge()
{
    return age;
}

void student::setName(char* x)
{
    if (Name != nullptr)
    {
        delete[] Name;
        Name = nullptr;
    }
    Deep_Copy(Name, x);
}
void student::setStudentid(char* x)
{
    if (Studentid != nullptr)
    {
        delete[] Studentid;
        Studentid = nullptr;
    }
    Deep_Copy(Studentid, x);
}
void student::setAge(int x)
{
    if (x > 0)
    {
        age = x;
    }
}

void student::display()
{
    cout << "The ID of student is = " << Studentid << endl;
    cout << "The age of student is = " << age << endl;
    cout << "The name of student is = " << Name << endl;
    
}